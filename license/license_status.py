import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import requests 
import json
import global_params


def loaded_scenario():
    
    response = requests.get(f"{global_params.get_url()}/license/status", headers=global_params.get_header())
    
    data_response = response.json()
    
    if response.status_code != 200:
        print(data_response.get("message"))
        sys.exit()
    else:
        print(json.dumps(data_response, indent=4))
    

def main():
    loaded_scenario()
    
if __name__ == "__main__":
    main()