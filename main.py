"""
This is the entrypoint to the program. 'python main.py' will be executed and the 
expected csv file should exist in ../data/destination/ after the execution is complete.
"""
from src import sourcecolumns
from src import sourcedata

def columns_extractions():
    rel_path = 'data/source/SOURCECOLUMNS.txt'
    relfilepath = sourcecolumns.ColumnExtraction.filepath(rel_path)
    headerslist = sourcecolumns.ColumnExtraction.obtaining_headers(relfilepath)
    sourcecolumns.ColumnExtraction.uploadingheaders(headerslist)

def data_extraction():
    rel_path = 'data/source/SOURCEDATA.txt'
    filepath = sourcedata.DataExtraction.obtainingfilepath(rel_path)
    sourcedata.DataExtraction.addingdata(filepath)


def main():
    columns_extractions()
    data_extraction()



if __name__ == '__main__':
    """Entrypoint"""
    print('Beginning the ETL process...')
    main()
