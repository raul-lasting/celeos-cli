import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import requests 
import json
import global_params


def show_list():
    
    response = requests.get(f"{global_params.get_url()}/sigmf/list", headers=global_params.get_user_hader())
    
    data_response = response.json()
    
    if response.status_code != 200:
        print(data_response.get('message'))
        response.raise_for_status()
    else:
        print(json.dumps(data_response, indent=4))
    return data_response

    
def get_sigmf_archives():
    
    response = requests.get(f"{global_params.get_url()}/sigmf/list", headers=global_params.get_user_hader())
    
    data_response = response.json()
    
    if response.status_code != 200:
        print(data_response.get('message'))
        response.raise_for_status()
    else:
        archive_names = [item["archive"] for item in data_response.get("items", [])]
        for name in archive_names:
            print(name)
        return archive_names
    
    
def get_archives_and_size():
    
    response = requests.get(f"{global_params.get_url()}/sigmf/list", headers=global_params.get_user_hader())
    
    data_response = response.json()
    
    if response.status_code != 200:
        print(data_response.get('message'))
        response.raise_for_status()
    else:
        for archives in data_response.get("items", []):
            print(archives)
        return data_response.get("items", [])
        
        
if __name__ == "__main__":
    show_list()
    #get_sigmf_archives()
    #get_archives_and_size()