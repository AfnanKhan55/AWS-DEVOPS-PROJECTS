#!/bin/bash

# Task 1: List all Docker images
echo "Listing all Docker images:"
docker images

# Task 2: Remove each image interactively using a loop
echo "Do you want to remove the Docker images? (yes/no)"
read confirmation

if [ "$confirmation" == "yes" ]; then
    # Loop through the images and remove them one by one
    echo "Removing Docker images..."
    for image_id in $(docker images -q); do
        echo "Removing image $image_id"
        docker rmi $image_id
    done
    echo "All Docker images have been removed."
else
    echo "No Docker images have been removed."
fi

