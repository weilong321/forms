from classes.authority_to_collect_deceased import Authority_to_Collect_Deceased

test = Authority_to_Collect_Deceased(
    'test_facility',
    'lastname',
    'firstname',
    'male',
    '22/03/2000',
    '123 sydney nsw'
)

print(test.facility)