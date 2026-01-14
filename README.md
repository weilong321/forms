# Funeral Case Management & Automated PDF Form Generator

A cross‑platform desktop application for funeral directors and case managers, designed to streamline the creation, storage, and management of legally required documentation.

This project automates the generation of NSW funeral authority forms, manages case data, and maintains a searchable deceased index — all through a Tkinter‑based GUI. It is packaged for distribution using PyInstaller and runs as a standalone executable on Windows.

---

## Features

### **Automated PDF Form Generation**
- Fills official NSW forms:
  - *Authority to Collect Deceased*
  - *Coroner’s Authority to Transfer*
- Uses **PyPDF** and **PyMuPDF (fitz)** to inject structured case data into PDF templates.
- Outputs professionally formatted PDFs ready for printing or digital submission.

### **Case Management System**
- Create, save, and load individual cases.
- Each case stores:
  - Deceased details  
  - Executor / next‑of‑kin details  
  - Funeral director information  
  - Authority‑to‑collect metadata  
- Cases are saved as JSON for portability and long‑term storage.

### **Deceased Index**
- Automatically maintains a searchable index of all cases.
- Updates dynamically whenever a case is created or modified.
- Stored as a JSON file in a writable runtime directory.

### **Desktop Application**
- Built with **Tkinter** for a simple, accessible GUI.
- Fully self‑contained executable — no Python installation required for end users.
- Cross‑platform architecture (Windows `.exe`, macOS `.app`).

---

## Architecture Overview

The project is structured for clarity, maintainability, and PyInstaller compatibility:

```
app/
    gui.py
    paths.py
    helpers.py
    assets/
        documents/   (PDF templates)
        data/        (default data)
    generating_helpers/
        generate_filled_authority_to_collect_deceased.py
        generate_filled_transfer_authority.py
```

### Key Architectural Decisions

- **Separation of assets vs. runtime data**  
  - Assets (PDF templates) are bundled inside the executable.  
  - Runtime data (cases, index, output PDFs) is stored in writable directories next to the executable.

- **Dependency injection for PDF generation**  
  - PDF helpers receive `document_path` and `output_file` functions, making them environment‑agnostic and testable.

- **PyInstaller‑safe path resolution**  
  - `paths.py` detects whether the app is running from source or from a PyInstaller bundle (`_MEIPASS`).

- **Modular class design**  
  - Deceased, Executor, FuneralDirector, and AuthorityToCollect are clean data models with `.to_dict()` serialization.

---

## Technologies Used

### **Core Python**
- Python 3.10  
- Tkinter (GUI)  
- `uuid`, `datetime`, `json`, `pathlib`

### **PDF Processing**
- **PyPDF** — form field filling and PDF writing  
- **PyMuPDF (fitz)** — text insertion and template manipulation  

### **Packaging & Deployment**
- **PyInstaller**  
  - Bundles assets  
  - Handles Babel locale data  
  - Excludes heavy scientific libraries  
  - Produces standalone executables

### **Localization**
- **Babel** — required by `tkcalendar` for date localization  
- Includes bundled locale data for PyInstaller compatibility

---

## Running the Application

### **From Source**
```bash
pip install -r requirements.txt
python main.py
```

### **Packaged Executable (Windows)**
- Download the ZIP containing:
  - `main.exe`
  - `output_files/` (created automatically if missing)
- Extract the ZIP
- Double‑click `main.exe`

### **Packaged Executable (macOS)**
- Build on macOS using PyInstaller  
- Run the `.app` bundle  
- If unsigned, macOS will require “Open Anyway” via Security settings

---

## Building the Executable

### **Windows**
```bash
pyinstaller --onefile --windowed main.py \
  --add-data "app/assets;app/assets" \
  --add-data "<path-to-babel-locale-data>;babel/locale-data" \
  --hidden-import babel.numbers \
  --hidden-import babel.dates \
  --hidden-import babel.core \
  --hidden-import babel.localedata \
  --exclude-module numpy \
  --exclude-module pandas \
  --exclude-module scipy \
  --exclude-module matplotlib \
  --exclude-module pyarrow \
  --exclude-module PyQt5
```

### **macOS**
Use `:` instead of `;` in `--add-data`.

---

## Challenges Solved

- **PyInstaller asset bundling**  
  Ensured PDF templates and Babel locale data load correctly inside `_MEIPASS`.

- **Writable runtime directories**  
  Prevented write failures by separating bundled assets from user‑generated data.

- **Cross‑platform path resolution**  
  Designed `paths.py` to behave consistently on Windows and macOS.

- **PDF form automation**  
  Integrated two different PDF libraries to handle both form fields and free‑text insertion.

- **Executable distribution**  
  Produced a fully standalone `.exe` suitable for non‑technical users.

---

## Future Enhancements

- Add search and filtering to the deceased index  
- Add more documents for PDF filling
- Package macOS `.dmg` installer  