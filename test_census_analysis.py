import json

import pytest

from com.bridgelabz.census.Census_analyzer_exception import CensusAnalyserError
from com.bridgelabz.census.CSVReader import CSVFileLoader, CSVFileReader
from com.bridgelabz.census.CSV_header import IndiaCensusCSV
from com.bridgelabz.census.StateCSVHeader import StateCSVHeader

CENSUS_CSV_FILE_PATH = "/Users/LENOVO/PycharmProjects/census_analysis/com/bridgelabz/census/data/IndiaStateCensusData.csv"
STATE_CODE_CSV_FILE_PATH = "/Users/LENOVO/PycharmProjects/census_analysis/com/bridgelabz/census/data/IndiaStateCode.csv"
CSV_WRONG_FILE_PATH = "CSVFile/IndiaStateCensusData.csv"
CSV_WRONG_FILE_TYPE = "/Users/LENOVO/PycharmProjects/census_analysis/com/bridgelabz/census/data/IndiaStateCensusData.pdf"
CENSUS_CSV_WRONG_HEADER = "/Users/LENOVO/PycharmProjects/census_analysis/com/bridgelabz/census/data/IndiaStateCensusData_WrongHeader.csv"
STATE_CODE_CSV_WRONG_HEADER = "/Users/LENOVO/PycharmProjects/census_analysis/com/bridgelabz/census/data/IndiaStateCode_WrongHeader.csv"
CENSUS_CSV_WRONG_DELIMITER = "/Users/LENOVO/PycharmProjects/census_analysis/com/bridgelabz/census/data/IndiaStateCensusDataSpace.csv"
STATE_CODE_CSV_WRONG_DELIMITER = "/Users/LENOVO/PycharmProjects/census_analysis/com/bridgelabz/census/data/IndiaStateCodeSemicolon.csv"


@pytest.fixture
def census_csv_file():
    csv_file = CSVFileLoader(IndiaCensusCSV(), CENSUS_CSV_FILE_PATH)
    census_csv_file = CSVFileReader(csv_file)
    return census_csv_file


@pytest.fixture
def state_csv_file():
    csv_file = CSVFileLoader(StateCSVHeader(), STATE_CODE_CSV_FILE_PATH)
    state_csv_file = CSVFileReader(csv_file)
    return state_csv_file

# check if given path, file type, delimiter and header is correct or not


@pytest.mark.parametrize("header,path,expected", [
    (IndiaCensusCSV(), CSV_WRONG_FILE_TYPE, CensusAnalyserError),
    (StateCSVHeader(), CSV_WRONG_FILE_TYPE, CensusAnalyserError),
    (IndiaCensusCSV(), CSV_WRONG_FILE_PATH, CensusAnalyserError),
    (StateCSVHeader(), CSV_WRONG_FILE_PATH, CensusAnalyserError),
    (IndiaCensusCSV(), CENSUS_CSV_WRONG_DELIMITER, CensusAnalyserError),
    (StateCSVHeader(), STATE_CODE_CSV_WRONG_DELIMITER, CensusAnalyserError),
    (IndiaCensusCSV(), CENSUS_CSV_WRONG_HEADER, CensusAnalyserError),
    (StateCSVHeader(), STATE_CODE_CSV_WRONG_HEADER, CensusAnalyserError),
])
def test_givenCSVFile_WhenLoaded_ShouldHaveCorrectPathTypeHeaderAndDelimiter(header, path, expected):
    with pytest.raises(expected):
        csv = CSVFileLoader(header, path)
        csv.load_csv()

# check if length of record is same or not in given csv file


@pytest.mark.parametrize("header,path, expected", [
    (IndiaCensusCSV(), CENSUS_CSV_FILE_PATH, 29),
    (StateCSVHeader(), STATE_CODE_CSV_FILE_PATH, 37),
])
def test_givenCSVFile_WhenCounted_ShouldReturnRecordsCount(header, path, expected):
    csv = CSVFileLoader(header, path)
    csv_file = CSVFileReader(csv)
    assert csv_file.record_counter_in_csv() == expected

# check if IndiaCensusData.csv file is sorted or not


def test_givenIndiaCensusCSVFile_WhenSorted_IfNot_ShouldRaiseCustomException(census_csv_file):
    data = json.loads(census_csv_file.sort_data_in_csv("State"))
    if list(data.keys())[0] != "Andhra Pradesh" and list(data.keys())[len(data)-1] != "West Bengal":
        raise CensusAnalyserError("File is not sorted!!!")

# check if IndiaStateCode.csv file is sorted or not


def test_givenStateCodeCSV_WhenSorted_IfNot_ShouldRaiseCustomException(state_csv_file):
    data = json.loads(state_csv_file.sort_data_in_csv("StateCode"))
    if list(data.get(list(data.keys())[0]))[3] != "AD" and list(data.get(list(data.keys())[len(data) - 1]))[3] != "WB":
        raise CensusAnalyserError("File is not sorted")


# check if IndiaStateCode.csv file is sorted or not according to population from most to least


def test_givenStateCodeCSV_WhenSortedAccordingToPopulation_IfNot_ShouldRaiseCustomException(census_csv_file):
    data = json.loads(census_csv_file.sort_data_in_csv("Population"))
    if list(data.keys())[0] != "Uttar Pradesh" and list(data.keys())[len(data) - 1] != "Sikkim":
        raise CensusAnalyserError("File is not sorted")


# check if IndiaStateCode.csv file is sorted or not according to population density from most to least


def test_givenStateCodeCSV_WhenSortedAccordingToDensity_IfNot_ShouldRaiseCustomException(census_csv_file):
    data = json.loads(census_csv_file.sort_data_in_csv("DensityPerSqKm"))
    if list(data.keys())[0] != "Bihar" and list(data.keys())[len(data) - 1] != "Arunachal Pradesh":
        raise CensusAnalyserError("File is not sorted")


# check if IndiaStateCode.csv file is sorted or not according to largest area to smallest


def test_givenStateCodeCSV_WhenSortedAccordingToArea_IfNot_ShouldRaiseCustomException(census_csv_file):
    data = json.loads(census_csv_file.sort_data_in_csv("AreaInSqKm"))
    if list(data.keys())[0] != "Rajasthan" and list(data.keys())[len(data) - 1] != "Goa":
        raise CensusAnalyserError("File is not sorted")
