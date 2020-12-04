import pandas as pd

from com.bridgelabz.census.census_analyzer_error import CensusAnalyserError


class CSVFileLoader:

    def __init__(self, header, path):
        self.path = path
        self.header = header
        self.col_names = None
        self.data = None

    def load_csv(self):
        """
        loads the csv file and read data
        :return: data
        """
        try:
            self.col_names = repr(self.header).split(",")
            self.data = pd.read_csv(self.path, usecols=self.col_names)
            return self.data
        except FileNotFoundError:
            raise CensusAnalyserError("Wrong path given")
        except ValueError:
            raise CensusAnalyserError("Header is wrong or Delimiter is wrong")