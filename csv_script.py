import os
import csv

def create_csv_annotation(annotation_name: str) -> None:
    """This function generates a CSV annotation by taking three inputs: the absolute file path, the relative file path, the file's class name."""
    path_to_class = os.path.join('data')
    class_names = os.listdir(path_to_class)
    with open(annotation_name, mode="w", newline='') as file:
        file_writer = csv.writer(file, delimiter=" ")
        for name in class_names:
            file_writer.writerow(
                [os.path.join(os.path.abspath(path_to_class), name), os.path.join('data', name), name])

def run1(annotation_name: str) -> None:
    create_csv_annotation(annotation_name)
