#import boto3
#import json
from aws_utils.s3_ops import read_s3_object

json_data1 = read_s3_object('aws-project-bucket-rachit','first-json-file.json')
print(json_data1['info']['name'])
