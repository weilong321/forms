class Authority_to_Collect_Deceased:

    def __init__(self, facility, family_name, given_name, MRN, gender, dob, MO, address, location_ward):
        self.facility = facility
        self.family_name = family_name
        self.given_name = given_name
        self.MRN = MRN
        self.gender = gender
        self.dob = dob
        self.MO = MO
        self.address = address
        self.location_ward = location_ward

        dob_split = dob.split('/')
        self.day = dob_split[0]
        self.month = dob_split[1]
        self.year = dob_split[2]