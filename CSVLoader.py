import pandas as pd

from com.bridgelabz.census.CSVLoaderInterface import CSVLoaderInterface
from com.bridgelabz.census.Csv_header import IndiaCensusCSV
from com.bridgelabz.census.census_analyzer_error import CensusAnalyserError
from com.bridgelabz.census.state_csv_header import StateCSVHeader


class CSVFileLoader(CSVLoaderInterface):

    def record_counter_in_csv(self):
        """
        counts record in csv file
        :return: return number of records
        """
        try:
            path = self.path
            col_names = repr(self.header).split(",")
            data = pd.read_csv(path, usecols=col_names)
            return len(data)
        except FileNotFoundError:
            raise CensusAnalyserError("Wrong path given")
        except ValueError:
            raise CensusAnalyserError("Delimiter is wrong or Header is wrong")


if __name__ == "__main__":

    census_csv = CSVFileLoader(IndiaCensusCSV(), "/Users/LENOVO/PycharmProjects/census_analysis/com/bridgelabz/census/data/IndiaStateCensusData.csv")
    state_csv = CSVFileLoader(StateCSVHeader(), "/Users/LENOVO/PycharmProjects/census_analysis/com/bridgelabz/census/data/IndiaStateCode.csv")
    print(census_csv.record_counter_in_csv())
    print(state_csv.record_counter_in_csv())
