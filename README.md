# FastAPI Starter Template

A production-ready FastAPI starter template with MongoDB integration, JWT authentication, comprehensive testing infrastructure, and environment configuration.

## Complete Setup Guide (From Step 0)

### Prerequisites

- Python 3.8+ installed on your system
- MongoDB installed and running (version 4.4+ recommended)
- Basic knowledge of terminal/command line

### Step 1: Clone the Repository

```bash
git clone https://github.com/amddevmh/fast-api-starter.git
cd fast-api-starter
```

### Step 2: Set Up Python Virtual Environment

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
# Upgrade pip to the latest version
pip install --upgrade pip

# Install required packages
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables

```bash
# Create a .env file based on the .env.example template
cp .env.example .env
# Edit it if you need to change any settings
```

The `.env` file will contain:
```
# API Configuration
API_HOST=0.0.0.0
API_PORT=8000

# MongoDB Atlas Configuration
MONGODB_URI=mongodb+srv://moualhiahmed:<db_password>@cluster0.eqd2a.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
MONGODB_PASSWORD=your_actual_password
DATABASE_NAME=nutrition_assistant
```

### Step 5: Set Up MongoDB Atlas

This application uses MongoDB Atlas, a fully-managed cloud database service. You don't need to install MongoDB locally.

1. Make sure you have access to the MongoDB Atlas cluster at:
   ```
   mongodb+srv://moualhiahmed:<password>@cluster0.eqd2a.mongodb.net/
   ```

2. Run the setup script to create your .env file with the MongoDB Atlas connection details:
   ```bash
   python setup_env.py
   ```

3. When prompted, enter your MongoDB Atlas password.

Alternatively, you can manually create a .env file based on the .env.example template and replace the placeholder password with your actual MongoDB Atlas password.

### Step 6: Seed the Database (Optional)

To populate the database with sample nutrition data:

```bash
# Make sure you're in the backend directory with activated virtual environment
python seed_db.py
```

You should see output indicating that sample nutrition profiles, food items, meals, and trackers have been created.

### Step 7: Run the Server

```bash
# Make sure you're in the backend directory with activated virtual environment
python run.py
```

The server will start on port 8000 by default (configurable in .env file).
You should see output similar to:
```
Database initialized successfully!
INFO:     Will watch for changes in these directories: ['/path/to/chatbot-template/backend']
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [xxxxx] using StatReload
INFO:     Started server process [xxxxx]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

### Step 8: Verify the Server is Running

Open your browser and navigate to:
```
http://localhost:8000/health
```

Or use curl from the terminal:
```bash
curl http://localhost:8000/health
```

You should see a response like:
```json
{"status":"healthy","message":"API is running"}
```

## API Endpoints

### Health
- `GET /health` - Health check endpoint

### Authentication
- `POST /api/v1/auth/test-token` - Get a test token for development
- `GET /api/v1/auth/me` - Get current user information

### Nutrition
- `POST /api/chat/message` - Process chat messages
- `POST /api/nutrition/extract` - Extract nutrition information from user messages
- `POST /api/nutrition/confirm/{nutrition_id}` - Confirm extracted nutrition information
- `POST /api/nutrition/reject/{nutrition_id}` - Reject extracted nutrition information

## Project Structure

This template follows a modular and organized structure to promote maintainability and scalability. For a detailed overview of the project structure, see the [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) file.

### Key Components

- **API Layer**: Routes and endpoints
- **Authentication**: JWT-based authentication system
- **Database**: MongoDB connection using Beanie ODM
- **Models**: Pydantic models for data validation
- **Services**: Business logic implementation

## Testing the API

This template includes a comprehensive testing infrastructure with a Makefile for easy test execution.

### Using the Makefile

```bash
# Run all tests
make test

# Run only authentication tests
make test-auth

# Run only message service tests
make test-message-service

# Run only integration tests
make test-integration

# Run the application
make run

# Clean generated files
make clean
```

### Using curl for API testing

```bash
# Test the health endpoint
curl http://localhost:8000/health

# Test the authentication endpoint
curl -X POST http://localhost:8000/api/v1/auth/test-token
```

## Documentation

Once the server is running, you can access the interactive API documentation at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Troubleshooting

### Common Issues

1. **Port already in use**
   - Change the port in the `.env` file
   - Check if another process is using port 8000

2. **Package installation errors**
   - Try updating pip: `pip install --upgrade pip`
   - Make sure you're using a compatible Python version

3. **Environment activation issues**
   - Ensure you've activated the virtual environment before running commands
   - The terminal prompt should show `(venv)` when activated

4. **MongoDB Atlas connection issues**
   - Verify your MongoDB Atlas password is correct in the `.env` file
   - Check your network connection and make sure you can access MongoDB Atlas
   - Verify that your IP address is whitelisted in the MongoDB Atlas network access settings
   - Check if there are any MongoDB Atlas service outages

## Development

The server uses hot-reloading, so any changes you make to the code will automatically restart the server.

## Authentication System

This template includes a robust JWT-based authentication system with the following features:

- JWT token generation and validation
- User registration and verification
- Development token for testing
- Environment-aware configuration
- Middleware for protected routes

For more details, see the [DEV_AUTH.md](DEV_AUTH.md) file.

The application includes a robust user authentication and verification system:

### User Model

The `User` model includes:
- Username and email for identification
- Hashed password for secure authentication
- Verification status to ensure email verification
- Active status to control account access

### Authentication Flow

1. **Development Mode**: 
   - Use the `/api/v1/auth/test-token` endpoint with the `test_secret_key` header to get a test token
   - This is only available in non-production environments

2. **Token Verification**:
   - All API requests are verified using JWT tokens
   - Tokens include the username as the subject
   - Tokens expire after 30 minutes by default

3. **User Verification**:
   - Users must be verified before accessing protected resources
   - Verification is handled through a token-based email verification system
   - Unverified users cannot access nutrition data

### Security Features

- Password hashing using bcrypt
- JWT token-based authentication
- Email verification
- Active/inactive user status
- Role-based access control

### User Service

The `UserService` provides methods for:
- User registration
- Email verification
- Authentication
- Profile management
