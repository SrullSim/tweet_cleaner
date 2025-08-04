import pandas as pd
from cleaner import Cleaner
from data_analyzer import ExploreData

class Reporter(Cleaner):

    def __init__(self, df , column_to_drop, path_to_write_in):
        super().__init__(df,column_to_drop)
        self.df= df
        self.path = path_to_write_in
        self.explore = ExploreData(df)
        self.result  ={}

    def build_the_result_json(self):
        self.result["sum_tweets"] = self.explore.sum_by_category()
        self.result["average_len"] = [self.explore.average_len_of_tweet(),self.explore.average_by_category()]
        self.result["three_longest_tweets"] = self.explore.three_longest_tweets()
        self.result["common_words"] = self.explore.find_ten_most_common_words()
        self.result["uppercase_words"] = [self.explore.uppercase_words(), self.explore.uppercase_by_category()]





    def write_to_result(self, path):
        with open(path, 'a') as res:

            res.write(self.result)

