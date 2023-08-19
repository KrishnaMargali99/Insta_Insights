import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

def read_data_from_csv():
    tags=pd.read_csv('tags.csv')
    return tags


def data_cleaning():
    #DO NOT REMOVE FOLLOWING LINE
    #call remove_unwanted_columns() function to get dataframe
    tags=read_data_from_csv()
    dropped_columns=['location']
    tags.drop(columns=dropped_columns,inplace=True)
    renamed_columns={'tag text':'tag_name','created time':'created_at'}
    tags.rename(columns=renamed_columns,inplace=True)
        #Remove Unwanted columns
    
    
    
    #rename columns, only these columns are allowed in the dataset
    # 1.	id
    # 2.	tag_name
    # 3.	created_at
    
    #export cleaned Dataset to newcsv file named "tags_cleaned.csv"
    tags.to_csv('tags_cleaned.csv',index = False)
    return tags


#Do not Delete the Following function
def task_runner():
    data_cleaning()
