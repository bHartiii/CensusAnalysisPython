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

# check if file path is correct or not


def test_raises_exception_on_wrong_file():
    with pytest.raises(CensusAnalyserError):
        csv_loader = CSVLoader(CENSUS_CSV_WRONG_FILE_PATH)
        csv_loader.record_counter()

# check if file type is right or not


def test_raises_exception_on_wrong_file_type():
    with pytest.raises(CensusAnalyserError):
        csv_loader = CSVLoader(CENSUS_CSV_WRONG_FILE_TYPE)
        csv_loader.record_counter()