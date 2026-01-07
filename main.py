import logging
logger = logging.getLogger("pypdf")
logger.setLevel(logging.ERROR)

from pypdf import PdfReader, PdfWriter
import fitz
import uuid
from datetime import datetime
import json
import os

INDEX_FILE = "data/deceased_index.json"
CASES_DIR = "data/cases"
os.makedirs(CASES_DIR, exist_ok=True)

def load_deceased_index():
    if not os.path.exists(INDEX_FILE):
        return []

    with open(INDEX_FILE, "r", encoding="utf-8") as f:
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

    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=4)


# 1. deceased
# 2. next of kin
# 3. executor
# 4. funeral director
# 5. doc specific
from info.deceased import Deceased
from info.executor_or_next_of_kin import Executor_or_Next_of_Kin
from info.funeral_director import Funeral_Director
from info.authority_to_collect_deceased import Authority_to_Collect_Deceased
from info.transfer_authority import Transfer_Authority
    
def save_case(deceased, executor, funeral_director, authority_to_collect, case_code=None):
    if case_code is None:
        case_code = generate_case_code()

    file_path = os.path.join(CASES_DIR, f"{case_code}.json")

    case_data = {
        "case_code": case_code,
        "deceased": deceased.to_dict(),
        "executor_or_next_of_kin": executor.to_dict(),
        "funeral_director": funeral_director.to_dict(),
        "authority_to_collect_deceased": authority_to_collect.to_dict()
    }

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(case_data, f, indent=4)

    update_deceased_index(case_code, deceased)

    return case_code

def load_case(case_code):
    file_path = os.path.join(CASES_DIR, f"{case_code}.json")

    if not os.path.exists(file_path):
        raise FileNotFoundError("Case not found")

    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def generate_filled_forms(deceased, executor, funeral_director, authority_to_collect):
    from generating_helpers.generate_filled_authority_to_collect_deceased import generate_filled_authority_to_collect_deceased
    generate_filled_authority_to_collect_deceased(deceased, executor, funeral_director, authority_to_collect, PdfReader, PdfWriter)

    from generating_helpers.generate_filled_transfer_authority import generate_filled_transfer_authority
    generate_filled_transfer_authority(deceased, executor, funeral_director, fitz)

    return 