'use strict';
const REGION = process.env.REGION
const STAGE = process.env.STAGE
const ACCOUNTS_TABLE_NAME = process.env.ACCOUNTS_TABLE_NAME
const EVENTS_TABLE_NAME = process.env.EVENTS_TABLE_NAME
//const OPEN_ACCOUNT_STEP_FUNCTION_ARN = process.env.OPEN_ACCOUNT_STEP_FUNCTION_ARN

const AWS = require('aws-sdk')
const uuid = require('uuid/v4')
AWS.config.update({region: REGION});

const dynamo = new AWS.DynamoDB.DocumentClient();
const stepfunctions = new AWS.StepFunctions();
const ssm = new AWS.SSM();

const applicationKey = id => `application|${id}`


const getApplication = async (id) => {
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


const submitNewAccountApplication = async (data) => {
    const id = uuid()
    const { name } = data
    const application = { id: applicationKey(id), name, state: 'SUBMITTED' }
    const event = Event('APPLICATION_SUBMITTED', { application })

    const request= await ssm.getParameter({'Name':'StateMachineArnSSM'}).promise()
    const OPEN_ACCOUNT_STEP_FUNCTION_ARN = request.Parameter.Value

    let params = {
        TransactItems: [
            {
                Put: {
                    TableName: ACCOUNTS_TABLE_NAME,
                    Item: application
                }
            },
            {
                Put: {
                    TableName: EVENTS_TABLE_NAME,
                    Item: event
                }
            }
        ]
    };
    await dynamo.transactWrite(params).promise()

    params = {
        "input": JSON.stringify({ application }),
        "name": `ProcessAccountApplication-${id}`,
        "stateMachineArn": OPEN_ACCOUNT_STEP_FUNCTION_ARN
    }
    await stepfunctions.startExecution(params).promise()

    return event
} 


const updateApplication = async (id, attributes, event) => {
    const application = await getApplication(id)
    const updatedApplication = Object.assign(application, attributes)
    const params = {
        TransactItems: [
            {
                Put: {
                    TableName: ACCOUNTS_TABLE_NAME,
                    Item: updatedApplication
                }
            },
            {
                Put: {
                    TableName: EVENTS_TABLE_NAME,
                    Item: event
                }
            }
        ]
    };
    return dynamo.transactWrite(params).promise()
}

const flagForReview = async (data) => {
    const { id, reason, taskToken } = data

    const event = Event('APPLICATION_FLAGGED_FOR_REVIEW', { id, reason, taskToken })
    await updateApplication(
        id, 
        {
            state: 'WAITING_FOR_REVIEW',
            reason,
            taskToken
        },
        event
    )

    return event
}


const processHumanReview = async (data) => {
    const { id, decision } = data
    if (decision !== 'APPROVE' && decision !== 'REJECT') {
        throw new Error("Required `decision` parameter must be 'APPROVE' or 'REJECT'")
    }

    const application = await getApplication(id)
    let params = {
        output: JSON.stringify({
            decision
        }),
        taskToken: application.taskToken
    };
    await stepfunctions.sendTaskSuccess(params).promise()

    const event = Event('HUMAN_REVIEWED_APPLICATION', { id, application, decision })
    params = {
        TableName: EVENTS_TABLE_NAME,
        Item: event
    }
    await dynamo.put(params).promise()

    return event
}


const approveApplication = async (data) => {
    const { id } = data

    const application = await getApplication(id)

    const event = Event('APPLICATION_APPROVED', { id, application })
    await updateApplication(
        id, 
        { state: 'APPROVED', },
        event
    )

    return event
}


const rejectApplication = async (data) => {
    const { id, reason } = data

    const event = Event('APPLICATION_REJECTED', { id, application })
    await updateApplication(
        id, 
        { state: 'REJECTED', },
        event
    )

    return event
}



const commandHandlers = {
    'SUBMIT_NEW_ACCOUNT_APPLICATION': submitNewAccountApplication,
    'FLAG_ACCOUNT_APPLICATION_FOR_HUMAN_REVIEW': flagForReview,
    'PROCESS_HUMAN_REVIEW': processHumanReview,
    'APPROVE_ACCOUNT_APPLICATION': approveApplication,
    'REJECT_ACCOUNT_APPLICATION': rejectApplication,
}

module.exports.handler = async(event) => {
    try {
        const isAPiGatewayRequest = event.requestContext && event.requestContext.apiId
        const params = typeof event.body === "string"
            ? JSON.parse(event.body)
            : event.body
        const result = await commandHandlers[params.command](params.data)

        if (!isAPiGatewayRequest) 
            return result

        const response = {
            statusCode: 200,
            body: JSON.stringify(result)
        };
        return response;
    } catch (ex) {
        console.error(ex)
        console.info('event', JSON.stringify(event))
    }
};
