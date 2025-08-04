from string import punctuation
import pandas as pd
from numpy.matlib import empty
# from pandas import DataFrame
from pprint import pprint
from loader import Loader


class Cleaner:

    def __init__(self, df, column_to_drop):
        self.original_df = df
        self.df= df.copy()
        self.columns_to_drop = column_to_drop
        self.clean_uninteresting()
        self.replace_to_lower()
        self.replace_punctuation_marks()
        # self.empty_cell()


    def clean_uninteresting(self):
        """ drop the columns who not useful (not change the original df)"""
        for col in self.columns_to_drop:
            self.df.drop(col, axis=1, inplace=True)

    def replace_punctuation_marks(self):
        self.df['Text'] = self.df['Text'].str.replace(f"[{punctuation}]","",regex = True)


    def replace_to_lower(self):
        self.df['Text'] = self.df['Text'].str.lower()

    # def empty_cell(self):
    #     self.df = self.df.drop()






#
# cols = ['TweetID']
# l = Loader("../data/tweets_dataset.csv")
# c = Cleaner(l.df, cols)
# pprint(c.df["Text"])
# c.replace_punctuation_marks()
# # c.empty_cell()
#
# pprint(c.df["Text"])
