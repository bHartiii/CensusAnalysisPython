import json

from pandas.io.json import to_json

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

    def sort_data_in_csv(self, sorting_key):
        """
        sorts csv data according to sorting key
        :return:sorted data in json format
        """
        data_dict = {}
        asc = True
        if sorting_key == "Population":
            asc = False
        data = self.main.load_csv().sort_values(sorting_key, ascending=asc)
        for x in data.values:
            data_list = list(x)
            data_dict[data_list[0]] = data_list
        return json.dumps(data_dict)


if __name__ == "__main__":
    census_csv = CSVFileLoader(IndiaCensusCSV(), "/Users/LENOVO/PycharmProjects/census_analysis/com/bridgelabz/census/data/IndiaStateCensusData.csv")
    csv = CSVFileReader(census_csv)
    print(csv.sort_data_in_csv("Population"))
