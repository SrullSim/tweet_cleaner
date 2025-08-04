import pandas as pd
import numpy as np
from loader import Loader
from pprint import  pprint
class ExploreData:

    def __init__(self, df):
        self.df = df
        self.set_len_column()
        self.sub_df = self.split_df()
        self.sum_by_category = self.sum_by_category()


    def split_df(self):
        non_anty_df = self.df[self.df["Biased"] == 0 ]
        anty_df = self.df[self.df["Biased"] == 1 ]
        return non_anty_df, anty_df

    def sum_by_category(self):
        """ count the sum of values per column """
        antisemitism_tweet = self.df.groupby("Biased", observed=False).size()
        # antisemitism_tweet = self.df["Biased"].value_counts()
        return antisemitism_tweet

    def set_len_column(self):
        """ set new column in df holding the length of the text column """
        self.df['length'] = self.df['Text'].str.len()

    def average_len_of_tweet(self):
        """ check the average length of all the tweets """
        series_to_check = self.df["Text"]
        sum_len = 0
        for raw in series_to_check:
            sum_len += len(str(raw).split(' '))
        average_len = sum_len / series_to_check.size
        return average_len

    def average_by_category(self):
        """ return the average length of each value """
        lengths = []
        for df in self.sub_df:
            average_len = sum(df['length'])/ df.size
            lengths.append(average_len)
        print(pd.Series(lengths))
        return pd.Series(lengths)

    def three_longest_tweets(self):
        """ return the 3 longest tweets per category """
        tweets =[]
        for df in self.sub_df:
            tree_longest = df.sort_values(by= "length", ascending=False).head(3)
            tweets.append(tree_longest)
        return pd.Series(tweets).values

    def find_ten_most_common_words(self):
        """ return the 10 most common word across all the tweets """
        words = "".join(self.df["Text"].str.lower()).split()
        return pd.Series(words).value_counts().head(10)

    def uppercase_words(self):
        """ check uppercase in all tweets """
        upper = self.df['Text'].apply(lambda x: sum(word.isupper() for word in str(x).split()))
        return sum(upper)

    def uppercase_by_category(self):
        """ check uppercase in each df """
        sum_upper = []
        for df in self.sub_df:
            upper = df['Text'].apply(lambda x: sum(word.isupper() for word in str(x).split()))
            sum_upper.append(sum(upper))
        return pd.Series(sum_upper)


l = Loader("../data/tweets_dataset.csv")
explor = ExploreData(l.df)
print(explor.uppercase_by_category())
