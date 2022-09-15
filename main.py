"""
This is the entrypoint to the program. 'python main.py' will be executed and the 
expected csv file should exist in ../data/destination/ after the execution is complete.
"""
from src import sourcecolumns
from src import sourcedata

def columns_extractions():
    file_column_name = 'SOURCECOLUMNS.txt'
    relfilepath = sourcecolumns.ColumnExtraction.filepath(file_column_name)
    headerslist = sourcecolumns.ColumnExtraction.obtaining_headers(relfilepath)
    sourcecolumns.ColumnExtraction.uploadingheaders(headerslist)

def data_extraction():
    file_source_name = 'SOURCEDATA.txt'
    filepath = sourcedata.DataExtraction.obtainingfilepath(file_source_name)
    sourcedata.DataExtraction.addingdata(filepath)


def main():
    columns_extractions()
    data_extraction()



if __name__ == '__main__':
    """Entrypoint"""
    print('Beginning the ETL process...')
    main()
