import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import requests 
import json
import global_params


def show_users():
    
    response = requests.get(f"{global_params.get_url()}/user/list", headers=global_params.get_user_hader())
    
    data_response = response.json()
    
    if response.status_code != 200:
        print(data_response.get('message'))
        response.raise_for_status()
    else:
        print(json.dumps(data_response, indent=4))
    return data_response

if __name__ == "__main__":
    show_users()