#!/bin/bash

# Function to run a Docker container (simulating an error)
run_container() {
    local container_name="$1"
    echo "Attempting to run Docker container: $container_name"
    
    # Try to run the Docker container (intentionally providing a non-existent image)
    docker run -it --rm "$container_name"
    
    # Check the exit status of the previous command
    if [ $? -ne 0 ]; then
        echo "Error: Docker container '$container_name' does not exist."
    fi
}

# Main script workflow
main() {
    container_name="non_existent_container:tag"
    
    # Run the Docker container and handle errors
    run_container "$container_name"
}

# Call the main function to start the script
main

