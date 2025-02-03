import pandas as pd
#creating new csv file
csv_path="C:/Users/keerthi/Documents/java pro/Book1.csv"
read_file=pd.read_csv(csv_path)
#printing the datatypes of the datas
print(read_file.dtype)
# printing the head of the file
print(read_file.head())
# printing the head of the file      
print(read_file.tail())
#proving all the info of the data like DataFrame, including data types and missing values.
print(read_file.info())
#describes the statical info
print(read_file.describe())
#filtering datas
print(read_file[read_file["Name"]=="Alice"])
#printing the datas as boolean value
print([read_file["Name"]=="Alice"])
#index and printing row and column
get_value=read_file.loc[5,"Name"]
#print(get_value)