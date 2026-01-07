def generate_filled_transfer_authority(deceased_info, executor_info, funeral_director_info, fitz):

    deceased_full_name = deceased_info.given_name + ' ' + deceased_info.family_name
    
    fields = [
        (135, 243, funeral_director_info.funeral_company_name),
        (207, 271, deceased_full_name),
        (95, 327, deceased_info.dob),
        (173, 355, deceased_info.no_unit),
        (283, 355, deceased_info.street),
        (82, 383, deceased_info.suburb),
        (283, 383, deceased_info.state),
        (435, 383, deceased_info.country),
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