import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

def read_data_from_csv():
    comments=pd.read_csv('comments.csv')
    return comments


def data_cleaning():
    #DO NOT REMOVE FOLLOWING LINE
    #call remove_unwanted_columns() function to get dataframe
    comments=read_data_from_csv()
    dropped_columns=['posted date','emoji used','Hashtags used count']
    comments.drop(columns=dropped_columns,inplace=True)
    #Remove Unwanted columns
    renamed_columns={'User  id':'user_id','comment':'comment_text','Photo id':'photo_id',
    'created Timestamp':'created_at'}
    comments.rename(columns=renamed_columns,inplace=True)
    
    #rename columns, only these columns are allowed in the dataset
    # 1.	id
    # 2.	comment_text
    # 3.	user_id
    # 4.	photo_id
    # 5.	created_at
    
    #export cleaned Dataset to newcsv file named "comments_cleaned.csv"
    comments.to_csv('comments_cleaned.csv',index=False)
    return comments


#Do not Delete the Following function
def task_runner():
    data_cleaning()

