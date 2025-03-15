AWS EC2 Terraform Deployment

This Terraform configuration deploys two EC2 instances in AWS with specific provisioning:

child-1: Installs Docker and adds the ubuntu user to the Docker group.

child-2: Installs Nginx.

Prerequisites

Before running this Terraform script, ensure you have:

AWS CLI installed and configured.

Terraform installed.

A valid AWS access key and secret key.

An existing key pair named selenium.

A security group (sg-05a251e19c0285bb4) that allows SSH and necessary traffic.

Usage

1. Initialize Terraform

Run the following command to initialize the Terraform working directory:

terraform init

2. Plan the Deployment

Run to see the changes Terraform will make:

terraform plan

3. Apply the Deployment

Deploy the resources by running:

terraform apply -auto-approve

4. Retrieve Public IPs

After deployment, Terraform will output the public IPs of the instances:

terraform output

5. Access the Instances

Use SSH to connect to the instances:

ssh -i /home/ubuntu/selenium.pem ubuntu@<child_1_public_ip>
ssh -i /home/ubuntu/selenium.pem ubuntu@<child_2_public_ip>

Resources Created

2 EC2 Instances

child-1: Runs Docker.

child-2: Runs Nginx.

Security Group (existing): sg-05a251e19c0285bb4.

Key Pair (existing): selenium.

Cleanup

To destroy the created resources:

terraform destroy -auto-approve

Notes

Modify the AMI ID (ami-04b4f1a9cf54c11d0) based on your region.

Ensure your security group allows inbound SSH (port 22) and HTTP (port 80) if needed.


