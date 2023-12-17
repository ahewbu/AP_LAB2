import os
import csv
               

def Parse(annotation_name: str) -> str:
    string = ""

    with open(annotation_name, newline='') as file:
        file_reader = csv.reader(file)
        for row in file_reader:
            string = row[0].split("\\")[0]
            break
    return string

               
class Iterator:
    def __init__(self, class_name, annotation_name):
        self.class_name = class_name
        self.annotation_name = annotation_name
        string = Parse(annotation_name)
        
        class_dir = os.path.join(string, class_name)
        if not os.path.exists(class_dir):
            raise FileNotFoundError(f"Directory '{class_dir}' does not exist.")
        self.paths = [
            os.path.join(class_dir, filename)
            for filename in os.listdir(class_dir)
        ]
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.paths):
            path = self.paths[self.index]
            self.index += 1
            return path
        else:
            raise StopIteration
     
        
if __name__ == "__main__":
    rev1 = Iterator('1', 'annotation.csv')

    print(next(rev1))

    