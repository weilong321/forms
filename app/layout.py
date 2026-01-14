class FormLayout:
    def __init__(self):
        # ---------------- DECEASED ----------------
        self.deceased = {
            "start": 2,
            "given_name": 3,
            "family_name": 4,
            "dob": 5,
            "gender": 6,          # label + radio buttons share this row
            "house_unit": 7,
            "street": 8,
            "suburb": 9,
            "state": 10,
            "country": 11
        }

        # ---------------- EXECUTOR ----------------
        self.executor = {
            "start": 12,
            "given_name": 13,
            "family_name": 14,
            "address": 15,
            "phone": 16,
            "relationship": 17,
            "is_nominated": 18
        }

        # ---------------- FUNERAL DIRECTOR ----------------
        self.funeral_director = {
            "start": 19,
            "company_name": 20,
            "address": 21,
            "transfer_company": 22,
            "contact_person": 23,
            "phone": 24,
            "fax_email": 25
        }

        # ---------------- AUTHORITY TO COLLECT ----------------
        self.authority = {
            "start": 26,
            "facility": 27,
            "mrn": 28,
            "mo": 29,
            "address": 30,
            "location_ward": 31
        }

        # ---------------- SUBMIT BUTTON ----------------
        self.submit_row = 34