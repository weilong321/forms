import tkinter as tk
from tkinter import messagebox, ttk
from tkinter.simpledialog import askstring
from tkcalendar import DateEntry

from app.info.deceased import Deceased
from app.info.executor_or_next_of_kin import Executor_or_Next_of_Kin
from app.info.funeral_director import Funeral_Director
from app.info.authority_to_collect_deceased import Authority_to_Collect_Deceased
from app.info.transfer_authority import Transfer_Authority
from app.layout import FormLayout
from app.helpers import load_case, save_case, load_deceased_index, generate_filled_forms

current_case_code = None
layout = FormLayout()

def refresh_deceased_dropdown(dropdown):
    index = load_deceased_index()
    options = [
        f"{entry['given_name']} {entry['family_name']} ({entry['case_code']})"
        for entry in index
    ]
    dropdown["values"] = options

def load_case_into_form(case_code):
    """
    Given a case code, load the JSON and populate all GUI fields.
    Also sets current_case_code so submit() knows which case to save.
    """
    global current_case_code
    try:
        data = load_case(case_code)
    except FileNotFoundError:
        messagebox.showerror("Error", f"Case {case_code} not found")
        return

    current_case_code = data["case_code"]

    # ---------------- DECEASED ----------------
    d_given.delete(0, tk.END)
    d_given.insert(0, data["deceased"]["given_name"])

    d_family.delete(0, tk.END)
    d_family.insert(0, data["deceased"]["family_name"])

    d_no_unit.delete(0, tk.END)
    d_no_unit.insert(0, data["deceased"]["no_unit"])

    d_street.delete(0, tk.END)
    d_street.insert(0, data["deceased"]["street"])

    d_suburb.delete(0, tk.END)
    d_suburb.insert(0, data["deceased"]["suburb"])

    d_state.delete(0, tk.END)
    d_state.insert(0, data["deceased"]["state"])

    d_country.delete(0, tk.END)
    d_country.insert(0, data["deceased"]["country"])

    d_dob.set_date(data["deceased"]["dob"])

    gender_var.set(data["deceased"]["gender"])

    # ---------------- EXECUTOR / NEXT OF KIN ----------------
    e_given.delete(0, tk.END)
    e_given.insert(0, data["executor_or_next_of_kin"]["given_name"])

    e_family.delete(0, tk.END)
    e_family.insert(0, data["executor_or_next_of_kin"]["family_name"])

    e_address.delete(0, tk.END)
    e_address.insert(0, data["executor_or_next_of_kin"]["address"])

    e_phone.delete(0, tk.END)
    e_phone.insert(0, data["executor_or_next_of_kin"]["contact_phone_number"])

    e_relationship.delete(0, tk.END)
    e_relationship.insert(0, data["executor_or_next_of_kin"]["relationship_to_deceased"])

    e_is_nominated.delete(0, tk.END)
    e_is_nominated.insert(0, data["executor_or_next_of_kin"]["if_nominated"])

    # ---------------- FUNERAL DIRECTOR ----------------
    fd_company.delete(0, tk.END)
    fd_company.insert(0, data["funeral_director"]["funeral_company_name"])

    fd_address.delete(0, tk.END)
    fd_address.insert(0, data["funeral_director"]["address"])

    fd_transfer.delete(0, tk.END)
    fd_transfer.insert(0, data["funeral_director"]["transfer_company"])

    fd_contact.delete(0, tk.END)
    fd_contact.insert(0, data["funeral_director"]["contact_person"])

    fd_phone.delete(0, tk.END)
    fd_phone.insert(0, data["funeral_director"]["phone"])

    fd_fax_email.delete(0, tk.END)
    fd_fax_email.insert(0, data["funeral_director"]["fax_or_email"])

    # ------------ AUTHORITY TO COLLECT DECEASED ---------
    collect_authority_facility.delete(0, tk.END)
    collect_authority_facility.insert(0, data["authority_to_collect_deceased"]["facility"])

    collect_authority_MRN.delete(0, tk.END)
    collect_authority_MRN.insert(0, data["authority_to_collect_deceased"]["MRN"])

    collect_authority_MO.delete(0, tk.END)
    collect_authority_MO.insert(0, data["authority_to_collect_deceased"]["MO"])

    collect_authority_address.delete(0, tk.END)
    collect_authority_address.insert(0, data["authority_to_collect_deceased"]["address"])

    collect_authority_location.delete(0, tk.END)
    collect_authority_location.insert(0, data["authority_to_collect_deceased"]["location_ward"])


def on_deceased_selected():
    selection = selected_deceased.get()
    if not selection:
        return

    case_code = selection.split("(")[-1].replace(")", "")
    load_case_into_form(case_code)

def load_case_from_gui():
    global current_case_code
    case_code = askstring("Load Case", "Enter Case Code:")

    if not case_code:
        return

    data = load_case(case_code)
    current_case_code = data["case_code"]

    # Populate fields
    d_given.delete(0, tk.END)
    d_given.insert(0, data["deceased"]["given_name"])
    d_family.delete(0, tk.END)
    d_family.insert(0, data["deceased"]["family_name"])
    d_no_unit.delete(0, tk.END)
    d_no_unit.insert(0, data["deceased"]["no_unit"])
    d_street.delete(0, tk.END)
    d_street.insert(0, data["deceased"]["street"])
    d_suburb.delete(0, tk.END)
    d_suburb.insert(0, data["deceased"]["suburb"])
    d_state.delete(0, tk.END)
    d_state.insert(0, data["deceased"]["state"])
    d_country.delete(0, tk.END)
    d_country.insert(0, data["deceased"]["country"])
    d_dob.set_date(data["deceased"]["dob"])
    gender_var.set(data["deceased"]["gender"])

    e_given.delete(0, tk.END)
    e_given.insert(0, data["executor_or_next_of_kin"]["given_name"])
    e_family.delete(0, tk.END)
    e_family.insert(0, data["executor_or_next_of_kin"]["family_name"])
    e_address.delete(0, tk.END)
    e_address.insert(0, data["executor_or_next_of_kin"]["address"])
    e_phone.delete(0, tk.END)
    e_phone.insert(0, data["executor_or_next_of_kin"]["contact_phone_number"])
    e_relationship.delete(0, tk.END)
    e_relationship.insert(0, data["executor_or_next_of_kin"]["relationship_to_deceased"])
    e_is_nominated.insert(0, data["executor_or_next_of_kin"]["if_nominated"])

    fd_company.delete(0, tk.END)
    fd_company.insert(0, data["funeral_director"]["funeral_company_name"])
    fd_address.delete(0, tk.END)
    fd_address.insert(0, data["funeral_director"]["address"])
    fd_transfer.delete(0, tk.END)
    fd_transfer.insert(0, data["funeral_director"]["transfer_company"])
    fd_contact.delete(0, tk.END)
    fd_contact.insert(0, data["funeral_director"]["contact_person"])
    fd_phone.delete(0, tk.END)
    fd_phone.insert(0, data["funeral_director"]["phone"])
    fd_fax_email.delete(0, tk.END)
    fd_fax_email.insert(0, data["funeral_director"]["fax_or_email"])

    collect_authority_facility.delete(0, tk.END)
    collect_authority_facility.insert(0, data["funeral_director"]["facility"])
    collect_authority_MRN.delete(0, tk.END)
    collect_authority_MRN.insert(0, data["funeral_director"]["MRN"])
    collect_authority_MO.delete(0, tk.END)
    collect_authority_MO.insert(0, data["funeral_director"]["MO"])
    collect_authority_address.delete(0, tk.END)
    collect_authority_address.insert(0, data["funeral_director"]["address"])
    collect_authority_location.delete(0, tk.END)
    collect_authority_location.insert(0, data["funeral_director"]["location_ward"])

def submit():
    try:
        global current_case_code

        deceased = Deceased(
            d_given.get(),
            d_family.get(),
            d_dob.get(),
            gender_var.get(),
            d_no_unit.get(),
            d_street.get(),
            d_suburb.get(),
            d_state.get(),
            d_country.get()
        )

        executor = Executor_or_Next_of_Kin(
            e_given.get(),
            e_family.get(),
            e_address.get(),
            e_phone.get(),
            f"{deceased.given_name} {deceased.family_name}",
            e_relationship.get(),
            e_is_nominated.get()
        )

        funeral_director = Funeral_Director(
            fd_company.get(),
            fd_address.get(),
            fd_transfer.get(),
            fd_contact.get(),
            fd_phone.get(),
            fd_fax_email.get()
        )

        authority_to_collect_deceased = Authority_to_Collect_Deceased(
            collect_authority_facility.get(),
            collect_authority_MRN.get(),
            collect_authority_MO.get(),
            collect_authority_address.get(),
            collect_authority_location.get()
        )

        current_case_code = save_case(
            deceased,
            executor,
            funeral_director,
            authority_to_collect_deceased,
            current_case_code
        )

        generate_filled_forms(deceased, executor, funeral_director, authority_to_collect_deceased)

        messagebox.showinfo(
            "Saved",
            f'''Case saved successfully\nCase Code: {current_case_code}\
                \nOutput Files generated'''
        )

    except Exception as e:
        messagebox.showerror("Error", str(e))


root = tk.Tk()
root.title("Funeral Case Entry")

selected_deceased = tk.StringVar()

# Top section: Load existing case (spans both columns)
tk.Label(
    root,
    text="Select Existing Case",
    font=("Arial", 10, "bold")
).grid(row=0, column=0, columnspan=2, sticky="w", padx=5, pady=5)

deceased_dropdown = ttk.Combobox(
    root,
    textvariable=selected_deceased,
    state="readonly",
    width=45
)
deceased_dropdown.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

deceased_dropdown.bind("<<ComboboxSelected>>", lambda e: on_deceased_selected())
refresh_deceased_dropdown(deceased_dropdown)

# Create left frame for personal info
left_frame = tk.Frame(root)
left_frame.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)

# Create right frame for document info
right_frame = tk.Frame(root)
right_frame.grid(row=2, column=1, sticky="nsew", padx=10, pady=10)

# Configure column weights for proper resizing
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# ============ LEFT FRAME: DECEASED, EXECUTOR, FUNERAL DIRECTOR ============

# --- DECEASED ---
tk.Label(left_frame, text="Deceased", font=("Arial", 10, "bold")).grid(
    row=0, column=0, sticky="w", pady=(10, 0)
)

d_given = tk.Entry(left_frame)
d_family = tk.Entry(left_frame)
d_dob = DateEntry(left_frame, date_pattern="dd/mm/yyyy", showweeknumbers=False, width=17)

d_no_unit = tk.Entry(left_frame)
d_street = tk.Entry(left_frame)
d_suburb = tk.Entry(left_frame)
d_state = tk.Entry(left_frame)
d_country = tk.Entry(left_frame)

# Gender
gender_var = tk.StringVar(value="MALE")
tk.Label(left_frame, text="Gender").grid(
    row=5, column=0, sticky="e", padx=5
)
male_rb = tk.Radiobutton(left_frame, text="MALE", variable=gender_var, value="MALE")
female_rb = tk.Radiobutton(left_frame, text="FEMALE", variable=gender_var, value="FEMALE")
male_rb.grid(row=5, column=1, sticky="w")
female_rb.grid(row=5, column=1, sticky="e")

deceased_labels = [
    ("Given Name", d_given, 1),
    ("Family Name", d_family, 2),
    ("DOB", d_dob, 3),
    ("House/Unit Number", d_no_unit, 6),
    ("Street Name", d_street, 7),
    ("Suburb Name", d_suburb, 8),
    ("State", d_state, 9),
    ("Country", d_country, 10),
]

for label, entry, row in deceased_labels:
    tk.Label(left_frame, text=label).grid(row=row, column=0, sticky="e", padx=5)
    entry.grid(row=row, column=1, padx=5, pady=2)

# --- EXECUTOR / NEXT OF KIN ---
tk.Label(left_frame, text="Executor / Next of Kin", font=("Arial", 10, "bold")).grid(
    row=11, column=0, sticky="w", pady=(10, 0)
)

e_given = tk.Entry(left_frame)
e_family = tk.Entry(left_frame)
e_address = tk.Entry(left_frame)
e_phone = tk.Entry(left_frame)
e_relationship = tk.Entry(left_frame)
e_is_nominated = tk.Entry(left_frame)

executor_fields = [
    ("Given Name", e_given, 12),
    ("Family Name", e_family, 13),
    ("Address", e_address, 14),
    ("Phone", e_phone, 15),
    ("Relationship", e_relationship, 16),
    ("Is Nominated", e_is_nominated, 17),
]

for label, entry, row in executor_fields:
    tk.Label(left_frame, text=label).grid(row=row, column=0, sticky="e", padx=5)
    entry.grid(row=row, column=1, padx=5, pady=2)

# --- FUNERAL DIRECTOR ---
tk.Label(left_frame, text="Funeral Director", font=("Arial", 10, "bold")).grid(
    row=18, column=0, sticky="w", pady=(10, 0)
)

fd_company = tk.Entry(left_frame)
fd_address = tk.Entry(left_frame)
fd_transfer = tk.Entry(left_frame)
fd_contact = tk.Entry(left_frame)
fd_phone = tk.Entry(left_frame)
fd_fax_email = tk.Entry(left_frame)

funeral_fields = [
    ("Company Name", fd_company, 19),
    ("Address", fd_address, 20),
    ("Transfer Company", fd_transfer, 21),
    ("Contact Person", fd_contact, 22),
    ("Phone", fd_phone, 23),
    ("Fax / Email", fd_fax_email, 24),
]

for label, entry, row in funeral_fields:
    tk.Label(left_frame, text=label).grid(row=row, column=0, sticky="e", padx=5)
    entry.grid(row=row, column=1, padx=5, pady=2)

# ============ RIGHT FRAME: AUTHORITY TO COLLECT DECEASED ============

tk.Label(right_frame, text="Authority to Collect Deceased", font=("Arial", 10, "bold")).grid(
    row=0, column=0, sticky="w", pady=(10, 0)
)

collect_authority_facility = tk.Entry(right_frame)
collect_authority_MRN = tk.Entry(right_frame)
collect_authority_MO = tk.Entry(right_frame)
collect_authority_address = tk.Entry(right_frame)
collect_authority_location = tk.Entry(right_frame)

authority_fields = [
    ("Facility", collect_authority_facility, 1),
    ("MRN", collect_authority_MRN, 2),
    ("MO", collect_authority_MO, 3),
    ("Address", collect_authority_address, 4),
    ("Location / Ward", collect_authority_location, 5),
]

for label, entry, row in authority_fields:
    tk.Label(right_frame, text=label).grid(row=row, column=0, sticky="e", padx=5)
    entry.grid(row=row, column=1, padx=5, pady=2)

# ============ SUBMIT BUTTON (bottom, spans both columns) ============
tk.Button(root, text="Submit Case", command=submit).grid(
    row=3, column=0, columnspan=2, pady=15
)

root.mainloop()