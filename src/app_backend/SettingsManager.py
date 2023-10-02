from PySide6.QtWidgets import QTextEdit
from pyqtconfig import ConfigManager, unicode

from src.PathManager import PathManager


class _Singleton(type):
    """
    Singleton metaclass
    """
    _instance = None

    def __call__(cls, *args, **kw):
        if not cls._instance:
            cls._instance = super(_Singleton, cls).__call__(*args, **kw)
        return cls._instance


def _get_TextEdit(self):
    return self.toPlainText()


def _set_TextEdit(self, val: str):
    self.setPlainText(unicode(val))


def _event_TextEdit(self):
    return self.textChanged


class SettingsManager(metaclass=_Singleton):
    """
    Singleton class that stores all the ConfigManager objects
    """

    def __init__(self):
        # Create ConfigManagers
        self.config = ConfigManager(filename=f"{PathManager.SETTINGS_DIR / 'config.json'}")
        self.config.set_defaults({
            "osu_path": "",
            "main_widget_always_stay_on_top": False,
            "sliders_v1_save_fields": [[0, False], [1, True]],
            "sliders_v2_save_fields": [[0, False], [1, True]],
        })

        self.sliders_v1_config = ConfigManager(
            filename=f"{PathManager.SETTINGS_DIR / 'sliders_v1_config.json'}")
        self.sliders_v1_config.add_hooks(QTextEdit, (_get_TextEdit, _set_TextEdit, _event_TextEdit))
        self.sliders_v2_config = ConfigManager(filename=f"{PathManager.SETTINGS_DIR / 'sliders_v2_config.json'}")
        self.sliders_v2_config.add_hooks(QTextEdit, (_get_TextEdit, _set_TextEdit, _event_TextEdit))

        # Create list of them
        self.config_list = []
        for attr in self.__dict__.values():
            if isinstance(attr, ConfigManager):
                self.config_list.append(attr)

    def get(self, key: str) -> str:
        """
       Returns value of the given key among ALL ConfigManagers

       :param: key
       :type key: str
       :returns: Value of the given key
       :rtype: str
       :raises KeyError: If the key is not unique. If the key is not found
       """
        value = None
        for cfg in self.config_list:
            if key in cfg.config:
                if value is not None:
                    exc_msg = "Key is not unique"
                    raise KeyError(exc_msg)
                value = cfg.get(key)
        if value is None:
            for cfg in self.config_list:
                if key in cfg.defaults:
                    if value is not None:
                        exc_msg = "Key is not unique"
                        raise KeyError(exc_msg)
                    value = cfg.get(key)
            if value is None:
                exc_msg = "Key not found"
                raise KeyError(exc_msg)

        return value

    def save(self):
        """Saves all configs to files"""
        for cfg in self.config_list:
            cfg.save()

    def remove_all_handlers(self):
        """Removes all handlers from all configs"""
        for cfg in self.config_list:
            for key in cfg.config.keys():
                cfg.remove_handler(key)

    def reload(self):
        """Reloads all configs from files"""
        for cfg in self.config_list:
            cfg.load()
