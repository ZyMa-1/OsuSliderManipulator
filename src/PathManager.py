import pathlib


class PathManager:
    """Class for storing paths."""
    PROJECT_ROOT: pathlib.Path | None = None
    SETTINGS_DIR: pathlib.Path | None = None
    LOGS_DIR: pathlib.Path | None = None
    LOGGING_INI: pathlib.Path | None = None

    @classmethod
    def set_project_root(cls, path: pathlib.Path):
        cls.PROJECT_ROOT = path
        cls.SETTINGS_DIR = cls.PROJECT_ROOT / "settings"
        cls.LOGS_DIR = cls.PROJECT_ROOT / "logs"
        cls.LOGGING_INI = cls.PROJECT_ROOT / 'logging_config.ini'
