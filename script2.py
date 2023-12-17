import shutil
import os
import csv


def create_dir(dir_name: str) -> str:
    """This function create dir where we must copy our data"""
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)
    return dir_name


def create_copy_data(dir_copy: str, annotation_name: str) -> None:
    """This function copy our data in another directory and create csv file with 2 parameters: filename and file's
    class name """
    create_dir(dir_copy)
    for data_item in os.listdir("data"):
        files_list = os.listdir(os.path.join("data", data_item))
        create_dir(os.path.join(dir_copy, data_item))
        for file_name in files_list:
            shutil.copy(os.path.join(os.path.join("data", data_item),
                                     file_name), os.path.join(os.path.join(dir_copy, data_item), f"{file_name}"))
        with open(os.path.join(dir_copy, annotation_name), mode="a", newline='') as file:
            file_writer = csv.writer(file, delimiter=" ")
            for file_name in files_list:
                file_writer.writerow([f"{os.path.join(dir_copy)}\{data_item}\{file_name}", data_item])


def run2(dir_copy: str, annotation_name: str) -> None:
    create_copy_data(dir_copy, annotation_name)