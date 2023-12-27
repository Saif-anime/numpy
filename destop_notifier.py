import time

# install plyer module 
from plyer import notification 

if __name__ == '__main__':
    notification.notify(

        title = "Plz Subscribe my channal",
        message = "Like short and video support us",

        # displaying time 
        timeout = 2

    )
    # waiting time 
    time.sleep(7)
