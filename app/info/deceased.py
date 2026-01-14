class Deceased:
    
    def __init__(self, given_name, family_name, dob, gender, no_unit, street, suburb, state, country):
        self.given_name = given_name
        self.family_name = family_name
        self.dob = dob
        self.gender = gender
        self.no_unit = no_unit
        self.street = street
        self.suburb = suburb
        self.state = state
        self.country = country

    def to_dict(self):
        return {
            "given_name": self.given_name,
            "family_name": self.family_name,
            "dob": self.dob,
            "gender": self.gender,
            "no_unit": self.no_unit,
            "street": self.street,
            "suburb": self.suburb,
            "state": self.state,
            "country": self.country
        }