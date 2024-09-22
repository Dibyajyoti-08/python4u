'''
Implement a function that checks if a specific process 
(e.g., python) is currently running on the system.
'''

import subprocess

def check_status():
    status = subprocess.run(["pgrep", "python3"], capture_output=True, text=True)
    return status.stdout.strip()

if check_status():
    print("Python process is running.")
else:
    print("Python process is not running.")