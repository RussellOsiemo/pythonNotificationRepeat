import time

import schedule


def show_notification():
    print("Iam a code that runs every 5 seconds")
    print("after another 5 seconds you'll see me")


schedule.every(5).seconds.do(show_notification)

while 1:
    schedule.run_pending()
    time.sleep(1)
