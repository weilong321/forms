import sys
from pathlib import Path

def base_dir():
    # Running inside PyInstaller bundle
    if hasattr(sys, "_MEIPASS"):
        return Path(sys._MEIPASS)

    # Running from source
    return Path(__file__).resolve().parent

def asset_path(*parts):
    return base_dir() / "app" / "assets" / Path(*parts)

def document_path(name):
    return asset_path("documents", name)

def runtime_root():
    return Path.cwd()

def runtime_data_dir():
    d = runtime_root() / "data"
    d.mkdir(parents=True, exist_ok=True)
    return d

def runtime_cases_dir():
    d = runtime_data_dir() / "cases"
    d.mkdir(parents=True, exist_ok=True)
    return d

def runtime_index_file():
    return runtime_data_dir() / "deceased_index.json"

def output_dir():
    d = Path.cwd() / "output_files"
    d.mkdir(exist_ok=True)
    return d

def output_file(name):
    return output_dir() / name
