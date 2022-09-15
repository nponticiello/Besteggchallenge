import csv
import os
from src import some_storage_library
import datetime
#Going to iterate over the file being receieved then as that is occuring we are going to open the output.csv and split the line, so we can write the row
#Note that with open has an 'a' because we are appending not overwritting this allows us to keep the header row

class DataExtraction:

    def addingdata(path_name:str):
        ct = datetime.datetime.now()
        cur_date = ct.strftime('%m-%d-%Y')
        file = open(path_name, "r")
        with open(f'{cur_date}.csv', 'a', newline='') as f:
            mywriter = csv.writer(f, delimiter=',')
            for line in file:
                cur_line = line.split("|")
                mywriter.writerow(cur_line)
            some_storage_library.SomeStorageLibrary.load_csv(f'{cur_date}.csv')
            f.close()



