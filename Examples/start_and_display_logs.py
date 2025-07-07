import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import time, signal
import scenario
import device
import signal_handler
import status


signal_handler.signal_handler.received_stop_signal = False
signal.signal(signal.SIGINT, signal_handler.signal_handler)
signal.signal(signal.SIGTERM, signal_handler.signal_handler)  
    
    
if __name__ == "__main__":
    
    profiles = scenario.show_profiles()
    selected_index = int(input("\nEnter the index of the profile you want: "))
    profile = profiles[selected_index - 1]
    device.load_profile_as_string(profile)
    start_time = time.time()
    timeout = 30
    device.start_emulation()
    print("\nEmulation is running. Press Ctrl+C to stop.")
    print()
    status.display_logs()
    time.sleep(3600)