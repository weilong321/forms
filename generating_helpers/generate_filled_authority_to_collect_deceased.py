def generate_filled_authority_to_collect_deceased(deceased_info, executor_info, funeral_director_info, authority_to_collect_info, PdfReader, PdfWriter):
    
    dob_split = deceased_info.dob.split("/")
    day = dob_split[0]
    month = dob_split[1]
    year = dob_split[2]

    reader = PdfReader("documents/Authority-to-collect-deceased.pdf")
    writer = PdfWriter()

    writer.append(reader)

    writer.update_page_form_field_values(
        writer.pages[0],
        {
            **{
                "Facility": (authority_to_collect_info.facility, "/F1", 0),
                "FAMILY NAME": (deceased_info.family_name, "/F1", 0),
                "GIVEN NAME": (deceased_info.given_name, "/F1", 0),
                "MO": (authority_to_collect_info.MO, "/F1", 0),
                "undefined": '/' + deceased_info.gender,
                "undefined_2": (day, "/F1", 0), 
                "undefined_3": (month, "/F1", 0), 
                "undefined_4": (year, "/F1", 0),
                "MRN": (authority_to_collect_info.MRN, "/F1", 0),
                "ADDRESSAUTHORITY TO COLLECT DECEASED": (authority_to_collect_info.address, "/F1", 0),
                "LOCATION  WARD": (authority_to_collect_info.location_ward, "/F1", 0)
            },
            **{
                "Given Name": (executor_info.given_name, "/F1", 0),
                "Family Name": (executor_info.family_name, "/F1", 0),
                "Address": (executor_info.address, "/F1", 0),
                "Contact Phone Number": (executor_info.contact_phone_number, "/F1", 0),
                "I print name": (executor_info.given_name + " " + executor_info.family_name, "/F1", 0),
                "give authority to Funeral Director": (funeral_director_info.funeral_company_name, "/F1", 0),
                "to collect the body of name of deceased": (executor_info.name_of_deceased, "/F1", 0),
                "Relationship  to  Deceased": (executor_info.relationship_to_deceased, "/F1", 0),
                "If nominated as a delegate of the ExecutorNext of Kin please provide details": (executor_info.if_nominated, "/F1", 0),
            },
            **{
                "Funeral Company Name": (funeral_director_info.funeral_company_name, "/F1", 0),
                "Address_2": (funeral_director_info.address, "/F1", 0),
                "Transfer Company if applicable": (funeral_director_info.transfer_company, "/F1", 0),
                "Contact Person": (funeral_director_info.contact_person, "/F1", 0),
                "Phone": (funeral_director_info.phone, "/F1", 0),
                "Fax  or Email": (funeral_director_info.fax_or_email, "/F1", 0)
            }
        },
        auto_regenerate=False,
    )

    writer.update_page_form_field_values(
        writer.pages[1],
        {
            **{
                "Facility_2": (authority_to_collect_info.facility, "/F1", 0),
                "FAMILY NAME_2": (deceased_info.family_name, "/F1", 0),
                "GIVEN NAME_2": (deceased_info.given_name, "/F1", 0),
                "MO_2": (authority_to_collect_info.MO, "/F1", 0),
                "undefined_6": '/' + deceased_info.gender + '_2',
                "DOB_2": (day, "/F1", 0), 
                "undefined_7": (month, "/F1", 0), 
                "undefined_8": (year, "/F1", 0),
                "MRN_2": (authority_to_collect_info.MRN, "/F1", 0),
                "ADDRESSAUTHORITY TO COLLECT DECEASED_2": (authority_to_collect_info.address, "/F1", 0),
                "LOCATION  WARD_2": (authority_to_collect_info.location_ward, "/F1", 0)
            }
        },
        auto_regenerate=False,
    )

    writer.write(f"output_files/authority-to-collect-deceased-{executor_info.name_of_deceased}.pdf")