import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import requests 
import json
import getpass
import global_params

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(REPO_ROOT)


def login_from_file(file_path):
    payload = global_params.read_from_file(file_path)
    credentials = json.loads(payload)
    token = login(credentials["user"], credentials["pass"])
    write_token(token)


def login(username, password):
    
    payload = json.dumps({
        "user": username,
        "pass": password
    })
    
    response = requests.post(f"{global_params.get_url()}/login", headers=global_params.get_header(), data=payload)
    
    data_reponse = response.json()
    token = data_reponse.get("token")
   
    if response.status_code != 200:
        print("Incorrect credentials. Please try again.")
        response.raise_for_status()
    else:
        print("Authentication successful.")
        
    return token

    
def write_token(token): 
    with open(os.path.join(REPO_ROOT, "user_token.txt"), 'w') as f:
        f.write(token)
        
def login_and_write_token(username, password):
    token = login(username, password)
    write_token(token)
    
if __name__ == "__main__":
    # username = str(input("Username: "))
    # password = getpass.getpass("Password: ")
    # login_and_write_token(username, password)
    login_from_file("login/login_file.json")