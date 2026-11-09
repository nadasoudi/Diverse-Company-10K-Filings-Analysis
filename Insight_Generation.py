import requests

# Function to analyze text with Hugging Face API
def analyze_text_with_llm(text):
    api_token = "API token "  # Replace with your actual API token
    headers = {"Authorization": f"Bearer {api_token}"}
    api_url = "https://api-inference.huggingface.co/models/distilgpt2"  # Use the correct model name
    payload = {
        "inputs": text,
        "parameters": {
            "max_length": 500,  # Adjust this value based on the model's capabilities
        }
    }

    response = requests.post(api_url, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to generate text: {response.status_code}, {response.text}")

# Function to read the content of the file
def read_file_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Main function to process the file and analyze the text
def main():
    file_path = 'sec-edgar-filings/CAT/10-K/0000018230-01-500017/full-submission.txt'
    text_content = read_file_content(file_path)
    
    # Analyze the first 500 characters (or more, depending on your needs)
    insights = analyze_text_with_llm(text_content[:500])
    with open('output.txt', 'w') as file:
        file.write(insights[0]['generated_text'])
    # Print or process the insights here
    print(insights)

# Run the main function
if __name__ == "__main__":
    main()
