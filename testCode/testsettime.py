import schedule
import time
import datetime

def job():
   for i in range(11):
    for j in range(i):
        print (i, end=' ')
    print()

schedule.every().day.at("20:47").do(job)

while True:
    schedule.run_pending()
    print(datetime.datetime.now())
    time.sleep(1)