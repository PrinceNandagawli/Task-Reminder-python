from msilib.schema import Icon
import time
from plyer import notification


if __name__ == "__main__":
    notification.notify(
        title = "Your most important task today",
        message = "you have an online class at 3pm",#you can put your custom message here
        app_icon = "C:\\Users\\NITRO\\Desktop\\Reminder\\yt.ico",
        timeout = 5
        
    )

