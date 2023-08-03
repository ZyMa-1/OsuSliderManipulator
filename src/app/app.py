import logging

from PySide6.QtWidgets import QApplication

from src.app.widgets.MainWindow import MainWindow

logger = logging.getLogger(__name__)


def run(args):
    """Creates app and launches it"""

    app = QApplication(args)

    app_name = "Slider manipulator"
    app_ver = "0.1"

    app.setOrganizationName(app_name)
    app.setApplicationName(app_name)
    app.setApplicationVersion(app_ver)

    logger.debug("App started")
    window = MainWindow()
    window.setWindowTitle(app_name + " " + app_ver)
    window.show()
    app.exec()
    logger.debug("App finished")
