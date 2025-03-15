#!/bin/bash

# Function to pull a Docker image
pull_image() {
    local image_name="$1"
    echo "Pulling the Docker image: $image_name"
    docker pull "$image_name"
}

# Function to run a Docker container
run_container() {
    local image_name="$1"
    echo "Running the Docker container based on: $image_name"
    docker run -it --rm -name "$image_name" "$image_name"
}

# Function to stop a Docker container
stop_container() {
    local container_name="$1"
    echo "Stopping the Docker container: $container_name"
    docker stop "$container_name"
}

# Main script workflow
main() {
    read -p "Enter the name of the Docker image to pull and run: " image_name

    # Pull the Docker image
    pull_image "$image_name"

    # Run the Docker container
    run_container "$image_name"

    # Ask if the user wants to stop the container
    read -p "Do you want to stop the container? (yes/no): " stop_choice
    if [ "$stop_choice" == "yes" ]; then
        # Stop the Docker container
        stop_container "$image_name"
    else
        echo "Container is still running. You can manually stop it later."
    fi
}

# Call the main function to start the script
main

