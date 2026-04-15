from alarm import get_wake_up_time
from logger import get_logger


log = get_logger(__name__)

if __name__ == "__main__":
    log.info("RoboCurtain starting...")
    wake_up = get_wake_up_time()
    if wake_up:
        log.info(f"Parsed datetime: {wake_up}")
    
    log.info("RoboCurtain is done and also going to sleep. ZzZz...")
