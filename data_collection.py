import pandas as pd
# import json
import json
import boto3
# store the URL in url 

s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket ='aws-simplified-transactions420'
    url = 'https://house-stock-watcher-data.s3-us-west-2.amazonaws.com/data/all_transactions.json'
    df = pd.read_json(url)
    f = pd.DataFrame(df)
    
    fileName = 'data' + '.csv'
    
    s3.put_object(Bucket=bucket, Key=fileName, Body=f.to_csv())
    print('Put Complete') 