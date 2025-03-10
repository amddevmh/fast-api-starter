#!/usr/bin/env python3
"""
Run the FastAPI application for testing
"""
import uvicorn

if __name__ == "__main__":
    uvicorn.run("app.application:app", host="127.0.0.1", port=8000, reload=True)
