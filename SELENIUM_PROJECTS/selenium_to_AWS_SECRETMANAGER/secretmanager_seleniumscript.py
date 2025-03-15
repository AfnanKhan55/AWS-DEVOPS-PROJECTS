import boto3

def store_secret(secret_name, secret_data):
	client = boto3.client('secretsmanager')
	response = client.create_secret(
    	Name=secret_name,
    	SecretString=secret_data
	)
	print("Secret created successfully!")

secret_name = "test/selenium/credentials"
secret_data = '{"username": "admin", "password": "admin123"}'
store_secret(secret_name, secret_data)



