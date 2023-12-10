import os
from typing import Optional


def get_next_element(class_mark: str) -> Optional[str]:
    """This function return gradually elements of class"""
    path = os.path.join("dataset", class_mark)
    names_list = os.listdir(path)
    names_list.append(None)
    for i in range(0, len(names_list)):
        yield names_list[i]