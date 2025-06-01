import boto3
import json
def read_s3_object(bucket_name, file_name):
    s3 = boto3.resource("s3")
    file_object = s3.Object(bucket_name, file_name)
    contents=file_object.get()['Body'].read().decode('utf-8')
    json_data=json.loads(contents)
    return json_data

def upload_s3_object():
    pass

def delete_s3_object():
    pass

def delete_s3_bucket():
    pass


