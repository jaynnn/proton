import schedule
import time
import subprocess

def job():
    subprocess.run(["python", "__export.py"])

schedule.every().second.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)