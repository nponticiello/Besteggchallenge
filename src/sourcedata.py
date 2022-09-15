import csv
import os
from src import some_storage_library
#Going to iterate over the file being receieved then as that is occuring we are going to open the output.csv and split the line, so we can write the row
#Note that with open has an 'a' because we are appending not overwritting this allows us to keep the header row

class DataExtraction:

    def addingdata(path_name:str):
        file = open(path_name, "r")
        with open('output.csv', 'a', newline='') as f:
            mywriter = csv.writer(f, delimiter=',')
            for line in file:
                cur_line = line.split("|")
                mywriter.writerow(cur_line)
            some_storage_library.SomeStorageLibrary.load_csv('output.csv')
            f.close()



