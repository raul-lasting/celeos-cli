import os
import sys

ip_add = str(input("IP Address: "))
set_url = f"http://{ip_add}:3001"

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(REPO_ROOT)

with open(os.path.join(REPO_ROOT, "URL"), 'w') as f:
    f.write(set_url)
    