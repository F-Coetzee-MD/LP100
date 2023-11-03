import time
import subprocess

target_script = "your_target_script.py"

while True:
    # Wait for the target script to exit
    process = subprocess.Popen(["python", target_script], shell=True)
    process.wait()  

    # Wait for 5 seconds before restarting
    time.sleep(5) 
