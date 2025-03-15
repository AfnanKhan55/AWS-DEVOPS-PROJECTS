import boto3

region = "eu-north-1"  
bucket_name = "my-unique-bucket1"  


s3 = boto3.client("s3", region_name=region)

try:
    # When creating a bucket outside 'us-east-1', you must specify LocationConstraint
    s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={"LocationConstraint": region},
    )

    print(f"S3 Bucket '{bucket_name}' created successfully in {region}!")
except Exception as e:
    print(f"Error creating bucket: {e}")

