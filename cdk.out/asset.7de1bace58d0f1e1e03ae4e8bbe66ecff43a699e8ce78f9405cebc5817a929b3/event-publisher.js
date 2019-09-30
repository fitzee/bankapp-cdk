'use strict';
const REGION = process.env.REGION
const EVENT_BRIDGE_ARN = process.env.EVENT_BRIDGE_ARN
const EVENT_BUS_NAME = EVENT_BRIDGE_ARN.split('/').slice(-1)[0]

const AWS = require('aws-sdk')
AWS.config.update({region: REGION});

var eventbridge = new AWS.EventBridge({apiVersion: '2015-10-07'});
const cloudwatchevents = new AWS.CloudWatchEvents();

const processRecord = async (record) => {
  if (record.eventName !== 'INSERT') return

  const item = AWS.DynamoDB.Converter.unmarshall(record.dynamodb.NewImage)
  let result
  let putAttempts = 0
  const maxRetries = 5
  let params
  while (!result || (result.FailedEntryCount > 0 && putAttempts < maxRetries)) {
    putAttempts += 1
    params = {
      Entries: [
        {
          Detail: JSON.stringify(item.data),
          DetailType: item.name,
          EventBusName: EVENT_BUS_NAME,
          Source: record.eventSourceARN,
          // Time: new Date || 'Wed Dec 31 1969 16:00:00 GMT-0800 (PST)' || 123456789
        }
      ]
    };
    result = await eventbridge.putEvents(params).promise()
  }

  if (result.FailedEntryCount !== 0 && putAttempts >= maxRetries) {
    //TODO Put this item in a Dead Letter Queue since we failed to publish it to EventBridge many times?
    console.error('Failed to put event into EventBridge', JSON.stringify(params), 'Error:', JSON.stringify(result), 'Record:', JSON.stringify(record))
  } 
  else {
    console.info('Published event', JSON.stringify(params))
  }
}


const processRecords = async (records) => {
  for (let record of records) {
    await processRecord(record)
  }
}

module.exports.handler = async event => {
  await processRecords(event.Records)
};
