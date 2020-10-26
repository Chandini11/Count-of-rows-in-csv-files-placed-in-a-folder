 # -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 16:39:29 2020


"""


# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 11:57:57 202
"""

#importing the necessary libraries
import pandas as pd
import os
import glob
import csv
import sys
from pathlib import Path

#working directory

input_path = input("Please enter the working directory:")

def record(input_path):
    #file format
    extension = 'csv'
    
    #create a dataframe to write the name of the file and count
    data = pd.DataFrame(columns = ['File_Name','File_Count']) 
    
    file_name_list = []
    file_count_list = []
    
    #iterate the files in folder
    for i in glob.glob(input_path+'/*.{}'.format(extension)):
        file_name = Path(i).name
        count_of_records = 0    
        file_name_list.append(file_name)
        print("Reading file count from {}".format(file_name))
        df = pd.read_csv(i)
        count_of_records = len(df)
        print(count_of_records)
        file_count_list.append(count_of_records)
        
    data['File_Name'] = file_name_list
    data['File_Count'] = file_count_list
    
    data.to_csv(input_path+'/Record_Count.csv',index = False)
    print("Output generated in {}".format(input_path))
if os.path.isdir(input_path):    
    record(input_path)
else:
    print("Please enter a valid path")
    sys.exit(1)
