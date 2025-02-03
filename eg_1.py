import pandas as pd

Students=(

{
    "name":"logu",
    "age":18,
    "mark":90
}
,
{
    "name":"tharu",
    "age":18,
    "mark":90
},
{
    
    "name":"logesh",
    "age":None,
    "mark":90
})
data_df=pd.DataFrame(Students)
# df=pd.Series(students)
# print(df.tail(3))
data_df.dropna(inplace=True)

MARK_TRESHOLD=35
student_mark_greater_than_treshold=data_df[data_df['mark']>MARK_TRESHOLD]
print(student_mark_greater_than_treshold)
#
marks_mask=data_df['marks']>MARK_TRESHOLD
string_mask=data_df['name'].str.startswith('z')
data_df_greater_than_treshold=data_df
#read dataset
df=pd.read_csv("cleaned_dataset.csv")
#convert datafile to csv
student_mark_greater_than_treshold.to_csv("data.csv",index=False)