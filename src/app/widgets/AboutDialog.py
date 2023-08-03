from PySide6.QtWidgets import QDialog, QApplication

from src.app.ui.Ui_AboutDialog import Ui_AboutDialog


class AboutDialog(QDialog):
    """
    Dialog to display info about app
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        # Setup UI
        self.ui = Ui_AboutDialog()
        self.ui.setupUi(self)

        # Update app_version and app_name labels
        app_instance = QApplication.instance()
        app_version = app_instance.applicationVersion()
        app_name = app_instance.applicationName()

        self.ui.version_label.setText(f'- Version {app_version} or something')
        self.ui.name_label.setText(f'{app_name}')
