import os
import collections
import csv
import datetime


#Retrieved abs path by using dirname + the file path. Then iterated through the data and added to a dict, which was then put in a OrderedDict to sort. 
#The values were then in order which allowed me to add those as the headers to the csv

class ColumnExtraction:

    def filepath(rel_path: str) -> str:
        path_file = 'data/source/' + rel_path
        dir = os.path.dirname(__file__)
        path_name = os.path.join(os.path.split(dir)[0], path_file)
        return path_name

    def obtaining_headers(path_name: str):
        header_dict = {}
        header_list = []
        file = open(path_name, "r")
        for line in file:
            cur_line = line.split("|")
            header_dict[int(cur_line[0])] = cur_line[1]
            ordered_headers = collections.OrderedDict(sorted(header_dict.items()))
        for key, value in ordered_headers.items():
            header_list.append(value)
        return header_list

    def uploadingheaders(headerlist: []):
        ct = datetime.datetime.now()
        cur_date = ct.strftime('%m-%d-%Y')
        with open(f'{cur_date}.csv', 'w') as file:
            writer = csv.DictWriter(file, delimiter=',', fieldnames=headerlist)
            writer.writeheader()
