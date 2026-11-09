import os

# Define the directory where you have saved the filings
download_directory = "sec-edgar-filings"

# Function to process a single file
def process_10k_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        
        # Find the start of the actual content, after the <SEC-DOCUMENT> tag
        start_idx = content.find('<SEC-DOCUMENT>')
        if start_idx != -1:
            # Cut off everything before the <SEC-DOCUMENT> tag
            content = content[start_idx:]
            # Now you can further process 'content' as needed
            return content
        else:
            return "No <SEC-DOCUMENT> tag found."

# Loop through the downloaded files and process them
for root, dirs, files in os.walk(download_directory):
    for file in files:
        if file.endswith('.txt'):  # Adjust the extension if necessary
            file_path = os.path.join(root, file)
            print(f"Processing file: {file_path}")
            text_content = process_10k_file(file_path)
            # Here you can decide what to do with the text_content
            # For example, you could print it, save it to a file, or pass it to another function for further processing
            # For demonstration, we'll just print the first 500 characters of the content after the <SEC-DOCUMENT> tag
            print(text_content[:500])
