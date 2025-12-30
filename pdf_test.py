from pypdf import PdfReader, PdfWriter
import fitz 
from classes.executor_or_next_of_kin import Executor_or_Next_of_Kin
from classes.funeral_director import Funeral_Director
from classes.authority_to_collect_deceased import Authority_to_Collect_Deceased


# reader = PdfReader("documents/NSW-Coroners-Authority-to-Transfer.pdf", strict=False)
# with open("documents/NSW-Coroners-Authority-to-Transfer.pdf", "rb") as f: 
#     reader = PdfReader(f) 
# writer = PdfWriter()

fields = [
    (135, 243, "Funeral Director"),
    (207, 271, "Deceased Name"),
    (95, 327, "dd/mm/yyyy"),
    (173, 355, "no/unit"),
    (283, 355, "street name"),
    (82, 383, "suburb"),
    (283, 383, "state"),
    (435, 383, "other country"),
    (150, 456, "senior next of kin name"),
    (200, 484, "relationship to the deceased")
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
doc.save('testing.pdf')

# fields = reader.get_fields()
# for name in fields:
#     print(name)


# print(fields["undefined_6"])
# print(reader)
# import fitz 
# doc = fitz.open("documents/NSW-Coroners-Authority-to-Transfer.pdf") 
# page = doc[0] # draw vertical lines every 50px 
# for x in range(0, int(page.rect.width), 100): 
#     page.insert_text((x, 20), str(x), fontsize=8, color=(1,0,0))
# for y in range(0, int(page.rect.height), 100): 
#     page.insert_text((5, y), str(y), fontsize=8, color=(0,0,1))
# doc.save("grid.pdf")