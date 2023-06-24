import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

base_url = "https://api.github.com"
token = os.getenv('GITHUB_TOKEN')
headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/vnd.github.v3+json"
}
def list_repositories():
    url = f"{base_url}/user/repos"
    response = requests.get(url, headers=headers)
    repositories = json.loads(response.text)
    for repository in repositories:
        print(repository["name"])

def create_repository(repo_name):
    url = f"{base_url}/user/repos"
    data = {
        "name": repo_name,
        "auto_init": True
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print("Failed to create repository.")

def delete_repository(repo_name):
    url = f"{base_url}/repos/Shrey496/{repo_name}"
    response = requests.delete(url, headers=headers)
    if response.status_code == 204:
        print(f"Repository '{repo_name}' deleted successfully. ")
    else:
        print("Failed to delete repository.")


# List repositories
list_repositories()

# Create a repository
#create_repository("Created_by_code")

# Delete a repository
delete_repository("Created_by_code")
