#!/bin/bash

# Define AWS EC2 instance details
aws_region="eu-east-1"
instance_type="t3.micro"
ami_id="ami-09a9858973b288bdd"  # Ubuntu 22.04 AMI ID
key_name="dockerlab7"
key_path="~/Downloads/dockerlab7.pem"

# Define Docker container details
docker_image="ubuntu:latest"
docker_command="docker run -it --rm $docker_image /bin/bash"

# Function to launch an EC2 instance
launch_instance() {
    echo "Launching EC2 instance..."
    
    # Use AWS CLI to launch the EC2 instance
    instance_id=$(aws ec2 run-instances \
        --region "$aws_region" \
        --instance-type "$instance_type" \
        --image-id "$ami_id" \
        --key-name "$key_name" \
        --query "Instances[0].InstanceId" \
        --output text)

    if [[ -z "$instance_id" ]]; then
        echo "Failed to launch EC2 instance."
        exit 1
    fi

    echo "Waiting for the instance to start..."
    aws ec2 wait instance-running --instance-ids "$instance_id" --region "$aws_region"
    
    # Get the public DNS
    public_dns=$(aws ec2 describe-instances \
        --region "$aws_region" \
        --instance-ids "$instance_id" \
        --query "Reservations[0].Instances[0].PublicDnsName" \
        --output text)

    if [[ -z "$public_dns" ]]; then
        echo "Failed to retrieve the public DNS of the instance."
        exit 1
    fi

    echo "Instance launched successfully!"
    echo "Instance ID: $instance_id"
    echo "Public DNS: $public_dns"

    # Store public DNS for later use
    echo "$public_dns" > ec2_public_dns.txt
}

# Function to SSH into the EC2 instance and run Docker container
ssh_and_run_docker() {
    echo "Waiting for SSH access..."
    sleep 60  # Ensure the instance is ready for SSH

    # Get the public DNS of the EC2 instance
    public_dns=$(cat ec2_public_dns.txt)

    if [[ -z "$public_dns" ]]; then
        echo "Could not retrieve public DNS. Exiting."
        exit 1
    fi

    echo "Connecting to EC2 instance via SSH..."
    
    # SSH into the instance and run the Docker container
    ssh -o StrictHostKeyChecking=no -i "$key_path" ubuntu@"$public_dns" << EOF
        sudo apt update -y
        sudo apt install -y docker.io
        sudo systemctl start docker
        sudo usermod -aG docker ubuntu
        newgrp docker
        $docker_command
EOF
}

# Main script workflow
main() {
    launch_instance
    ssh_and_run_docker
}

# Call the main function
main

