'use strict';
const REGION = process.env.REGION
const ACCOUNTS_TABLE_NAME = process.env.ACCOUNTS_TABLE_NAME
const EVENTS_TABLE_NAME = process.env.EVENTS_TABLE_NAME

const AWS = require('aws-sdk')
const uuid = require('uuid/v4')
AWS.config.update({region: REGION});

const dynamo = new AWS.DynamoDB.DocumentClient();
const accountKey = id => `account|${id}`


const getAccount = async (id) => {
    const params = {
      TableName: ACCOUNTS_TABLE_NAME,
      Key: { id: id }
    };
    
    const result = await dynamo.get(params).promise()    
    return result.Item
}


const Event = (name, data) => {
    return {
        id: uuid(),
        name,
        data
    }
}


const createAccount = async ({applicationId, name}) => {
    const id = uuid()
    const account = { id: accountKey(id), name, balance: 0 }
    const event = Event('ACCOUNT_CREATED', { account, applicationId })
    const params = {
        TransactItems: [
            {
                Put: {
                    TableName: ACCOUNTS_TABLE_NAME,
                    Item: account
                }
            },
            {
                Put: {
                    TableName: EVENTS_TABLE_NAME,
                    Item: event
                },
            }
        ]
    };
    await dynamo.transactWrite(params).promise()
    return event
} 


const creditAccount = async (data) => {
    let { id, amount, note } = data
    amount = parseInt(amount, 10)

    return adjustAccount(id, amount, note)    
}


const debitAccount = async (data) => {
    let { id, amount, note } = data
    amount = parseInt(amount, 10)

    return adjustAccount(id, amount * -1, note)    
}


const adjustAccount = async (id, amount, note) => {
    const existingAccount = await getAccount(id) 
    if (!existingAccount) {
        throw new Error(`Account with ID ${id} doesn't exist!`)
    }
    
    const params = {
      TableName: ACCOUNTS_TABLE_NAME,
      Key: { id: id },
      UpdateExpression: 'ADD #balance :amount',
      ExpressionAttributeNames: {'#balance' : 'balance'},
      ExpressionAttributeValues: {
        ':amount' : amount,
      }
    };
    await dynamo.update(params).promise()

    const [eventName, eventAmount] = amount < 0 ? ['ACCOUNT_DEBITED', amount * -1] : ['ACCOUNT_CREDITED', amount]
    return { 
        name: eventName,
        data: { 
            id, 
            amount: eventAmount, 
            note
        }
    }
}


const commandHandlers = {
    'CREATE_ACCOUNT': createAccount,
    'CREDIT_ACCOUNT': creditAccount,
    'DEBIT_ACCOUNT': debitAccount,
}


const eventType = (event) => {
    if (event.requestContext && event.requestContext.apiId) return 'APIGatewayRequest'
    if (event.source && event["detail-type"] && event.detail) return 'EventBridgeEvent'
    return 'Unknown'
}


const handleAPIGatewayRequest = async (event) => {
    const params = JSON.parse(event.body)
    const result = await commandHandlers[params.command](params.data)

    const response = {
        statusCode: 200,
        body: JSON.stringify(result),
    };
    return response
}


const handleEventBridgeEvent = async (event) => {
    const handlers = {
        'APPLICATION_APPROVED': async (event) => { return createAccount({ name: event.detail.application.name, applicationId: event.detail.application.id })  }
    }
    const detailType = event["detail-type"]

    if (handlers[detailType] === undefined ) {
        console.error("Recieved event we don't know how to handle:", JSON.stringify(event))
        return
    }

    const result = await handlers[event["detail-type"]](event)
    return result
}


module.exports.handler = async (event) => {
    try {
        const handlers = {
            'APIGatewayRequest': handleAPIGatewayRequest,
            'EventBridgeEvent': handleEventBridgeEvent
        }
        const handler = handlers[eventType(event)]
        await handler(event)
    }
    catch(ex) {
        console.error('Exception:', ex, 'Event:', JSON.stringify(event))
        throw ex
    }
};
