class Funeral_Director:

    def __init__(self, funeral_company_name, address, transfer_company, contact_person, phone, fax_or_email):
        self.funeral_company_name = funeral_company_name
        self.address = address
        self.transfer_company = transfer_company
        self.contact_person = contact_person
        self.phone = phone
        self.fax_or_email = fax_or_email

    def to_dict(self):
        return {
            "funeral_company_name": self.funeral_company_name,
            "address": self.address,
            "transfer_company": self.transfer_company,
            "contact_person": self.contact_person,
            "phone": self.phone,
            "fax_or_email": self.fax_or_email
        }