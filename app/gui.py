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

    # ------------ TRANSFER AUTHORITY --------------------



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

# ---------------- DECEASED ----------------
tk.Label(root, text="Deceased", font=("Arial", 10, "bold")).grid(
    row=layout.deceased["start"], column=0, sticky="w", pady=(10, 0)
)

d_given = tk.Entry(root)
d_family = tk.Entry(root)
d_dob = DateEntry(root, date_pattern="dd/mm/yyyy", showweeknumbers=False, width=17)

d_no_unit = tk.Entry(root)
d_street = tk.Entry(root)
d_suburb = tk.Entry(root)
d_state = tk.Entry(root)
d_country = tk.Entry(root)

# Gender
gender_var = tk.StringVar(value="MALE")
tk.Label(root, text="Gender").grid(
    row=layout.deceased["gender"], column=0, sticky="e", padx=5
)
male_rb = tk.Radiobutton(root, text="MALE", variable=gender_var, value="MALE")
female_rb = tk.Radiobutton(root, text="FEMALE", variable=gender_var, value="FEMALE")
male_rb.grid(row=layout.deceased["gender"], column=1, sticky="w")
female_rb.grid(row=layout.deceased["gender"], column=1, sticky="e")

# Labels + entries
deceased_labels = [
    ("Given Name", d_given, layout.deceased["given_name"]),
    ("Family Name", d_family, layout.deceased["family_name"]),
    ("DOB", d_dob, layout.deceased["dob"]),
    ("House/Unit Number", d_no_unit, layout.deceased["house_unit"]),
    ("Street Name", d_street, layout.deceased["street"]),
    ("Suburb Name", d_suburb, layout.deceased["suburb"]),
    ("State", d_state, layout.deceased["state"]),
    ("Country", d_country, layout.deceased["country"]),
]

for label, entry, row in deceased_labels:
    tk.Label(root, text=label).grid(row=row, column=0, sticky="e", padx=5)
    entry.grid(row=row, column=1, padx=5, pady=2)

# ---------------- EXECUTOR / NEXT OF KIN ----------------
tk.Label(root, text="Executor / Next of Kin", font=("Arial", 10, "bold")).grid(
    row=layout.executor["start"], column=0, sticky="w", pady=(10, 0)
)

e_given = tk.Entry(root)
e_family = tk.Entry(root)
e_address = tk.Entry(root)
e_phone = tk.Entry(root)
e_relationship = tk.Entry(root)
e_is_nominated = tk.Entry(root)

executor_fields = [
    ("Given Name", e_given, layout.executor["given_name"]),
    ("Family Name", e_family, layout.executor["family_name"]),
    ("Address", e_address, layout.executor["address"]),
    ("Phone", e_phone, layout.executor["phone"]),
    ("Relationship", e_relationship, layout.executor["relationship"]),
    ("Is Nominated", e_is_nominated, layout.executor["is_nominated"]),
]

for label, entry, row in executor_fields:
    tk.Label(root, text=label).grid(row=row, column=0, sticky="e", padx=5)
    entry.grid(row=row, column=1, padx=5, pady=2)

# ---------------- FUNERAL DIRECTOR ----------------
tk.Label(root, text="Funeral Director", font=("Arial", 10, "bold")).grid(
    row=layout.funeral_director["start"], column=0, sticky="w", pady=(10, 0)
)

fd_company = tk.Entry(root)
fd_address = tk.Entry(root)
fd_transfer = tk.Entry(root)
fd_contact = tk.Entry(root)
fd_phone = tk.Entry(root)
fd_fax_email = tk.Entry(root)

funeral_fields = [
    ("Company Name", fd_company, layout.funeral_director["company_name"]),
    ("Address", fd_address, layout.funeral_director["address"]),
    ("Transfer Company", fd_transfer, layout.funeral_director["transfer_company"]),
    ("Contact Person", fd_contact, layout.funeral_director["contact_person"]),
    ("Phone", fd_phone, layout.funeral_director["phone"]),
    ("Fax / Email", fd_fax_email, layout.funeral_director["fax_email"]),
]

for label, entry, row in funeral_fields:
    tk.Label(root, text=label).grid(row=row, column=0, sticky="e", padx=5)
    entry.grid(row=row, column=1)

# -------- AUTHORITY TO COLLECT DECEASED -------------
tk.Label(root, text="Authority to Collect Deceased Document", font=("Arial", 10, "bold")).grid(
    row=layout.authority["start"], column=0, sticky="w", pady=(10, 0)
)

collect_authority_facility = tk.Entry(root)
collect_authority_MRN = tk.Entry(root)
collect_authority_MO = tk.Entry(root)
collect_authority_address = tk.Entry(root)
collect_authority_location = tk.Entry(root)

authority_fields = [
    ("Facility", collect_authority_facility, layout.authority["facility"]),
    ("MRN", collect_authority_MRN, layout.authority["mrn"]),
    ("MO", collect_authority_MO, layout.authority["mo"]),
    ("Address", collect_authority_address, layout.authority["address"]),
    ("Location / Ward", collect_authority_location, layout.authority["location_ward"]),
]

for label, entry, row in authority_fields:
    tk.Label(root, text=label).grid(row=row, column=0, sticky="e", padx=5)
    entry.grid(row=row, column=1, padx=5, pady=2)


# ---------------- LOAD EXISTING CASE ----------------
tk.Label(root, text="Select Existing Case").grid(row=1, column=0, sticky="e", padx=5)

tk.Label(
    root,
    text="Select Existing Case",
    font=("Arial", 10, "bold")
).grid(row=0, column=0, sticky="w", padx=5, pady=5)

deceased_dropdown = ttk.Combobox(
    root,
    textvariable=selected_deceased,
    state="readonly",
    width=45
)
deceased_dropdown.grid(row=1, column=1, padx=10, pady=5)

deceased_dropdown.bind("<<ComboboxSelected>>", lambda e: on_deceased_selected())
refresh_deceased_dropdown(deceased_dropdown)

# ---------------- SUBMIT ----------------
tk.Button(root, text="Submit Case", command=submit).grid(
    row=layout.submit_row, column=0, columnspan=2, pady=15
)

root.mainloop()