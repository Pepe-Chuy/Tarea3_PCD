# Tarea3_PCD
Assignment on api use# FastAPI User Management API

This is a simple User Management API built with FastAPI, SQLAlchemy, and Pydantic. The API allows you to create, read, update, and delete user data stored in a database.

## Requirements

- Python 3.8+
- FastAPI
- SQLAlchemy
- Pydantic
- Uvicorn

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-repo/fastapi-user-management.git
    cd fastapi-user-management
    ```

2. Install the required dependencies:

    ```bash
    pip install fastapi uvicorn sqlalchemy pydantic
    ```

3. Set up the database by creating the required tables:

    The `models.Base.metadata.create_all(bind=engine)` line in the code will automatically create the necessary tables when the application is started.

## Running the Application

To start the FastAPI application, run the following command:

```bash
uvicorn main:app --port 4444 --reload
