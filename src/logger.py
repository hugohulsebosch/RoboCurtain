import logging
from pathlib import Path

LOG_FILE = Path(
    "/Users/hugohulsebosch/Documents/Code/RoboCurtain/logs/robocurtain.log")


def get_logger(name: str) -> logging.Logger:
    root = logging.getLogger()

    if not root.handlers:  # only configure once
        LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
        root.setLevel(logging.INFO)

        formatter = logging.Formatter(
            fmt="%(asctime)s [%(levelname)s] %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        file_handler = logging.FileHandler(LOG_FILE)
        file_handler.setFormatter(formatter)

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)

        root.addHandler(file_handler)
        root.addHandler(stream_handler)

    return logging.getLogger(name)
