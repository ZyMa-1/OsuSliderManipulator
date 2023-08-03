import logging.config
import os
import sys
from datetime import datetime
from pathlib import Path

from src.app import app

root_path = Path(os.path.abspath(__file__)).parent


def setup_logging(*, level: int):
    """Load logging configuration"""
    # Make logs dir if it does not exist
    logs_path = root_path / "logs"
    logs_path.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y_%m_%d-%H_%M_%S")
    logging.config.fileConfig(
        'logging_config.ini',
        disable_existing_loggers=False,
        defaults={"logfilename": f"logs/{timestamp}.log"}
    )
    logging.getLogger().setLevel(level)


if __name__ == "__main__":
    setup_logging(level=logging.DEBUG)
    app.run(sys.argv)
    sys.exit(0)
