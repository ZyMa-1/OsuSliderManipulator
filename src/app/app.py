import logging

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from src.app.widgets.MainWindow import MainWindow

logger = logging.getLogger(__name__)


def run(args):
    """Creates app and launches it"""

    app = QApplication(args)

    app_name = "Slider manipulator"
    app_ver = "1.1"

    app.setOrganizationName(app_name)
    app.setApplicationName(app_name)
    app.setApplicationVersion(app_ver)

    icon = QIcon(":/icons/icons/SliderManipulator.png")
    QApplication.setWindowIcon(icon)

    logger.debug("App started")
    window = MainWindow()
    window.setWindowIcon(icon)
    window.setWindowTitle(app_name + " " + app_ver)
    window.show()
    app.exec()
    logger.debug("App finished")
