import pandas as pd

def shorlister():
    # reading the files
    file1 = pd.read_excel(r'C:\Z\AI Club\Shortlisting\Team Members.xlsx')
    file2 = pd.read_excel(r"C:\Z\AI Club\Shortlisting\Recruitment Form'24 (Responses).xlsx")

    # Removing the rows with null vaules in the Email Id column and storing it in a variable 
    file1_emails = file1['Email'].dropna()
    # making a list of email ids and removing tab spaces 
    selected_members = [x.replace("/t","") for x in file1_emails]
    # Creating an empty dataframe
    file3 = pd.DataFrame()
    # appending the index of rows that contain the email ids of selected members
    indexes = []
    for i in range(file2.shape[0]):    
        if file2['Email Address'][i].replace("/t","") in selected_members :
            indexes.append(i)
    # Removing the selected member using the indices
    file3 = file2.drop(indexes,axis = 0)
    # Going thru all the email ids of selected members 
    # Appending True if eamil id is in file3 and false if not
    huhu = []
    for i in range(len(selected_members)):
        huhu.append(selected_members[i] in file3['Email Address'])
    # Checking if True is in huhu
    print(True in huhu)
    # Yahooooooooooooooo!!!!!!!!!
    # The work is now donezezzzz 
    # SAVING...........
    file3.to_excel('notselected.xlsx')