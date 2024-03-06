import schedule
import time
import subprocess

def job():
    subprocess.run(["tools/py37/py37.exe", "__export.py"])

schedule.every(30).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)