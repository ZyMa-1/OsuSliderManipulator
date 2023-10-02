# Building with Nuitka (v 1.7.8)
Building not complicated PySide6 project with Nuitka is straightforward.

Install nuitka in your venv:
```bash
pip3 install nuitka
```

Execute following command:
```bash
nuitka --onefile --follow-imports --quiet --disable-console --plugin-enable=pyside6 --output-filename=slider_manipulator_v1.1.exe .\main.py
```