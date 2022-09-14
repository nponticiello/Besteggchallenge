import os
import collections
import csv

rel_path = 'data/source/SOURCECOLUMNS.txt'


class ColumnExtraction:

    def filepath(rel_path: str) -> str:
        dir = os.path.dirname(__file__)
        path_name = os.path.join(os.path.split(dir)[0], rel_path)
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
        with open('output.csv', 'w') as file:
            writer = csv.DictWriter(file, delimiter=',', fieldnames=headerlist)
            writer.writeheader()
