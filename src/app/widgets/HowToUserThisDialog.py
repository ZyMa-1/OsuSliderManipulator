import pathlib

from PySide6.QtCore import Slot, Qt
from PySide6.QtWidgets import QDialog, QPushButton, QDialogButtonBox

from src.app.ui.Ui_HowToUseThisDialog import Ui_HowToUseThisDialog


class HowToUseThisDialog(QDialog):
    """
    Dialog to display how to use this shit ui
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        # Setup UI
        self.ui = Ui_HowToUseThisDialog()
        self.ui.setupUi(self)

        # Set additional window flags
        self.setWindowFlags(
            self.windowFlags() | Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint | Qt.WindowCloseButtonHint)

        # Load html to web engine view
        html_path = pathlib.Path(r"static_data/how_to_use_this.html")
        with open(html_path, "r") as f:
            self.ui.web_engine_view.setHtml(f.read())

        # Connect signals to slots
        self.ui.button_box.clicked.connect(self.handle_button_box_click)

    @Slot(QPushButton)
    def handle_button_box_click(self, button: QPushButton):
        """
        Handles button click in a button_box and routes it

        :param button: Button from button_box
        :type button: QPushButton
        :raises TypeError: If button_role is not supported
        """
        button_role = self.ui.button_box.buttonRole(button)
        match button_role:
            case QDialogButtonBox.ButtonRole.RejectRole:
                self.reject()
            case _:
                exc_msg = "This button_role is not supported"
                raise TypeError(exc_msg)
