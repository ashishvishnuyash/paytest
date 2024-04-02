# Expense Tracker API

## Overview

Expense Tracker API is a Python web application built using the BlackSheep framework. It provides various API endpoints for user registration, login, transactions, and account management. The application uses SQLAlchemy and Pydantic models for data validation and database interactions.

## Features

- User registration and login
- Token-based authentication
- User details retrieval
- Money transfer (send, receive)
- Transaction history
- Funds withdrawal and deposit
- Setting user address and ID proof



## API Endpoints

### Register a New User

- **URL:** `/register`
- **Method:** POST
- **Request Body:**

    ```json
    {
        "first_name": "John",
        "last_name": "Doe",
        "phone": "1234567890",
        "email": "johndoe@example.com",
        "group_id": 1,
        "password": "password123",
        "status_id": 1
    }
    ```

### User Login

- **URL:** `/login`
- **Method:** POST
- **Request Body:**

    ```json
    {
        "email": "johndoe@example.com",
        "password": "password123"
    }
    ```

### Get User Details

- **URL:** `/userdetail`
- **Method:** GET

### Send Money

- **URL:** `/send`
- **Method:** POST
- **Request Body:**

    ```json
    {
        "reciver_email": "janedoe@example.com",
        "amount": 100,
        "total": 105,
        "currency": "USD"
    }
    ```

### Receive Money

- **URL:** `/receive`
- **Method:** POST
- **Request Body:**

    ```json
    {
        "reciver_email": "johndoe@example.com",
        "amount": 100,
        "total": 100,
        "currency": "USD"
    }
    ```

### Transactions History

- **URL:** `/transactions`
- **Method:** GET

### Withdraw Funds

- **URL:** `/withdraw`
- **Method:** POST
- **Request Body:**

    ```json
    {
        "amount": 50,
        "total": 50,
        "currency": "USD"
    }
    ```

### Deposit Funds

- **URL:** `/deposit`
- **Method:** POST
- **Request Body:**

    ```json
    {
        "amount": 50,
        "total": 50,
        "currency": "USD"
    }
    ```

### Set User Address

- **URL:** `/set_address`
- **Method:** POST
- **Request Body:**

    ```json
    {
        "address": "123 Main St",
        "state": "CA",
        "city": "Los Angeles",
        "postal_code": "90001",
        "nationality": "US"
    }
    ```

### Set User ID Proof

- **URL:** `/set_id`
- **Method:** POST
- **Request Body:**

    ```json
    {
        "id_no": "1234567890",
        "id_type": "Passport",
        "id_expiry": "2025-12-31",
        "id_upload": "base64_encoded_image"
    }
    ```

