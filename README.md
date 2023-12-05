# Excel-Spreadsheet-Merge
Python functions that merge multiple excel worksheets across multiple workbooks by name in a certain directory


This file contains two functions and an example on how to use the functions.

def dataset(name, directory, sheetname):
    Establishes connection to directory, and checks for all files ending with .xlsx
    prints a message in order to confirm to the user that those files have been recognized 
    appends all worksheets into one list by name, specified by the input "sheetname"

  def createsheet (data, name):
      concatenates list into a dataset
      exports into a new named excel worksheet specified by "name"
