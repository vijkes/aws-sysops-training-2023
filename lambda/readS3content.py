import json
import boto3

def lambda_handler(event, context):
    s3 = boto3.client("s3")
    print(event)
    if event:
        file_obj = event["Records"][0]
        bucket_name = str(file_obj["s3"]["bucket"]["name"])
        filename = str(file_obj["s3"]["object"]["key"])
        print(f"Filename : {filename}")
        
        file_object = s3.get_object(Bucket=bucket_name, Key=filename)
        file_content = file_object["Body"].read().decode("utf-8")
        print(file_content)
    #print(event)        
    return {
        'statusCode': 200,
        'body': json.dumps('dfaldsfasldk')
        
    }
