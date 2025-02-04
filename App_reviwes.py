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
    count=1000, # defaults to 100
    #filter_score_with=5 # defaults to None(means all score)
)
df=pd.DataFrame(result)
df.to_excel(f"amazonreview.xlsx",index=False)
print(df)
#1.Distribution of ratings
rate_dist=df['score'].value_counts()
print("the distribution of rating is:")
print(rate_dist)
#2. total number of upvotes
total_count=df['thumbsUpCount'].sum()
print("\nThe Total number of upvotes:",total_count)
#3. determine male or female
#we can't find male or female based on the given data. 

#4. calculate lenght of each review
longest_review=df.loc[df["content"].str.len().idxmax(), "content"]
print("The longest reviews:",longest_review)
#5. frequency do users review the app
df['at'] = pd.to_datetime(df['at'])
reviews_df=df.sort_values(by='at')
time_between_reviews = reviews_df['at'].diff().mean()
print(f"Average Time Between Reviews: {time_between_reviews}")
#6. When are reviews most commonly submitted?
df['hour']=df['at'].dt.hour
most_common_time=df['hour'].value_counts().idxmax()
print(f"Most common time:\n",most_common_time)
#7. overall sentiment of the app
rating_sentiment=df['score'].mean()
sentiment="Positive"if rating_sentiment>=3 else print("negative")
print(sentiment)