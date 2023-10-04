# basic_etl
This is a basic ETL that extracts information from an API with synthetic data using Docker and PostgreSQL.


## Gen_Data API

The Gen_Data API is a web application built using the FastAPI framework, providing an interface for efficient and scalable access and management of genetic data. This API is ideal for projects that require storing and retrieving genetic sequences, annotations, and other genetics-related data.

## Running with Docker Compose

You can run the Gen_Data API easily using Docker Compose. Make sure you have Docker and Docker Compose installed on your system. Follow these steps:

1. Clone this repository to your local machine.

```
git clone https://github.com/bkoscar/basic_etl.git
```

2. Navigate to the repository directory.
```
cd Gen_Data
```
3. Build the Docker image and run the application with Docker Compose.
```
docker-compose up --build
```
This will create and run a Docker container hosting the Gen_Data API and make it accessible in your web browser.

## Usage

Once the API is up and running, you can access the user interface through your web browser at http://0.0.0.0:8000  where PORT is the port number the API is running on (typically, port 80 by default).

Use the user interface or make HTTP requests to interact with the API and manage genetic data according to your needs.

