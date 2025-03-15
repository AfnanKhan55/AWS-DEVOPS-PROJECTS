#!/bin/bash

# Task 1: Accept an image name as input
read -p "Enter the name of the Docker image: " image_name

# Task 2: Pull and run the Docker image
echo "Pulling the Docker image: $image_name"
docker pull $image_name

echo "Running the Docker container based on $image_name"
docker run -it --rm $image_name

