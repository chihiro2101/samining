import os
import requests
import base64


# Function to save README content to a text file
def save_readme_to_file(repo_name, readme_content):
    # Creating directory if not exists
    if not os.path.exists('readmefiles'):
        os.makedirs('readmefiles')


    # Writing content to file
    with open(f'readmefiles/{repo_name}_README.txt', 'wb') as file:
        file.write(readme_content)

def download_file_from_github(url, file_path, token):
    # Extracting repository owner and name from the URL
    parts = url.split('/')
    repo_owner = parts[-2]
    repo_name = parts[-1]

    # Making API request to get file content
    headers = {'Authorization': f'token {token}'}
    api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}"
    response = requests.get(api_url, headers = headers)

    if response.status_code == 404:
        file_path = "README.rst"
        api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}"
        response = requests.get(api_url, headers = headers)

    if response.status_code == 200:
        # Parsing response JSON
        content = response.json()

        if 'content' in content:
            # Decoding content from base64
            file_content = content['content'].encode('utf-8')
            file_content = base64.b64decode(file_content)
            save_readme_to_file(repo_name, file_content)
            # print(f"File '{repo_name}/{file_path}' downloaded successfully.")
        else:
            print("File '{repo_name}/{file_path}' not found.")
    else:
        print("Error occurred while downloading file '{repo_name}/{file_path}'.")



input_file_name = "URLs.txt"
token = "fmsdlvs"
with open(input_file_name, 'r') as f:
    urls = f.readlines()


for url in urls:
    github_url = url.split(",")[0].strip("\"")
    file_path = "README.md"
    download_file_from_github(github_url, file_path, token=token)



# # Example usage
# user = "username"
# repo = "repository-name"
# file_path = "path/to/file.txt"
# token = "your-access-token"

# download_file_from_github(user, repo, file_path, token)