import os
import requests
from dotenv import load_dotenv
from langchain_core.documents import Document

load_dotenv()

github_token = os.getenv("GITHUB_TOKEN")

def fetch_github(owner, repo, endpoint):
    url = f"https://api.github.com/repos/{owner}/{repo}/{endpoint}"
    headers={
        "Authorization": f"Bearer {github_token}"
    }

    response = requests.get(url,headers=headers)

    if response.status_code==200:
        data=response.json()
    else:
        print("Failed with status code:", response.status_code)
        return []

    return data

def fetch_github_issues(owner, repo):
    data = fetch_github(owner, repo, "issues")
    return load_issues(data)

# def load_issues(issues):
#     docs=[]
#     for entry in issues:
#         metadata={
#             "author": entry["user"]["login"],
#             "comments": entry["comments"],
#             "body": entry["body"],
#             "labels": entry["labels"],
#             "created_at": entry["created_at"]
#         }
#         data = entry["title"]
#         if entry["body"]:
#             data += entry["body"]
#         doc = Document(page_content=data, metadata=metadata)
#         docs.append(doc)
#     return docs

def load_issues(issues):
    docs = []
    max_length = 8000  # Maximum allowed length

    for entry in issues:
        metadata = {
            "author": entry["user"]["login"],
            "comments": entry["comments"],
            "labels": entry["labels"],
            "created_at": entry["created_at"]
        }
        
        # Start with the title
        data = entry["title"] + "\n"  # Add a newline for separation

        # Check if body exists and append it, truncating if necessary
        if entry["body"]:
            combined_length = len(data) + len(entry["body"])
            if combined_length > max_length:
                # Truncate to meet the max_length constraint
                remaining_length = max_length - len(data)
                data += entry["body"][:remaining_length]
            else:
                data += entry["body"]

        doc = Document(page_content=data, metadata=metadata)
        docs.append(doc)
    
    return docs




    

