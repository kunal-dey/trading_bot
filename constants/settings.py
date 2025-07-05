from datetime import datetime

DEBUG = True

# time settings
__current_time = datetime.now()

if DEBUG:
    START_TIME = datetime(__current_time.year, __current_time.month, __current_time.day, 20, 8, 0)
    START_BUYING_TIME = datetime(__current_time.year, __current_time.month, __current_time.day, 0, 2, 0)
    END_TIME = datetime(__current_time.year, __current_time.month, __current_time.day, 20, 12)
    STOP_BUYING_TIME = datetime(__current_time.year, __current_time.month, __current_time.day, 23, 58, 0)
else:
    START_TIME = datetime(__current_time.year, __current_time.month, __current_time.day, 9, 15, 0)
    START_BUYING_TIME = datetime(__current_time.year, __current_time.month, __current_time.day, 9, 30, 0)
    STOP_BUYING_TIME = datetime(__current_time.year, __current_time.month, __current_time.day, 12, 30, 0)
    END_TIME = datetime(__current_time.year, __current_time.month, __current_time.day, 15, 28)

SLEEP_INTERVAL = 1 if DEBUG else 45