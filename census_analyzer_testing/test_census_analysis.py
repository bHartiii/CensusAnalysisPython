import json

import pytest

from com.bridgelabz.census_analyzer.census_analyzer_exception import CensusAnalyserError
from com.bridgelabz.census_analyzer.csv_reader import CSVFileLoader, CSVFileReader, CENSUS_CSV_FILE_PATH, STATE_CODE_CSV_FILE_PATH
from com.bridgelabz.census_analyzer.census_csv_header import IndiaCensusCSV
from com.bridgelabz.census_analyzer.state_csv_header import StateCSVHeader

CENSUS_CSV_FILE_PATH = CENSUS_CSV_FILE_PATH
STATE_CODE_CSV_FILE_PATH = STATE_CODE_CSV_FILE_PATH
CSV_WRONG_FILE_PATH = "CSVFile/IndiaStateCensusData.csv"
CSV_WRONG_FILE_TYPE = "/Users/LENOVO/PycharmProjects/census_analysis/com/bridgelabz/data/IndiaStateCensusData.pdf"
CENSUS_CSV_WRONG_HEADER = "/Users/LENOVO/PycharmProjects/census_analysis/com/bridgelabz/data/IndiaStateCensusData_WrongHeader.csv"
STATE_CODE_CSV_WRONG_HEADER = "/Users/LENOVO/PycharmProjects/census_analysis/com/bridgelabz/data/IndiaStateCode_WrongHeader.csv"
CENSUS_CSV_WRONG_DELIMITER = "/Users/LENOVO/PycharmProjects/census_analysis/com/bridgelabz/data/IndiaStateCensusDataSpace.csv"
STATE_CODE_CSV_WRONG_DELIMITER = "/Users/LENOVO/PycharmProjects/census_analysis/com/bridgelabz/data/IndiaStateCodeSemicolon.csv"

CENSUS_ANALYZER_CUSTOM_EXCEPTION = CensusAnalyserError("File is not sorted")


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


# check if IndiaCensusData.csv file is sorted and first row is matched or not
@pytest.mark.parametrize("sorting_key, list_element, expected", [
    ("State", "Andhra Pradesh", CENSUS_ANALYZER_CUSTOM_EXCEPTION),
    ("Population", "Uttar Pradesh", CENSUS_ANALYZER_CUSTOM_EXCEPTION),
    ("DensityPerSqKm", "Bihar", CENSUS_ANALYZER_CUSTOM_EXCEPTION),
    ("AreaInSqKm", "Rajasthan", CENSUS_ANALYZER_CUSTOM_EXCEPTION),
])
def test_givenIndiaCensusCSVFile_WhenSorted_IfFirstRowIsNotMatched_ShouldRaiseCustomException(census_csv_file,
                                                                                              sorting_key, list_element, expected):
    data = json.loads(census_csv_file.sort_data_in_csv(sorting_key))
    if list(data.keys())[0] != list_element:
        raise expected


# check if IndiaCensusData.csv file is sorted and last row is matched or not
@pytest.mark.parametrize("sorting_key, list_element, expected", [
    ("State", "West Bengal", CENSUS_ANALYZER_CUSTOM_EXCEPTION),
    ("Population", "Sikkim", CENSUS_ANALYZER_CUSTOM_EXCEPTION),
    ("DensityPerSqKm", "Arunachal", CENSUS_ANALYZER_CUSTOM_EXCEPTION),
    ("AreaInSqKm", "Goa", CENSUS_ANALYZER_CUSTOM_EXCEPTION),
])
def test_givenIndiaCensusCSVFile_WhenSorted_IfLastRowIsNotMatched_ShouldRaiseCustomException(census_csv_file, sorting_key,list_element, expected):
    data = json.loads(census_csv_file.sort_data_in_csv(sorting_key))
    if list(data.keys())[-1] != list_element:
        raise expected


# check if IndiaStateCode.csv file is sorted or not
def test_givenStateCodeCSV_WhenSorted_IfFirstRowNotMatched_ShouldRaiseCustomException(state_csv_file):
    data = json.loads(state_csv_file.sort_data_in_csv("StateCode"))
    if list(data.get(list(data.keys())[0]))[3] != "AD":
        raise CENSUS_ANALYZER_CUSTOM_EXCEPTION


# check if IndiaStateCode.csv file is sorted or not
def test_givenStateCodeCSV_WhenSorted_IfLastRowNotMatched_ShouldRaiseCustomException(state_csv_file):
    data = json.loads(state_csv_file.sort_data_in_csv("StateCode"))
    if list(data.get(list(data.keys())[-1]))[3] != "WB":
        raise CENSUS_ANALYZER_CUSTOM_EXCEPTION
