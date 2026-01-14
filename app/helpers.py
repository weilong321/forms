import logging
logger = logging.getLogger("pypdf")
logger.setLevel(logging.ERROR)

from pypdf import PdfReader, PdfWriter
import fitz
import uuid
from datetime import datetime
import json
import os

from app.paths import (
    runtime_index_file,
    runtime_cases_dir,
    document_path,
    output_file
)

INDEX_FILE = runtime_index_file()
CASES_DIR = runtime_cases_dir()

os.makedirs(CASES_DIR, exist_ok=True)

def load_deceased_index():
    if not INDEX_FILE.exists():
        return []
    with INDEX_FILE.open("r", encoding="utf-8") as f:
        return json.load(f)

def generate_case_code():
    date_part = datetime.now().strftime("%Y%m%d")
    unique_part = uuid.uuid4().hex[:6].upper()
    return f"CASE-{date_part}-{unique_part}"

def update_deceased_index(case_code, deceased):
    index = load_deceased_index()

    for entry in index:
        if entry["case_code"] == case_code:
            entry["given_name"] = deceased.given_name
            entry["family_name"] = deceased.family_name
            break
    else:
        index.append({
            "case_code": case_code,
            "given_name": deceased.given_name,
            "family_name": deceased.family_name
        })

    with INDEX_FILE.open("w", encoding="utf-8") as f:
        json.dump(index, f, indent=4)

def save_case(deceased, executor, funeral_director, authority_to_collect, case_code=None):
    if case_code is None:
        case_code = generate_case_code()

    file_path = CASES_DIR / f"{case_code}.json"

    case_data = {
        "case_code": case_code,
        "deceased": deceased.to_dict(),
        "executor_or_next_of_kin": executor.to_dict(),
        "funeral_director": funeral_director.to_dict(),
        "authority_to_collect_deceased": authority_to_collect.to_dict()
    }

    with file_path.open("w", encoding="utf-8") as f:
        json.dump(case_data, f, indent=4)

    update_deceased_index(case_code, deceased)

    return case_code

def load_case(case_code):
    file_path = CASES_DIR / f"{case_code}.json"
    if not file_path.exists():
        raise FileNotFoundError("Case not found")
    with file_path.open("r", encoding="utf-8") as f:
        return json.load(f)

def generate_filled_forms(deceased, executor, funeral_director, authority_to_collect):
    from app.generating_helpers.generate_filled_authority_to_collect_deceased import generate_filled_authority_to_collect_deceased
    generate_filled_authority_to_collect_deceased(deceased, executor, funeral_director, authority_to_collect, PdfReader, PdfWriter)

    from app.generating_helpers.generate_filled_transfer_authority import generate_filled_transfer_authority
    generate_filled_transfer_authority(deceased, executor, funeral_director, fitz)

    return 