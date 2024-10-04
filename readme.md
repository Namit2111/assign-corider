

[StartOfDocument readme.md]
# Project Overview

This project is a web application built using Flask, a popular Python web framework. The application is configured to run in a Docker container, with a MongoDB database for data storage.

## Application Structure

The application is organized into the following directories and files:

* `app.py`: The main application file, which runs the Flask app.
* `app` : Folder containing all routes
* `db`: The directory containing the MongoDB database configuration and data.
* `config`: The directory containing the application configuration files.
* `utils`: The directory containing utility functions used throughout the application.

## Setup and Installation

To set up and run the application, follow these steps:

1. Clone the repository to your local machine.
2. Create a new directory for the project and navigate into it.
3. Run `docker-compose up --build` to build and start the application containers.
4. Attach debugger 
5. Access the application at `http://localhost:5000` in your web browser.

## Configuration

The application configuration is stored in the `config` directory. The main configuration file is `config.py`, which defines the application settings and database connections.

## Database

The application uses a MongoDB database for data storage. The database configuration is stored in the `db` directory. The `docker-compose.yml` file defines the MongoDB service and its dependencies.

## Utilities

The `utils` directory contains utility functions used throughout the application. These functions are used for tasks such as data processing and validation.

