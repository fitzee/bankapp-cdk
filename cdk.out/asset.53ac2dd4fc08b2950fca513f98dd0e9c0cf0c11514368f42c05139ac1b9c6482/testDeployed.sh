#! /bin/bash
set -x

#ENDPOINT="$(serverless info --verbose | grep ServiceEndpoint | sed s/ServiceEndpoint\:\ //g)"
ENDPOINT="https://9u0g56aria.execute-api.us-east-1.amazonaws.com/prod/"

# SUBMIT APPLICATION THAT PASSES CHECKS
RES=$(echo '{"command": "SUBMIT_NEW_ACCOUNT_APPLICATION", "data": {"name":"Gabe"}}' | http POST "$ENDPOINT" -b)
echo $RES
APP_ID=$(echo $RES | jq ".data.application.id" -r)
echo $APP_ID


# SUBMIT APPLICATION THAT FAILS ID CHECK
RES=$(echo '{"command": "SUBMIT_NEW_ACCOUNT_APPLICATION", "data": {"name":"Gabe-evil"}}' | http POST "$ENDPOINT" -b)
echo $RES
APP_ID=$(echo $RES | jq ".data.application.id" -r)
echo $APP_ID

# # FLAG FOR REVIEW
# RES=$(echo '{"command": "FLAG_ACCOUNT_APPLICATION_FOR_HUMAN_REVIEW", "data": {"id":"'"$APP_ID"'", "reason": "Testing", "taskTokenId": "stepfunc-abcd1234"}}' | http POST "$ENDPOINT" -b)
# echo $RES

# APPROVE FLAGGED APPLICATION
echo "Sleeping a bit to let the step function kick off and wait for human review for evil Gabe..."
sleep 5
echo "Approving evil gabe with application id $APP_ID"
RES=$(echo '{"command": "PROCESS_HUMAN_REVIEW", "data": {"id":"'"$APP_ID"'", "decision":"APPROVE"}}' | http POST "$ENDPOINT" -b)
echo $RES

# # CREATE
# RES=$(echo '{"command": "CREATE_ACCOUNT", "data": {"name": "Gabe", "applicationId":"'"$APP_ID"'" }}' | http POST "$ENDPOINT" -b)
# echo $RES
# ACC_ID=$(echo $RES | jq ".data.account.id" -r)
# echo $ACC_ID