import pandas as pd
from com.bridgelabz.census.Csv_header import IndiaCensusCSV
from com.bridgelabz.census.census_analyzer_error import CensusAnalyserError


class CSVLoader:

    def __init__(self, path=""):
        self.path = path

    def record_counter(self):
        """
        counts record in csv file
        :return: return number of records
        """
        try:
            path = self.path
            col_names = repr(IndiaCensusCSV()).split(",")
            data = pd.read_csv(path, usecols=col_names)
            return len(data)
        except FileNotFoundError:
            raise CensusAnalyserError("Wrong path given")
        except ValueError:
            raise CensusAnalyserError("Header is wrong")


# if __name__=="__main__":
#     csv_loader = CSVLoader(path="/Users/LENOVO/PycharmProjects/census_analysis/com/bridgelabz/census/data/IndiaStateCensusData.csv")
#     print(csv_loader.record_counter())