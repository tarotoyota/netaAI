from dataclasses import dataclass
from typing import List, Dict

@dataclass
class FactivatorTable:
    """
    teacher_data_list: List[List[str]]  # [["Author", "Sketch name or Season + Episode number", "Explanation"], ...]
    factivator_dict : Dict[str, List[str]]  # {"attribute name or anything else": ["factivator lines"], ...}
    """
    name: str
    teacher_data_list: List[List[str]]
    factivator_dict: Dict[str, List[str]]
    note: str = ""
#    actual_use_case_list

