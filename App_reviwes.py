import pandas as pd
# from google_play_scraper import app

# result = app(
#     'in.amazon.mShop.android.shopping',
#     lang='en', # defaults to 'en'
#     country='us' # defaults to 'us'
# )


from google_play_scraper import Sort, reviews

result, continuation_token = reviews(
    'in.amazon.mShop.android.shopping',
    lang='en', # defaults to 'en'
    country='us', # defaults to 'us'
    sort=Sort.NEWEST, # defaults to Sort.NEWEST
    count=200, # defaults to 100
    #filter_score_with=5 # defaults to None(means all score)
)
df=pd.DataFrame(result)
df.to_excel(f"amazonreview.xlsx",index=False)
print(df)
#csv_path="C:/java lab/python/pandas/amazonreview.csv"
#read_f=pd.read_csv(csv_path)
#Distribution of ratings
rate_dist=df['score'].value_counts()
print("the distribution of rating is:")
print(rate_dist)
#total number of upvotes
total_count=df['thumbsUpCount'].sum()
print("\nThe Total number of upvotes:",total_count)
# calculate lenght of each review
words_review=df['content'].str.len()
print(words_review)
#longest review
longest_review=df.loc[df["content"].str.len().idxmax(), "content"]
print(longest_review)
#frequency do users review the app
frequency_re = df['reviewId'].value_counts()
print("\nReview Frequency by Users:",frequency_re)
#When are reviews most commonly submitted?
df['hour']=df['at'].dt.hour
most_common_time=df['hour'].value_counts().idxmax()
print(f"Most common time:\n",most_common_time)
#overall sentiment of the app
rating_sentiment=df['score'].mean()
sentiment="Positive"if rating_sentiment>=3.5 else print("negative")
print(sentiment)