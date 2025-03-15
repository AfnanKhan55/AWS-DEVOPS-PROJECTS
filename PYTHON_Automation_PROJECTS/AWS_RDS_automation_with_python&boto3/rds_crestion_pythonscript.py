import boto3

rds_client = boto3.client('rds', region_name='your-region')

db_instance_name = 'rds'
db_instance_class = 'db.t2.micro'
engine = 'mysql'
master_username = 'Huzaifa_Tanveer'
master_password = 'iamtheone1122!'

response = rds_client.create_db_instance(
    DBInstanceIdentifier=db_instance_name,
    DBInstanceClass=db_instance_class,
    Engine=engine,
    MasterUsername=master_username,
    MasterUserPassword=master_password,
    AllocatedStorage=20, 
    MultiAZ=False 
   
)

if 'DBInstance' in response:
    print(f"RDS instance '{db_instance_name}' created successfully.")
else:
    print("Error creating RDS instance:", response)


