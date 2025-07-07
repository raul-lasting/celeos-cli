import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import time
import device

    
if __name__ == "__main__":
    start_time = time.time()
    timeout = 25
    
    device.start_emulation()
    device.check_if_starts(start_time, timeout)