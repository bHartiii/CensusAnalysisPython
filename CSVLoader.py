import pandas as pd
from com.bridgelabz.census.census_analyzer_error import CensusAnalyserError
from com.bridgelabz.census.csv_generator import CSVGenerator
from com.bridgelabz.census.state_csv_header import StateCSVHeader
from com.bridgelabz.census.Csv_header import IndiaCensusCSV


class CSVFileLoader:
    def __init__(self):
        self.path = None
        self.csv_header = None

    def generateCSV(self, header, path):
        self.path = path
        self.csv_header = header

    def record_counter_in_csv(self):
        """
        counts record in csv file
        :return: return number of records
        """
        try:
            path = self.path
            col_names = repr(self.csv_header).split(",")
            data = pd.read_csv(path, usecols=col_names)
            return len(data)
        except FileNotFoundError:
            raise CensusAnalyserError("Wrong path given")
        except ValueError:
            raise CensusAnalyserError("Delimiter is wrong or Header is wrong")


if __name__ == "__main__":
    census_csv_file = CSVGenerator(IndiaCensusCSV(), "/Users/LENOVO/PycharmProjects/census_analysis/com/bridgelabz/census/data/IndiaStateCensusData.csv")
    state_csv_file = CSVGenerator(StateCSVHeader(), "/Users/LENOVO/PycharmProjects/census_analysis/com/bridgelabz/census/data/IndiaStateCode.csv")
    csv = CSVFileLoader()
    csv.generateCSV(census_csv_file.header, census_csv_file.path)
    print(csv.record_counter_in_csv())
    csv.generateCSV(state_csv_file.header, state_csv_file.path)
    print(csv.record_counter_in_csv())

