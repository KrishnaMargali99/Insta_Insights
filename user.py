import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

def read_data_from_csv():
    users=pd.read_csv('users.csv')
    return users


def data_cleaning():
    #DO NOT REMOVE FOLLOWING LINE
    #call remove_unwanted_columns() function to get dataframe
    users=read_data_from_csv()
    dropped_columns=['private/public','post count','Verified status']
    users.drop(columns=dropped_columns,inplace=True)
    renamed_columns={'name':'username','created time':'created_at'}
    users.rename(columns=renamed_columns,inplace=True)
        #Remove Unwanted columns
    
    
    
    #rename columns, only these columns are allowed in the dataset
    # 1.	id
    # 2.	username
    # 3.	created_at
    
    #export cleaned Dataset to newcsv file named "users_cleaned.csv"
    users.to_csv('users_cleaned.csv',index = False)
    return users


#Do not Delete the Following function
def task_runner():
    data_cleaning()
