import logging.config
import os
import pathlib
import sys
from datetime import datetime

from src.PathManager import PathManager
from src.app import app


def ensure_if_ok_to_run():
    PathManager.set_project_root(pathlib.Path(__file__).absolute().parent)
    os.makedirs('settings', exist_ok=True)
    os.makedirs('logs', exist_ok=True)


def setup_logging(*, level: int):
    """Load logging configuration"""

    timestamp = datetime.now().strftime("%Y_%m_%d-%H_%M_%S")
    logging.config.fileConfig(
        PathManager.LOGGING_INI.name,
        disable_existing_loggers=False,
        defaults={"logfilename": f"{PathManager.LOGS_DIR.name}/{timestamp}.log"}
    )
    logging.getLogger().setLevel(level)


if __name__ == "__main__":
    ensure_if_ok_to_run()
    setup_logging(level=logging.DEBUG)
    app.run(sys.argv)
    sys.exit(0)
