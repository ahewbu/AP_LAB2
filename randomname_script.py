import random
import os
import shutil
import csv
from typing import Optional

from copy_script import create_dir


def get_element(class_name: str) -> Optional[str]:
    """This function return us list of names in data class"""
    for file_name in os.listdir(os.path.join("data", class_name)):
        yield file_name


def create_randomname_file(dir_copy: str, annotation_name: str) -> None:
    """This function create the copy of data in another directory with names which are random numbers"""
    file_number = list(range(10001))
    random.shuffle(file_number)
    counter = 1
    create_dir(dir_copy)
    for data_class in os.listdir("data"):
        for file_name in get_element(data_class):
            shutil.copy(os.path.join(os.path.join("data", data_class), file_name),
                        os.path.join(dir_copy, f"{file_number[counter]}.txt"))

            with open(os.path.join(dir_copy, annotation_name), mode="a", newline='') as file:
                file_writer = csv.writer(file, delimiter=" ")
                file_writer.writerow([os.path.join(os.path.abspath(dir_copy), f"{file_number[counter]}.txt"), os.path.join(dir_copy, f"{file_number[counter]}.txt"), data_class])
            counter += 1


def run3(annotation_name: str, dir_copy: str) -> None:
    create_randomname_file(annotation_name, dir_copy)