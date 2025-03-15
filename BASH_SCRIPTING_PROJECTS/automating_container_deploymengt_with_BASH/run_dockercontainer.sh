#!/bin/bash

# Task 1: Pull Nginx Docker image
echo "Task 1: Pulling Nginx Docker image"
docker pull nginx

# Check if image pull was successful
if [ $? -eq 0 ]; then
	echo "Image pull successful: Nginx Docker image"
else
	echo "Image pull failed: Nginx Docker image"
	exit 1
fi

# Task 2: Run Docker container
echo "Task 2: Running Docker container"
docker run -d -p 8080:80 --name nginx-container nginx

# Check if container is running
if docker ps | grep -q nginx-container; then
	echo "Nginx container is running and accessible at http://localhost:8080"
else
	echo "Failed to start Nginx container."
	exit 1
fi

# End of script
echo "Lab 2 tasks completed."



