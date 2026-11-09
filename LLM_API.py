import os
import requests

# Your Hugging Face API token
api_token = os.environ["HF_API_TOKEN"]

# The headers to provide to authenticate our request
headers = {
    "Authorization": f"Bearer {api_token}"
}

# The API URL for a model, replace `MODEL_NAME` with the actual model name you want to use
api_url = "https://api-inference.huggingface.co/models/distilgpt2"

# The payload with the prompt you want to send to the model
payload = {
    "inputs": "The quick brown fox jumps over the lazy dog",
}

# Make a POST request to the Hugging Face API
response = requests.post(api_url, headers=headers, json=payload)

# Check if the request was successful
if response.status_code == 200:
    # Print the generated text
    print(response.json())
else:
    # Print the error
    print(f"Failed to generate text: {response.status_code}, {response.text}")