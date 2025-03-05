# Project Structure

This FastAPI starter template follows a modular and organized structure to promote maintainability and scalability.

## Directory Structure

```
fast-api-starter/
├── app/                      # Main application package
│   ├── api/                  # API routes and endpoints
│   │   ├── __init__.py
│   │   └── routes.py         # API route definitions
│   ├── auth/                 # Authentication components
│   │   ├── __init__.py
│   │   ├── middleware.py     # Auth middleware
│   │   ├── routes.py         # Auth endpoints
│   │   └── security.py       # JWT and security utilities
│   ├── database/             # Database connection and utilities
│   │   ├── __init__.py
│   │   └── mongodb.py        # MongoDB connection
│   ├── models/               # Data models
│   │   ├── __init__.py
│   │   ├── message.py        # Message models
│   │   ├── nutrition.py      # Nutrition models
│   │   └── user.py           # User models
│   ├── services/             # Business logic services
│   │   ├── __init__.py
│   │   ├── message_service.py # Message processing service
│   │   ├── nutrition_service.py # Nutrition service
│   │   └── user_service.py   # User management service
│   ├── __init__.py
│   ├── application.py        # FastAPI application setup
│   ├── config.py             # Configuration settings
│   ├── main.py               # Application entry point
│   ├── .env                  # Environment variables (not in version control)
│   └── .env.example          # Example environment variables
├── tests/                    # Test files
│   ├── __init__.py
│   ├── test_user_auth.py     # Authentication tests
│   ├── test_message_service.py # Service tests
│   └── test_message_integration.py # Integration tests
├── .gitignore                # Git ignore file
├── Makefile                  # Makefile for common commands
├── README.md                 # Project documentation
├── DEV_AUTH.md               # Authentication documentation
├── TESTING.md                # Testing documentation
├── requirements.txt          # Python dependencies
├── run_app.py                # Script to run the application
└── generate_dev_token.py     # Utility to generate dev tokens
```

## Key Components

### API Layer
- Routes and endpoints for the application
- Request/response handling
- Input validation

### Authentication
- JWT-based authentication
- User registration and verification
- Development token for testing

### Database
- MongoDB connection using Beanie ODM
- Document models and schemas
- Database initialization

### Models
- Pydantic models for data validation
- MongoDB document models
- Request/response schemas

### Services
- Business logic implementation
- Data processing
- External integrations

## Design Principles

This template follows these design principles:

1. **Separation of Concerns**: Each module has a specific responsibility
2. **Dependency Injection**: Services and dependencies are injected where needed
3. **Environment-Aware Configuration**: Different settings for development and production
4. **Testability**: Code is structured to be easily testable
5. **Security**: Authentication and authorization built-in
6. **Documentation**: Comprehensive documentation for all components
