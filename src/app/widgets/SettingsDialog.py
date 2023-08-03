import pathlib

from PySide6.QtCore import Slot, QObject, Signal, Qt
from PySide6.QtWidgets import QDialog, QPushButton, QFileDialog, QLineEdit, QMessageBox, QCheckBox, \
    QButtonGroup, QDialogButtonBox

from src.app.ui.Ui_SettingsDialog import Ui_SettingsDialog
from src.app_backend.SettingsManager import SettingsManager


class SettingsDialog(QDialog):
    """
    Dialog for settings
    """
    settings_saved = Signal()
    settings_changed = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        # Setup UI
        self.ui = Ui_SettingsDialog()
        self.ui.setupUi(self)

        # Set additional window flags
        self.setWindowFlags(
            self.windowFlags() | Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint | Qt.WindowCloseButtonHint)

        # Disabling 'Apply' button
        self.ui.button_box.button(QDialogButtonBox.StandardButton.Apply).setEnabled(False)

        # Create Button group for radio buttons
        self.sliders_v1_button_group = QButtonGroup()
        self.sliders_v1_button_group.addButton(self.ui.slidesrv1_save_fields_yes_radio_button)
        self.sliders_v1_button_group.addButton(self.ui.slidersv1_save_fields_no_radio_button)
        self.sliders_v1_button_group.setExclusive(True)

        self.sliders_v2_button_group = QButtonGroup()
        self.sliders_v2_button_group.addButton(self.ui.slidesrv2_save_fields_yes_radio_button)
        self.sliders_v2_button_group.addButton(self.ui.slidersv2_save_fields_no_radio_button)
        self.sliders_v2_button_group.setExclusive(True)

        # Add all settings related widgets to a list and connect them to the `settings_changed` signal
        settings_widget_list = [self.ui.osu_folder_path_line_edit, self.ui.always_stay_on_top_check_box,
                                self.sliders_v1_button_group, self.sliders_v2_button_group]
        self.connect_settings_widget_list(settings_widget_list)

        # Create logic instance
        self.logic = _SettingsLogic(parent=self)

        # Connect signals to slots
        self.ui.side_menu_list.currentRowChanged.connect(self.ui.stacked_widget.setCurrentIndex)
        self.ui.button_box.clicked.connect(self.handle_button_box_click)
        self.ui.choose_osu_folder_btn.clicked.connect(self.handle_choose_osu_folder_button_click)
        self.finished.connect(self.logic.handle_dialog_finished)

        # Connect custom signals to slots
        self.settings_saved.connect(self.logic.handle_settings_saved)
        self.settings_changed.connect(self.handle_settings_changed)

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
            case QDialogButtonBox.ButtonRole.AcceptRole:
                self.accept()
            case QDialogButtonBox.ButtonRole.RejectRole:
                self.reject()
            case QDialogButtonBox.ButtonRole.ApplyRole:
                self.apply()
            case _:
                exc_msg = "This button_role is not supported"
                raise TypeError(exc_msg)

    @Slot()
    def handle_choose_osu_folder_button_click(self):
        folder_path = QFileDialog.getExistingDirectory(self, caption="Choose your osu! folder")
        if folder_path:
            if not pathlib.Path(folder_path).name.lower() == "osu!":
                QMessageBox.warning(self, "Warning!", "Folder name must be 'osu!'")
                return
            self.ui.osu_folder_path_line_edit.setText(folder_path)

    @Slot()
    def handle_settings_changed(self):
        self.ui.button_box.button(QDialogButtonBox.StandardButton.Apply).setEnabled(True)

    def accept(self):
        self.settings_saved.emit()
        super().accept()

    def apply(self):
        self.settings_saved.emit()
        self.ui.button_box.button(QDialogButtonBox.StandardButton.Apply).setEnabled(False)

    def connect_settings_widget_list(self, settings_widget_list: list):
        """Connects widgets `valueChanged` type Signals to `settings_changed` Signal"""
        for widget in settings_widget_list:
            if isinstance(widget, QLineEdit):
                widget.textChanged.connect(lambda *args, **kwargs: self.settings_changed.emit())
            if isinstance(widget, QCheckBox):
                widget.stateChanged.connect(lambda *args, **kwargs: self.settings_changed.emit())
            if isinstance(widget, QButtonGroup):
                widget.buttonToggled.connect(lambda *args, **kwargs: self.settings_changed.emit())


class _SettingsLogic(QObject):
    """
    Class to manage business logic
    """

    def __init__(self, *, parent=None):
        super().__init__(parent)

        self.dialog_widget = parent

        # Initialize SettingsManager instance and add handlers to it
        self._settings = SettingsManager()
        self._settings.config.add_handler('osu_path', self.dialog_widget.ui.osu_folder_path_line_edit)
        self._settings.config.add_handler('main_widget_always_stay_on_top',
                                          self.dialog_widget.ui.always_stay_on_top_check_box)
        self._settings.config.add_handler('sliders_v1_save_fields',
                                          self.dialog_widget.sliders_v1_button_group)
        self._settings.config.add_handler('sliders_v2_save_fields',
                                          self.dialog_widget.sliders_v2_button_group)

    @Slot()
    def handle_settings_saved(self):
        """Handles `settings_saved` Signal"""
        self._settings.save()

    @Slot()
    def handle_dialog_finished(self):
        """Handles `finished` Signal"""
        self._settings.remove_all_handlers()
        self._settings.reload()
