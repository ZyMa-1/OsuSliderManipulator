import pathlib
import subprocess

from PySide6.QtCore import Slot, QObject, Qt
from PySide6.QtGui import QIntValidator, QDoubleValidator
from PySide6.QtWidgets import QMainWindow, QFileDialog

from src.app.ui.Ui_MainWindow import Ui_MainWindow
from src.app.widgets.AboutDialog import AboutDialog
from src.app.widgets.HowToUserThisDialog import HowToUseThisDialog
from src.app.widgets.SettingsDialog import SettingsDialog
from src.app_backend.SettingsManager import SettingsManager
from src.app_backend.slider_convertor_module.SliderConvertor import SliderConvertor


def delete_empty_lines(text: str) -> str:
    """ChatGPT write that, not responsible for that"""
    lines = text.splitlines()
    non_empty_lines = [line for line in lines if line.strip()]
    result = '\n'.join(non_empty_lines)
    return result


class MainWindow(QMainWindow):
    """
    Main window of an application
    """

    def __init__(self):
        super().__init__()

        # Setup UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Create SettingsManager instance and apply settings
        self.settings_manager = SettingsManager()
        main_widget_always_stay_on_top = self.settings_manager.get("main_widget_always_stay_on_top")
        if main_widget_always_stay_on_top:
            self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        sliders_v1_save_fields = bool(self.settings_manager.get("sliders_v1_save_fields")[0][1])
        sliders_v2_save_fields = bool(self.settings_manager.get("sliders_v2_save_fields")[0][1])
        self.fields_save_logic = _FieldsSaveLogic(parent=self, sliders_v1_save_fields=sliders_v1_save_fields,
                                                  sliders_v2_save_fields=sliders_v2_save_fields)

        # Create Tab Logic instances
        self.tab1_logic = _Tab1Logic(parent=self)
        self.tab2_logic = _Tab2Logic(parent=self)

        # Add validators to the line edits
        self.ui.slider_tick_rate_line_edit.setValidator(QDoubleValidator(self))
        self.ui.beat_length_line_edit.setValidator(QDoubleValidator(self))
        self.ui.current_sv_multiplier_line_edit.setValidator(QDoubleValidator(self))
        self.ui.beatmap_sv_line_edit.setValidator(QDoubleValidator(self))
        self.ui.destination_line_edit.setValidator(QIntValidator(self))
        self.ui.destination_line_edit_2.setValidator(QIntValidator(self))

        # Connect Signals to slots
        self.ui.do_stuff_button.clicked.connect(self.tab1_logic.handle_do_stuff_button_clicked)
        self.ui.do_stuff_button_2.clicked.connect(self.tab2_logic.handle_do_stuff_button_clicked)
        self.ui.choose_osu_file_button_2.clicked.connect(self.handle_choose_osu_file_button_clicked)
        self.ui.open_osu_file_button_2.clicked.connect(self.handle_open_osu_file_button_clicked)

        # Connect actions
        self.ui.action_about.triggered.connect(self.show_about_dialog)
        self.ui.action_how_to_use_this.triggered.connect(self.show_how_to_use_this_dialog)
        self.ui.action_settings.triggered.connect(self.show_settings_dialog)

    @Slot()
    def show_about_dialog(self):
        dialog = AboutDialog(parent=self)
        dialog.setModal(True)
        dialog.show()

    @Slot()
    def show_settings_dialog(self):
        dialog = SettingsDialog(parent=self)
        dialog.setModal(True)
        dialog.show()

    @Slot()
    def show_how_to_use_this_dialog(self):
        dialog = HowToUseThisDialog(parent=self)
        dialog.setModal(True)
        dialog.show()

    @Slot()
    def handle_choose_osu_file_button_clicked(self):
        file_path, filter_str = QFileDialog.getOpenFileName(self, caption="Choose .osu file",
                                                            filter="Osu Files (*.osu)",
                                                            dir=str(pathlib.Path(
                                                                self.settings_manager.get("osu_path")) / "Songs"))
        if file_path:
            self.ui.choose_osu_file_line_edit_2.setText(file_path)

    @Slot()
    def handle_open_osu_file_button_clicked(self):
        path_str = self.ui.choose_osu_file_line_edit_2.text()
        osu_file_path = pathlib.Path(path_str)
        if path_str and osu_file_path.exists():
            try:
                subprocess.Popen(['notepad.exe', path_str])
            except OSError as e:
                raise OSError(str(e))

    def closeEvent(self, event):
        if self.fields_save_logic:
            self.fields_save_logic.handle_widget_closed()


class _Tab1Logic(QObject):
    def __init__(self, *, parent=None):  # parent must be dialog widget
        super().__init__(parent)

        self.dialog_widget = parent

    @Slot()
    def handle_do_stuff_button_clicked(self):
        slider_tick_rate = float(self.dialog_widget.ui.slider_tick_rate_line_edit.text())
        beat_length = float(self.dialog_widget.ui.beat_length_line_edit.text())
        current_sv_multiplier = float(self.dialog_widget.ui.current_sv_multiplier_line_edit.text())
        beatmap_sv = float(self.dialog_widget.ui.beatmap_sv_line_edit.text())
        destination_ms = int(self.dialog_widget.ui.destination_line_edit.text())
        timing_example_data = self.dialog_widget.ui.timing_example_data_line_edit.text()
        sliders_data = delete_empty_lines(self.dialog_widget.ui.sliders_text_edit.toPlainText())

        result_str_list = SliderConvertor.convert_sliders(slider_tick_rate=slider_tick_rate,
                                                          beat_length=beat_length,
                                                          current_sv_multiplier=current_sv_multiplier,
                                                          beatmap_sv=beatmap_sv,
                                                          destination_ms=destination_ms,
                                                          sliders_data=sliders_data,
                                                          timing_example_data=timing_example_data)

        self.dialog_widget.ui.result_timing_text_edit.setPlainText("\n".join(result_str_list))


class _Tab2Logic(QObject):
    def __init__(self, *, parent=None):  # parent must be dialog widget
        super().__init__(parent)

        self.dialog_widget = parent

    @Slot()
    def handle_do_stuff_button_clicked(self):
        osu_file_path = pathlib.Path(self.dialog_widget.ui.choose_osu_file_line_edit_2.text())
        destination_ms = int(self.dialog_widget.ui.destination_line_edit_2.text())
        sliders_data = delete_empty_lines(self.dialog_widget.ui.sliders_text_edit_2.toPlainText())

        result_str_list = SliderConvertor.convert_sliders_with_osu_file(osu_file_path=osu_file_path,
                                                                        destination_ms=destination_ms,
                                                                        sliders_data=sliders_data)

        self.dialog_widget.ui.result_timing_text_edit_2.setPlainText("\n".join(result_str_list))


class _FieldsSaveLogic(QObject):
    def __init__(self, *, parent=None, sliders_v1_save_fields: bool,
                 sliders_v2_save_fields: bool):  # parent must be dialog widget
        super().__init__(parent)

        self.dialog_widget = parent

        # Initialize SettingsManager instance and add handlers to it
        self._settings = SettingsManager()
        if sliders_v1_save_fields:
            self.add_slider_v1_handlers()
        if sliders_v2_save_fields:
            self.add_slider_v2_handlers()

    def add_slider_v1_handlers(self):
        self._settings.sliders_v1_config.add_handler('slider_tick_rate',
                                                     self.dialog_widget.ui.slider_tick_rate_line_edit)
        self._settings.sliders_v1_config.add_handler('beat_length',
                                                     self.dialog_widget.ui.beat_length_line_edit)
        self._settings.sliders_v1_config.add_handler('current_sv_multiplier',
                                                     self.dialog_widget.ui.current_sv_multiplier_line_edit)
        self._settings.sliders_v1_config.add_handler('beatmap_sv',
                                                     self.dialog_widget.ui.beatmap_sv_line_edit)
        self._settings.sliders_v1_config.add_handler('destination',
                                                     self.dialog_widget.ui.destination_line_edit)
        self._settings.sliders_v1_config.add_handler('timing_example_data',
                                                     self.dialog_widget.ui.timing_example_data_line_edit)
        self._settings.sliders_v1_config.add_handler('sliders',
                                                     self.dialog_widget.ui.sliders_text_edit)

    def add_slider_v2_handlers(self):
        self._settings = SettingsManager()
        self._settings.sliders_v2_config.add_handler('osu_file',
                                                     self.dialog_widget.ui.choose_osu_file_line_edit_2)
        self._settings.sliders_v2_config.add_handler('destination',
                                                     self.dialog_widget.ui.destination_line_edit_2)
        self._settings.sliders_v2_config.add_handler('sliders',
                                                     self.dialog_widget.ui.sliders_text_edit_2)

    @Slot()
    def handle_widget_closed(self):
        self._settings.save()
        self._settings.remove_all_handlers()
        self._settings.reload()
