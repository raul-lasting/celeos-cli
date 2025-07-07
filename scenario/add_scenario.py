import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import requests
import global_params
import json


#Adds scenario from a file path
def add_scenario_from_file(profile_file):
    
    profile = global_params.read_from_file(file_path=profile_file)
    name = add_scenario(profile)
    return name

#Adds the profile with a json object as parameter
def add_scenario(profile: json):
    
    response = requests.post(f"{global_params.get_url()}/scenario", headers=global_params.get_user_hader(), data=profile)
    data_response = response.json()
    
    profile_py = json.loads(profile)
    
    if response.status_code != 201:
        print(f"Could not add scenario. {data_response.get('message')} Please try again.")
        response.raise_for_status()
    else:
        print("Profile has been added to the list.")
    return profile_py["name"]
    
    
if __name__ == "__main__":
    name = add_scenario_from_file("scenario/add_profile.json")
    print(name)