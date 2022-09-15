import csv
import os
from src import some_storage_library
#Used a similar method as the sourcecolumns.py to obtianing the file. Then was able to add the data to the file by iterating through using .split
#Note that with open has an 'a' because we are appending not overwritting this allows us to keep the header row

class DataExtraction:

    def obtainingfilepath(rel_path:str)->str:
        path_file =  'data/source/' + rel_path
        dir = os.path.dirname(__file__)
        PATH_NAME = os.path.join(os.path.split(dir)[0], path_file)
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



