import os

# Get the absolute path of this file (global_params.py)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Read URL
def get_url():
    with open(os.path.join(BASE_DIR, "URL"), 'r') as file:
        url = file.read().strip()
        return url

# Standard header for requests
def get_header():
    # Headers
    header = {'Content-Type': 'application/json'}
    return header

# Header with token for logged users 
def get_user_hader():
    # Token
    with open(os.path.join(BASE_DIR, "user_token.txt"), 'r') as f:
        token = f.read().strip()

    # Header with token for logged users
    user_header = {
        'Content-Type': 'application/json',
        'Authorization': token
    }
    return user_header

# Token used for sigmf archive
def get_token():
    # Token
    with open(os.path.join(BASE_DIR, "user_token.txt"), 'r') as f:
        token = f.read().strip()

    return token

# General function for file read
def read_from_file(file_path: str):
    try:
        with open(file_path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File not found -> {file_path}")
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        
