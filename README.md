# MonitorGGConnectivity

## Overview

This sample code will monitor the runtime.log file in Greengrass 1.x for "Reconnect" or "Connected" messages. This will allow Greengrass to notify processes locally on the current connectivity state with AWS IoT Core. This sample code can be used to monitor other types of log files for a similar use case or for data collection.

## Steps To Install

1) Create a new Lambda function using Python 3.7

2) Download/Clone this repository as a zip file and upload this to your new Lambda function.

![UploadZip](/images/upload_zip.png) 

3) Move out files and folder into the root folder of the lambda. Delete the empty folder.
   
![MoveFiles](/images/move_out_files.png) 

4) Publish this Lambda Function to create a new version and assign that to an alias.

5) In your Greengrass configuration, select the Lambda function you just created.

![AddLambda](/images/add_lambda.png) 

5) Once you have added this Lambda function, configure it with the following settings

![Configure Lambda](/images/lambda_configuration.png) 

6) Since it requires root access to read this log file, you will also need to allow your Lambda to run as root. Update your config.json file as described here. https://docs.aws.amazon.com/greengrass/latest/developerguide/lambda-group-config.html#lambda-running-as-root

7) Create Subscriptions in your Greengrass configuration to route messages from the Lambda function to be handled.