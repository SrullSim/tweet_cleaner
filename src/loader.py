import pandas as pd

class Loader:

    def __init__(self, path):
        self.df= self.load(path)


    def load(self, path):
        df = pd.read_csv(path)
        return df