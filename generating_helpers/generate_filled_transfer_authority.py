def generate_filled_transfer_authority(Deceased, Executor_or_Next_of_Kin, Funeral_Director, Transfer_Authority, fitz):
    deceased = Deceased(
        given_name = 'John',
        family_name = 'Smith',
        address = '123 street street',
        dob = '11/22/2222'
    )

    executor_info = Executor_or_Next_of_Kin(
        given_name='given_name',
        family_name='family_name',
        address='address',
        contact_phone_number='contact_phone_number',
        name_of_deceased='name_of_deceased',
        relationship_to_deceased='relationship_to_deceased',
        if_nominated='if_nominated'
    )

    funeral_director_info = Funeral_Director(
        funeral_company_name='funeral_company_name',
        address='address',
        transfer_company='transfer_company',
        contact_person='contact_person',
        phone='04XXXXXXXX',
        fax_or_email='fax_or_email'
    )

    transfer_authority = Transfer_Authority(
        no_unit = '12',
        street = 'street street',
        suburb = 'suburb',
        state = 'NSW',
        other_country = 'China'
    )
    
    deceased_full_name = deceased.given_name + ' ' + deceased.family_name
    
    fields = [
        (135, 243, funeral_director_info.funeral_company_name),
        (207, 271, deceased_full_name),
        (95, 327, deceased.dob),
        (173, 355, transfer_authority.no_unit),
        (283, 355, transfer_authority.street),
        (82, 383, transfer_authority.suburb),
        (283, 383, transfer_authority.state),
        (435, 383, transfer_authority.other_country),
        (150, 456, executor_info.given_name + ' ' + executor_info.family_name),
        (200, 484, executor_info.relationship_to_deceased)
    ]

    doc = fitz.open("documents/NSW-Coroners-Authority-to-Transfer.pdf") 
    page = doc[0] 
    for x, y, text in fields:
        page.insert_text(
            (x, y),
            text,
            fontsize=12,
            color=(0,0,0)
        )
    doc.save(f'output_files/Authority-to-Transfer-{deceased_full_name}.pdf')