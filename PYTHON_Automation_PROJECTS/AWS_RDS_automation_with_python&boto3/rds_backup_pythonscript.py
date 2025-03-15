import boto3

rds_client = boto3.client('rds')

backup_name = 'dbBackup'
db_instance_name = 'database'

try:
    response = rds_client.create_db_snapshot(
        DBSnapshotIdentifier=backup_name,
        DBInstanceIdentifier=db_instance_name
    )

    if 'DBSnapshot' in response:
        print(f"Manual backup '{backup_name}' created successfully.")
    else:
        print("Error creating manual backup:", response)

except Exception as e:
    print(f"An error occurred: {e}")

