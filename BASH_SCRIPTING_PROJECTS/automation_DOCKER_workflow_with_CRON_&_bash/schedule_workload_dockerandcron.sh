#!/bin/bash

# Define variables
backup_directory="/backup_data"
docker_container_name="my_backup_container"
backup_tool_image="backup_tool:latest"

# Function to perform a backup using Dockerized backup tool
perform_backup() {
    # Create a backup directory if it doesn't exist
    mkdir -p "$backup_directory"

    # Run the Docker container to perform the backup
    docker run --rm -v "$backup_directory:/backup" "$backup_tool_image"
}

# Main script workflow
main() {
    echo "Starting periodic backup..."
    
    # Perform the backup
    perform_backup

    echo "Backup completed."
}

# Call the main function to start the script
main

