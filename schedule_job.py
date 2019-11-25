import datetime
import time
import schedule

def job():
    print(datetime.datetime.now())

schedule.every(5).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
