# import requests
# import os
# from dotenv import load_dotenv, find_dotenv

# # This will search for the .env file in the current directory and parent directories
# load_dotenv(find_dotenv())

# # Check if the API key is being loaded correctly
# api_key = os.getenv('RUNWAY_API_KEY')
# if not api_key:
#     raise ValueError("API key not found in environment variables. Please check your .env file.")

# headers = {"Authorization": f"Bearer {api_key}"}
# response = requests.get("https://api.runwayml.com/v1/models", headers=headers)

# # Print the status code and response from the API
# print(response.status_code, response.json())
import requests
import os
from dotenv import load_dotenv

# Specify the path to the .env file in the 'app/' folder
dotenv_path = os.path.join(os.getcwd(), 'app', '.env')

# Load the .env file from the specified path
load_dotenv(dotenv_path)

# Get the API key from the .env file
api_key = os.getenv('RUNWAY_API_KEY')
if not api_key:
    raise ValueError("API key not found in environment variables. Please check your .env file.")

# Set the API version header (you can check the API documentation for the specific version to use)
headers = {
    "Authorization": f"Bearer {api_key}",
    "X-Runway-Version": "1.0"  # Specify the version (replace with the correct version if needed)
}

# Make the API request
response = requests.get("https://api.dev.runwayml.com/v1/models", headers=headers)

# Check if the response is empty or has non-JSON content
if response.status_code == 200:
    try:
        print(response.status_code, response.json())  # Try parsing JSON
    except ValueError:
        print("Response is not in JSON format:", response.text)  # Print the raw response content
else:
    print(f"Error {response.status_code}: {response.text}")  # Handle non-200 status codes
