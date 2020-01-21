
# A CDK'ized Version of the Demo Banking Service


UPDATE Jan-21-2020:
  * Now takes advantage of EventBridge native support in CloudFormation
  * Remove CustomResource code to create event bus etc.
  * Will send an email via SNS subscription for human approved events

Install the CDK with `npm install -g aws-cdk` 

Run the `pip install -r requirements.txt` command to install the necessary Python modules.

`cdk deploy AccountApplicationService-dev` should be all that is required to deploy all the stacks!

# Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
