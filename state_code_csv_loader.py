import pandas as pd
from com.bridgelabz.census.state_csv_header import StateCSVHeader
from com.bridgelabz.census.census_analyzer_error import CensusAnalyserError

class state_code_csv_loader:
    def __init__(self, path=""):
        self.path = path

    def record_counter_in_state_csv(self):
        """
        counts record in state csv file
        :return: return number of records
        """
        try:
            path = self.path
            col_names = repr(StateCSVHeader()).split(",")
            data = pd.read_csv(path, usecols=col_names)
            return len(data)
        except FileNotFoundError:
            raise CensusAnalyserError("Wrong path given")
        except ValueError:
            raise CensusAnalyserError("Header is wrong")


if __name__ == "__main__":
    csv_loader_state = state_code_csv_loader(path="/Users/LENOVO/PycharmProjects/census_analysis/com/bridgelabz/census/data/IndiaStateCode.csv")
    print("state - "+str(csv_loader_state.record_counter_in_state_csv()))
