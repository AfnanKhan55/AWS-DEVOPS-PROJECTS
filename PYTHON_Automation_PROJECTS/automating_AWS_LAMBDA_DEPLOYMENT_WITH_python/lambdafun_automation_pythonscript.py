import boto3
import subprocess
import os
import time
import json

LAMBDA_FUNCTION_NAME = "MyLambdaFunction"
ZIP_FILE = "my_lambda_function.zip"
ROLE_NAME = "MyLambdaRole"
POLICY_ARN = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"

iam_client = boto3.client("iam")
lambda_client = boto3.client("lambda")

def check_lambda_file():
    if not os.path.exists("lambda_function.py"):
        print("Error: lambda_function.py not found. Creating a default function...")
        with open("lambda_function.py", "w") as f:
            f.write(
                """def lambda_handler(event, context):
return {'statusCode': 200, 'body': 'Hello, World!'}"""
            )

def create_zip():
    os.makedirs("my_lambda_package", exist_ok=True)
    subprocess.run(["cp", "lambda_function.py", "my_lambda_package/"])
    subprocess.run(["zip", "-r", ZIP_FILE, "."], cwd="my_lambda_package")

def create_role():
    try:
        response = iam_client.create_role(
            RoleName=ROLE_NAME,
            AssumeRolePolicyDocument=json.dumps({
                "Version": "2012-10-17",
                "Statement": [{
                    "Effect": "Allow",
                    "Principal": {"Service": "lambda.amazonaws.com"},
                    "Action": "sts:AssumeRole"
                }]
            })
        )
        iam_client.attach_role_policy(RoleName=ROLE_NAME, PolicyArn=POLICY_ARN)
        time.sleep(10)  # Wait for IAM role propagation
        return response["Role"]["Arn"]
    except iam_client.exceptions.EntityAlreadyExistsException:
        print("Role already exists. Retrieving existing role ARN...")
        response = iam_client.get_role(RoleName=ROLE_NAME)
        return response["Role"]["Arn"]
    except Exception as e:
        print(f"Error creating IAM role: {e}")
        exit(1)

def deploy_lambda():
    create_zip()
    role_arn = create_role()

    try:
        response = lambda_client.create_function(
            FunctionName=LAMBDA_FUNCTION_NAME,
            Runtime="python3.8",
            Role=role_arn,
            Handler="lambda_function.lambda_handler",
            Code={"ZipFile": open(f"my_lambda_package/{ZIP_FILE}", "rb").read()},
            Timeout=10,
            MemorySize=128
        )
        print(f"Lambda function {LAMBDA_FUNCTION_NAME} created successfully.")
    except lambda_client.exceptions.ResourceConflictException:
        print("Lambda function already exists. Updating function code...")
        lambda_client.update_function_code(
            FunctionName=LAMBDA_FUNCTION_NAME,
            ZipFile=open(f"my_lambda_package/{ZIP_FILE}", "rb").read()
        )
        print("Lambda function updated successfully.")

if __name__ == "__main__":
    check_lambda_file()
    deploy_lambda()
