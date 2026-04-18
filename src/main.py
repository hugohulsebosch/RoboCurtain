from alarm import get_wake_up_time
from logger import get_logger
from scheduler import schedule_open, schedule_close
from sun import get_sunrise_and_sunset
from datetime import timedelta


log = get_logger(__name__)


def main():
    log.info("RoboCurtain starting...")
    wake_up = get_wake_up_time()
    sunrise, sunset = get_sunrise_and_sunset()
    if wake_up:
        open_alarm = wake_up - timedelta(minutes=10)
        open_sun = sunrise + timedelta(minutes=15)
        schedule_open(max(open_alarm, open_sun))

    schedule_close(sunset)

    log.info("RoboCurtain is done scheduling and going to sleep. ZzZz...")


if __name__ == "__main__":
    main()
