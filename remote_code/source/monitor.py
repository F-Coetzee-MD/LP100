import time
import subprocess

while True:
    # Wait for the target script to exit
    process = subprocess.Popen(
        ["python", "main_loop.py"], shell=True)
    process.wait()  

    # Wait for 5 seconds before restarting
    time.sleep(2) 
