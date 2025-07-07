import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import requests 
import global_params


def stop_emulation():
    
    response = requests.delete(f"{global_params.get_url()}/device", headers=global_params.get_user_hader())
    data_response = response.json()
    
    if response.status_code != 200:
        print(f"No emulation was stopped. {data_response.get('message')}")
        response.raise_for_status()
    else:
        print("The emulation has been stopped.")

    
if __name__ == "__main__":
    stop_emulation()