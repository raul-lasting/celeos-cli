import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import requests 
import global_params


def delete_runtime_params():
    
    response = requests.delete(f"{global_params.get_url()}/runtime_params", headers = global_params.get_user_hader())
    data_response = response.json()
    
    if response.status_code != 200:
        print(f"Could not delete parameters. {data_response['message']}")
        response.raise_for_status()
    else:
        print(data_response['message'])
    

if __name__ == '__main__':
    delete_runtime_params()