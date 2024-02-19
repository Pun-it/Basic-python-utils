# A program to compare if 2 files are same or not . [Only for excel and csv files.]
import pandas as pd
import os

preffered_feild = input("The feild that you want to compare. [Please make sure that the feild is same in both the files] : ")

file_1_raw = input("Enter the path of manually recorded file : ")
file_2_raw  = input ("Enter the path of the ecel sheet extracted from GOOGLE DOCS : ")

sorted_file_1 = sorted(file_1_raw)
sorted_file_2 = sorted(file_2_raw)

scanned_file_1 = pd.read_excel(sorted_file_1) or pd.read_csv(sorted_file_1)
scanned_file_2 = pd.read_excel(sorted_file_2) or pd.read_csv(sorted_file_2)

sorted_file_1

if scanned_file_1.count(axis = 0)  == scanned_file_2.count(axis = 0):
    print('Both files match')
else:
    print('There are some extra names in the Google doc')

n = 0
while scanned_file_1.count(axis = 0)  < scanned_file_2.count(axis = 0) :
    n += n 
    if scanned_file_2.loc[n , scanned_file_2.preffered_feildr] != scanned_file_1.loc[all , scanned_file_1.preffered_feild] :
        print(scanned_file_2.loc[n , scanned_file_2.preffered_feild])
        removed = os.remove(scanned_file_2.loc[n])
    else :
        ()



