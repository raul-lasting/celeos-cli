import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import requests
import global_params 


def show_profiles():
    
    response = requests.get(f"{global_params.get_url()}/scenario/list", headers=global_params.get_user_hader())
    
    data_response = response.json()
    
    profile_list = []
    
    if response.status_code != 200:
        print(data_response.get('message'))
        response.raise_for_status()
    else:
        if not data_response.get("items"):
            print("There are no profiles for this user.")
        else:
            for index, profiles in enumerate(data_response["items"], start = 1):
                profile_name = profiles.get("name")
                print(f"{index}. {profile_name}")
                profile_list.append(profile_name)
                
    return profile_list
    
    
if __name__ == "__main__":
    profiles = show_profiles()
    selected_index = int(input("\nEnter the profile number you want: "))
    selected_profile = profiles[selected_index - 1]
    print(f"\nYou selected profile: {selected_profile}")
    