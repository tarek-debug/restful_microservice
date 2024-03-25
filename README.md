# Restful Microservice

## Overview

This project provides a web application backend, implementing a RESTful API with Flask. It's designed to run in a Docker container, ensuring easy setup and deployment. Additionally, it includes configuration for deployment on Kubernetes, making it scalable and suitable for production environments. The application manages diary entries, showcasing CRUD operations.

## Features

- **Flask RESTful API**: Utilize Flask to create and manage diary entries through a RESTful API.
- **Docker Support**: Package the application in a Docker container for ease of deployment.
- **Kubernetes Deployment**: Includes configuration files for deploying the application on a Kubernetes cluster, ensuring scalability and high availability.
- **Dependency Management**: Predefined list of Python dependencies for consistent environments.

## Getting Started

### Prerequisites

- Docker
- Kubernetes cluster (e.g., Minikube, AKS, EKS, GKE)
- Python 3.x

### Installation

1. Clone the repository:

```bash

git clone https://github.com/tarek-debug/restful\_microservice.git

cd restful\_microservice

```

1. Build the Docker image:
Replace [docker account] with your docker account username
```bash

docker build -t restful_microservice:v0.0.1 .
docker tag restful_microservice:v0.0.1 [docker account]/restful_microservice:v0.0.1
docker push [docker account]/restful_microservice:v0.0.1

```

### Running the Application

#### Docker

1. Run the Docker container:

```bash

docker run -d -p 5000:5000 restful_microservice:v0.0.1

```

1. Access the API at `http://localhost:5000`.

#### Kubernetes

1. Apply the Kubernetes configurations:

```bash

kubectl apply -f deployment.yaml, service.yaml, configmap.yaml

```

1. Find the external IP of the service:

```bash

kubectl get services

```

Note: It might take a few minutes for the external IP to be available.

1. Access the API at `http://<external-ip>:82`.

## API Usage

- `GET /diary/`: List all diary entries.
- `POST /diary/`: Create a new diary entry. Requires a JSON payload with `title` and `content`.
- `GET /diary/<title>`: Retrieve a specific diary entry by title.
- `PUT /diary/<title>`: Update an existing diary entry by title. Requires a JSON payload with updated `title` and/or `content`.
- `DELETE /diary/<title>`: Delete a diary entry by title.

## Kubernetes Configuration

The application is configured to run on Kubernetes with the following specifications:

- **Deployment (`deployment.yaml`)**: Creates a deployment with 3 replicas of the application, ensuring high availability. The application image is `tarek111778/restful\_microservice:v0.0.1`, listening on port 5010.
- **Service (`service.yaml`)**: Exposes the application outside the Kubernetes cluster using a LoadBalancer service on port 82, targeting port 5010 on the application containers.

## Contributors

- Tarek Solamy (Alsolame)

