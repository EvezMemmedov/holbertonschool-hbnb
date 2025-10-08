```mermaid
sequenceDiagram
    participant User
    participant API
    participant UserModel as Business Logic (User Model)
    participant DB as Database

    User->>API: POST /api/v1/users (user data)
    API->>API: Validate input (email, password, etc.)
    API->>UserModel: Create new User instance
    UserModel->>DB: INSERT new user into users table
    DB-->>UserModel: Return success (user_id)
    UserModel-->>API: Return created user object
    API-->>User: 201 Created (user info JSON)
