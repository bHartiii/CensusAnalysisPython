from com.bridgelabz.census.Csv_header import IndiaCensusCSV
from com.bridgelabz.census.state_csv_header import StateCSVHeader
from com.bridgelabz.census.CSVFileLoader import CSVFileLoader


class CSVFileReader(object):

    def __init__(self, obj):
        self.main = obj

    def record_counter_in_csv(self):
        """
        counts record in csv file
        :return: return number of records
        """
        return len(self.main.load_csv())


if __name__ == "__main__":
    census_csv = CSVFileLoader(IndiaCensusCSV(),
                               "/Users/LENOVO/PycharmProjects/census_analysis/com/bridgelabz/census/data/IndiaStateCensusData.csv")
    state_csv = CSVFileLoader(StateCSVHeader(),
                              "/Users/LENOVO/PycharmProjects/census_analysis/com/bridgelabz/census/data/IndiaStateCode.csv")

    census_csv_file = CSVFileReader(census_csv)
    state_csv_file = CSVFileReader(state_csv)
    print(census_csv_file.record_counter_in_csv())
    print(state_csv_file.record_counter_in_csv())
