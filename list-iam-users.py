import boto3

my_aws_console = boto3.session.Session()
my_iam = my_aws_console.resource('iam')

for i in my_iam.users.all():
    print(i.name)

    