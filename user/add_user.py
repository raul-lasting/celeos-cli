import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import requests 
import json
import getpass
import global_params


def add_user_from_file(user_file):
    
    payload = global_params.read_from_file(user_file)
    data = json.loads(payload)
    credentials = add_user(data["user"], data["name"], data["email"], data["pass"])
    return credentials


def add_user(user: str, name: str, email: str, password: str):
    
    payload = json.dumps({
        "user": user,
        "name": name,
        "email": email,
        "pass": password
    })
    
    #For login
    credentials = {
        "user": user,
        "pass": password
    }
    
    response = requests.post(f"{global_params.get_url()}/user", headers=global_params.get_header(), data=payload)
    
    if response.status_code != 201:
        print("User was not added. Try again. Check user list.")
        response.raise_for_status()
    else:
        print("New user was added succesfully.")
    return credentials

if __name__ == "__main__":
    user = str(input("Username: "))
    name = str(input("Name: "))
    email = str(input("Email: "))
    password = getpass.getpass("Password: ")
    add_user(user, name, email, password)
    
    #add_user_from_file("user/user_file.json")