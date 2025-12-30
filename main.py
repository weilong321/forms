import logging
logger = logging.getLogger("pypdf")
logger.setLevel(logging.ERROR)

from pypdf import PdfReader, PdfWriter
import fitz

# 1. deceased
# 2. next of kin / executor
# 4. funeral director
# 5. doc specific
from info.deceased import Deceased
from info.executor_or_next_of_kin import Executor_or_Next_of_Kin
from info.funeral_director import Funeral_Director
from info.authority_to_collect_deceased import Authority_to_Collect_Deceased
from info.transfer_authority import Transfer_Authority

from generating_helpers.generate_filled_authority_to_collect_deceased import generate_filled_authority_to_collect_deceased
generate_filled_authority_to_collect_deceased(Executor_or_Next_of_Kin, Funeral_Director, Authority_to_Collect_Deceased, PdfReader, PdfWriter)

from generating_helpers.generate_filled_transfer_authority import generate_filled_transfer_authority
generate_filled_transfer_authority(Deceased, Executor_or_Next_of_Kin, Funeral_Director, Transfer_Authority, fitz)