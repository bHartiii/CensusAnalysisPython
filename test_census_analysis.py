import pytest

from com.bridgelabz.census.census_analyzer_error import CensusAnalyserError
from com.bridgelabz.census.census_analyzer import CSVLoader


CENSUS_CSV_FILE_PATH = "/Users/LENOVO/PycharmProjects/census_analysis/com/bridgelabz/census/data/IndiaStateCensusData.csv"
CENSUS_CSV_WRONG_FILE_PATH = "CSVFile/IndiaStateCensusData.csv"
CENSUS_CSV_WRONG_FILE_TYPE = "/Users/LENOVO/PycharmProjects/census_analysis/com/bridgelabz/census/data/IndiaStateCensusData.pdf"
CENSUS_CSV_WRONG_DELIMITER = "/Users/LENOVO/PycharmProjects/census_analysis/com/bridgelabz/census/data/IndiaStateCensusDataSpace.csv"


# check if length of record is same or not


def test_record_counter():
    csv_loader = CSVLoader(CENSUS_CSV_FILE_PATH)
    assert csv_loader.record_counter() == 29

