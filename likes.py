import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

def read_data_from_csv():
    likes=pd.read_csv('likes.csv')
    return likes


def data_cleaning():
    #DO NOT REMOVE FOLLOWING LINE
    #call remove_unwanted_columns() function to get dataframe
    likes=read_data_from_csv()
    dropped_columns=['following or not','like type']
    likes.drop(columns=dropped_columns,inplace=True)
    renamed_columns={'user ':'user_id','photo':'photo_id','created time':'created_at'}
    likes.rename(columns=renamed_columns,inplace=True)
        #Remove Unwanted columns
    
    
    
    #rename columns, only these columns are allowed in the dataset
    # 1.	user_id
    # 2.	photo_id
    # 3.	created_at
    
    #export cleaned Dataset to newcsv file named "likes_cleaned.csv"
    likes.to_csv('likes_cleaned.csv',index = False)
    return likes


#Do not Delete the Following function
def task_runner():
    data_cleaning()

