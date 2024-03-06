# pip install plyer

import time
from plyer import notification

if __name__ == '__main__':
    while True:
        notification.notify(
            title = "Attend a class",
            message = "Complete scalar sessions",
            timeout = 10
        )
        time.sleep(15)