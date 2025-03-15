#!/bin/bash

# Exit on any error
set -e

# Step 1: Create a simple static website
echo "Creating a simple static website..."
mkdir -p website
cat <<EOF > website/index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Afnan Khan Project</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            color: #333;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .container {
            text-align: center;
            background: #ffffff;
            padding: 20px 40px;
            border-radius: 10px;
            box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #007bff;
        }
        p {
            font-size: 1.2em;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Welcome to Afnan Khan Project!</h1>
        <p>We have successfully created a containerized and scalable website deployment using Docker and Kubernetes.</p>
    </div>
</body>
</html>
EOF

# Step 2: Create a Dockerfile
echo "Writing Dockerfile..."
cat <<EOF > website/Dockerfile
# Use Nginx to serve the website
FROM nginx:alpine
COPY ./ /usr/share/nginx/html
EXPOSE 80
EOF

# Step 3: Build the Docker image
echo "Building Docker image..."
docker build -t simple-website:v1 ./website

# Step 4: Create a kind cluster
echo "Creating a kind cluster..."
kind create cluster --name demo-cluster

# Step 5: Load the Docker image into the kind cluster
echo "Loading Docker image into kind cluster..."
kind load docker-image simple-website:v1 --name demo-cluster

# Step 6: Create Kubernetes manifests
echo "Writing Kubernetes manifests..."

# Deployment manifest
echo "Creating deployment manifest..."
cat <<EOF > deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: simple-website
spec:
  replicas: 2
  selector:
    matchLabels:
      app: simple-website
  template:
    metadata:
      labels:
        app: simple-website
    spec:
      containers:
      - name: website-container
        image: simple-website:v1
        ports:
        - containerPort: 80
EOF

# Service manifest
echo "Creating service manifest..."
cat <<EOF > service.yaml
apiVersion: v1
kind: Service
metadata:
  name: simple-website-service
spec:
  selector:
    app: simple-website
  ports:
      - protocol: TCP
        port: 80
        targetPort: 80
EOF

# Step 7: Apply Kubernetes manifests
echo "Applying Kubernetes manifests..."
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

# Step 8: Port forwarding to access the service
echo "Setting up port forwarding..."
kubectl port-forward service/simple-website-service 8080:80 &

# Step 9: Display the access URL
echo "Deployment complete! Access your website at http://localhost:8080"

