# PandaExcelFileSplit
Takes a big Excel file and chops it up in to smaller ones. It's a simple little Python script again created for those that have to work with huge Excel files that contain lots of data. Frequently in my day job I have to import data to MS Dynamics which has a maximum upload filesize. This tool takes that Excel file and chops it up in to smaller ones.

# Usage
python3 excel_splitter.py large_excel_file.xlsx 10000

(where 10000 are the number of rows).

# Dependencies
Needs the pandas py module. pip install pandas
