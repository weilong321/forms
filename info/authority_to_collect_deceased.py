class Authority_to_Collect_Deceased:

    def __init__(self, facility, MRN, MO, address, location_ward):
        self.facility = facility
        self.MRN = MRN
        self.MO = MO
        self.address = address
        self.location_ward = location_ward

    def to_dict(self):
        return {
            "facility": self.facility,
            "MRN": self.MRN,
            "MO": self.MO,
            "address": self.address,
            "location_ward": self.location_ward
        }