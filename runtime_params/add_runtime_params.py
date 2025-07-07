import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import requests 
import global_params
import json


def add_runtime_params_from_file(runtime_file):
    
    runtime_params = global_params.read_from_file(runtime_file)
    runtime_params = add_runtime_params(runtime_params)
    return runtime_params


def add_runtime_params(runtime_params: json):
    
    response = requests.post(f"{global_params.get_url()}/runtime_params", headers = global_params.get_user_hader(), data = runtime_params)
    data_response = response.json()
    
    if response.status_code != 200:
        print(f"Could not send parameters. {data_response['message']}")
        response.raise_for_status()
        
    else:
        print(data_response['message'])
        
    return runtime_params


if __name__ == '__main__':
    add_runtime_params_from_file("Runtime_parameters/runtime_params.json")