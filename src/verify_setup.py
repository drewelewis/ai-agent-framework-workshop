"""Verify your workshop environment is configured correctly."""

from dotenv import load_dotenv
import os
import sys

load_dotenv()

print("Checking your environment...\n")

errors = []

# Check PROJECT_ENDPOINT
endpoint = os.getenv("PROJECT_ENDPOINT")
if endpoint:
    print(f"  PROJECT_ENDPOINT: {endpoint}")
else:
    errors.append("PROJECT_ENDPOINT is not set in your .env file")

# Check MODEL_DEPLOYMENT_NAME
model = os.getenv("MODEL_DEPLOYMENT_NAME")
if model:
    print(f"  MODEL_DEPLOYMENT_NAME: {model}")
else:
    errors.append("MODEL_DEPLOYMENT_NAME is not set in your .env file")

print()

if errors:
    print("PROBLEMS FOUND:")
    for error in errors:
        print(f"  - {error}")
    print("\nFix your .env file and run this script again.")
    sys.exit(1)
else:
    print("Everything looks good! You're ready for the labs.")
