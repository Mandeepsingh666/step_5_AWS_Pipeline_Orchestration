# Pipeline Orchestration with AWS lambda 
## Goal 
 My goal for this project was to show my knowlage of Pipeline Orchestration,python,
 boto3 module ,AWS lambda , AWS IAM roles , AWS S3 buckets and AWS Eventbridge.In this step of the project, i EXTRACTED data from the Source (api) then TRANSFORMED the data into appropriate format like from JSON to CSV for future analytical needs and then LOADED the data into AWS s3 bucket. The data is updated every 3 months.
 
 ## Prerequisites:
 1) Need a AWS account. 
 2) knowledge of AWS cloud sepcialy Lambda , s3 buckets and Iam roles.
 3) knowlege of python modules Pandas and boto3.
 

 ## Outline of Steps:
 1) Need create a AWS IAM role in which use case is for Lambda and  permissions policies s3 put policy and AWSLambdaBasicExecutionRole
 
 s3_put_policy
 ```
   {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": "s3:PutObject",
            "Resource": "*"
        }
    ]
}
```
AWSLambdaBasicExecutionRole
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": "*"
        }
    ]
}
```
2) Create a AWS lambda function to Extract data from api.
#### NOTE :In order to use pandas module. we need to crate AWS lambda layers which contain zip file contaning pandas module files. 
#### helpfull link : https://towardsdatascience.com/python-packages-in-aws-lambda-made-easy-8fbc78520e30
 
Python modules needed
``` 
import pandas 
import boto3
import json
```
3) Then we need to add trigger for our AWS lambda function.in this use case trigger is AWS EventBridge.
4)In AWS Eventbridge we need to create a event which trigger AWS lambda function. it accepts cron script or run expressions.
#### NOTE: AWS cron syntax is different then regual syntax
syntax
```
cron(fields)
```

 ## Technology used in project:
 ![download](https://user-images.githubusercontent.com/44817812/149073611-2bd6fffa-fdb1-44bd-96bb-5af5743c970c.jpeg)
 ![download](https://user-images.githubusercontent.com/44817812/149073734-b64ad276-3dbc-451c-9a63-ab1b031ed314.png)
 ![download (1)](https://user-images.githubusercontent.com/44817812/149073838-e21062fe-3941-4708-888c-2885bf3d57fe.png)
 ![download (1)](https://user-images.githubusercontent.com/44817812/149073924-29b1fe4e-c756-4397-9dfa-7f677faf11a8.jpeg)
 ![download (2)](https://user-images.githubusercontent.com/44817812/149074045-2ead8904-1bb9-49c9-b0f1-6a04b18aa34f.jpeg)
 ![download (2)](https://user-images.githubusercontent.com/44817812/149074164-82c2abc3-9cbf-4ada-9d08-864a26fe5ac9.png)
