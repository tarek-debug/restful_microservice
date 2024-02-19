
# Project Title

## Overview
This project provides a web application backend, implementing a RESTful API with Flask. It's designed to run in a Docker container, ensuring easy setup and deployment. The application manages diary entries, showcasing CRUD operations.

## Features
- **Flask RESTful API**: Utilize Flask to create and manage diary entries through a RESTful API.
- **Docker Support**: Package the application in a Docker container for ease of deployment.
- **Dependency Management**: Predefined list of Python dependencies for consistent environments.

## Getting Started

### Prerequisites
- Docker
- Python 3.x

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/tarek-debug/restful_microservice.git
   cd restful_microservice
   ```
2. Build the Docker image:
   ```bash
   docker build -t restful_microservice .
   ```

### Running the Application
1. Run the Docker container:
   ```bash
   docker run -d -p 5000:5000 restful_microservice
   ```
2. Access the API at `http://localhost:5000`.

## API Usage
- **Create a Diary Entry**: `POST /diary`
- **Read Diary Entries**: `GET /diary`
- **Update a Diary Entry**: `PUT /diary/<id>`
- **Delete a Diary Entry**: `DELETE /diary/<id>`


## Contributors
- Tarek Solamy (Alsolame)
