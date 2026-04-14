import logging
from pathlib import Path


LOG_FILE = Path(".") / "logs/robocurtain.log"


def get_logger(name: str) -> logging.Logger:
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            logging.FileHandler(LOG_FILE),   # append by default
            logging.StreamHandler()          # still prints to terminal
        ]
    )
    return logging.getLogger(name)

