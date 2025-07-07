import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import requests 
import json
import global_params


def get_status_state():
    
    response = requests.get(f"{global_params.get_url()}/status/state", headers=global_params.get_header())
    
    data_response = response.json()
    
    if response.status_code != 200:
        print(data_response.get("message"))
        response.raise_for_status()
    else:
        print(json.dumps(data_response, indent=4))
    return data_response
    
    
def get_status_log():
    
    response = requests.get(f"{global_params.get_url()}/status/log", headers=global_params.get_header())
    
    data_response = response.json()
    
    if response.status_code != 200:
        print(data_response.get("message"))
        response.raise_for_status()
    else:
        print(json.dumps(data_response.get('list'), indent=4))
    return data_response.get('list')

    
def get_status_vars():    
    
    response = requests.get(f"{global_params.get_url()}/status/vars", headers=global_params.get_header())
    
    data_response = response.json()
    
    if response.status_code != 200:
        print(data_response.get("message"))
        response.raise_for_status()
    else:
        print(json.dumps(data_response, indent=4))
    return data_response


if __name__ == "__main__":
    get_status_state()
    #get_status_vars()
    #get_status_log()