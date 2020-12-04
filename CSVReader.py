from com.bridgelabz.census.CSV_header import IndiaCensusCSV
from com.bridgelabz.census.StateCSVHeader import StateCSVHeader
from com.bridgelabz.census.CSVFileLoader import CSVFileLoader


class CSVFileReader:

    def __init__(self, obj):
        self.main = obj

    def record_counter_in_csv(self):
        """
        counts record in csv file
        :return: return number of records
        """
        return len(self.main.load_csv())



