import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

def read_data_from_csv():
    photos=pd.read_csv('photos.csv')
    return photos


def data_cleaning():
    #DO NOT REMOVE FOLLOWING LINE
    #call remove_unwanted_columns() function to get dataframe
    photos=read_data_from_csv()
    dropped_columns=['Insta filter used','photo type']
    photos.drop(columns=dropped_columns,inplace=True)
    renamed_columns={'image link':'image_url','user ID':'user_id','created dat':'created_date'}
    photos.rename(columns=renamed_columns,inplace=True)
        #Remove Unwanted columns
    
    
    
    #rename columns, only these columns are allowed in the dataset
    # 1.	id
    # 2.	image_url
    # 3.	user_id
    # 4.	created_date
    
    #export cleaned Dataset to newcsv file named "photos_cleaned.csv"
    photos.to_csv('photos_cleaned.csv',index = False)
    return photos


#Do not Delete the Following function
def task_runner():
    data_cleaning()

