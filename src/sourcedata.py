import csv
import os
from src import some_storage_library


class DataExtraction:

    def obtainingfilepath(rel_path:str)->str:
        dir = os.path.dirname(__file__)
        PATH_NAME = os.path.join(os.path.split(dir)[0], rel_path)
        return PATH_NAME

    def addingdata(path_name:str):
        file = open(path_name, "r")
        with open('output.csv', 'a', newline='') as f:
            mywriter = csv.writer(f, delimiter=',')
            for line in file:
                cur_line = line.split("|")
                mywriter.writerow(cur_line)
            some_storage_library.SomeStorageLibrary.load_csv('output.csv')
            f.close()



