import os
import os.path
import sys
import time

envLambdaTaskRoot = os.environ["LAMBDA_TASK_ROOT"]
print("LAMBDA_TASK_ROOT env var:" + os.environ["LAMBDA_TASK_ROOT"])
print("sys.path:" + str(sys.path))

sys.path.insert(0, envLambdaTaskRoot + "/eventbridge_handler")
print("sys.path:" + str(sys.path))
import botocore
import boto3

print("boto3 version:" + boto3.__version__)
print("botocore version:" + botocore.__version__)


# SDK documentation implies delete_event_bus() deletes all associated rules, this is not the case - so do the
# necessary rule deletes here...
def delete_event_bus(client: boto3.client, event_bus_name: str):
    rules = client.list_rules(EventBusName=event_bus_name)
    for rule in rules['Rules']:
        client.delete_rule(Name=rule['Name'], EventBusName=event_bus_name, Force=True)

    client.delete_event_bus(Name=event_bus_name)


def main(event, context):
    import logging as log
    import cfnresponse
    log.getLogger().setLevel(log.INFO)

    log.info('Input event: %s', event)
    event_bus_name = event['ResourceProperties']['Name']
    # This needs to change if there are to be multiple resources in the same stack
    physical_id = 'EventBridgeCustomResource'+'-'+event_bus_name

    try:
        eventbridge_client = boto3.client('events')

        # Check if this is a Create and we're failing Creates
        if event['RequestType'] == 'Create' and event['ResourceProperties'].get('FailCreate', False):
            raise RuntimeError('Create failure requested')
        elif event['RequestType'] == 'Delete':
            log.info('About to delete the event bus ' + event_bus_name)
            # if this is a delete, just remove the bus - all rules will be deleted accordingly
            delete_event_bus(eventbridge_client, event_bus_name)
            log.info('Deleted the event bus and all associated rules!')
        else:
            # if this is an update, delete the existing bus first then re-create
            if event['RequestType'] == 'Update':
                delete_event_bus(eventbridge_client, event_bus_name)

            # create the event bus
            event_bus = eventbridge_client.create_event_bus(Name=event_bus_name)

            attributes = {
                'EventBusArn': event_bus['EventBusArn'],
            }

            event_rules = event['ResourceProperties']['Rules']
            for rule in event_rules:
                res = eventbridge_client.put_rule(Name=rule['name'], State=rule['state'], EventPattern=rule['pattern'],
                                                  EventBusName=event_bus_name)

            event_targets = event['ResourceProperties']['Targets']
            for target in event_targets:
                targets = []
                for target_arn in target['arns']:
                    targets.append({'Id': 'Id_'+str(int(time.mktime(time.localtime()))), 'Arn': target_arn})

                res = eventbridge_client.put_targets(Rule=target['rule'], EventBusName=event_bus_name,
                                                     Targets=targets)

        cfnresponse.send(event, context, cfnresponse.SUCCESS, attributes, physical_id)
    except Exception as e:
        log.exception(e)
        # cfnresponse's error message is always "see CloudWatch"
        cfnresponse.send(event, context, cfnresponse.FAILED, {}, physical_id)
