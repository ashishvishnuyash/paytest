

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

### Global Fees Management

- **URL:** `/globle_fees`
- **Method:** POST
- **Request Body:**

    ```json
    {
        "setup_fee": 50,
        "transfer_fee": 10,
        "withdraw_fee": 5,
        "credit_mdr_percentage": 2,
        "credit_min_fee": 1,
        "debit_mdr_percentage": 1.5,
        "debit_min_fee": 0.5
    }
    ```

### User-Specific Fees Management

- **URL:** `/userfees`
- **Method:** POST
- **Request Body:**

    ```json
    {
        "user": 1,
        "setup_fee": 50,
        "transfer_fee": 10,
        "withdraw_fee": 5,
        "credit_mdr_percentage": 2,
        "credit_min_fee": 1,
        "debit_mdr_percentage": 1.5,
        "debit_min_fee": 0.5
    }
    ```

