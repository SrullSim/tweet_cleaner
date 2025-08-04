import pandas as pd

class Loader:

    """ takes a file in scv format and return it
        in DataFrame """

    def __init__(self, path):
        self.df= self.load(path)


    def load(self, path):
        df = pd.read_csv(path)
        return df