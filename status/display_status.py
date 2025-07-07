import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import requests
import global_params
import time

def display_status():
    

    while True:
        
        response_logs = requests.get(f'{global_params.get_url()}/status/state', headers=global_params.get_user_hader())
        
        logs = response_logs.json()
        print(logs)
        print()

        # for message_json in logs['list']:
            
        #     log_msg = message_json.get("message")
            
        #     if log_msg not in last_seen_log:
        #         print(message_json)
        #         last_seen_log.add(log_msg)
        time.sleep(0.1)
    

if __name__ == "__main__":
    display_status()