import os
import pandas as pd 


#####  Functions #####
def dataset(name, directory, sheetname):
    for file in os.listdir(directory):
        if file.endswith('.xlsx'):
            print('Loading file {0}...'.format(file))
            name.append(pd.read_excel(os.path.join(directory, file), sheet_name=sheetname))

def createsheet(data, name):
    temp_master = pd.concat(data, axis=0)
    temp_master.to_excel(name, index = False)
 
 
 
 
    
#####  Example  #####
df1 = []
dataset(df1, directory = 'C:/Users/Andrew Petrulakis/Desktop/Reports', sheetname = 'Merge')
        
# print(df1)
#print(len(df1))

createsheet(df1, name = 'Final')
