#!/bin/bash

# Name of the Docker container
CONTAINER_NAME="my-container"

# Check if the container is already running
if docker ps -f name=$CONTAINER_NAME | grep -q $CONTAINER_NAME; then
	echo "Container is already running."
else
	echo "Container is not running. Starting..."
	docker start $CONTAINER_NAME
	if [ $? -eq 0 ]; then
    	echo "Container started successfully."
	else
    	echo "Failed to start the container."
	fi
fi


