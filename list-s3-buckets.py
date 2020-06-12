#!/usr/bin/python3

import boto3

my_aws_console = boto3.session.Session()
my_s3 = my_aws_console.resource('s3')

for i in my_s3.buckets.all():
    print(i.name)
