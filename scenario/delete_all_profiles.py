import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import requests
import global_params

#Add return if it worked
def delete_all_scenarios():
    
    response = requests.delete(f"{global_params.get_url()}/scenario/all", headers=global_params.get_user_hader())
    
    data_response = response.json()
    
    if response.status_code != 200:
        #Check if it prints the message after raise function
        print(f"Could not delete scenario. {data_response.get('message')}")
        response.raise_for_status()
    else:
        print(data_response["message"])
    
    
if __name__ == "__main__":
    delete_all_scenarios()