import pytest

from com.bridgelabz.census.Census_analyzer_exception import CensusAnalyserError
from com.bridgelabz.census.CSVReader import CSVFileLoader, CSVFileReader
from com.bridgelabz.census.CSV_header import IndiaCensusCSV
from com.bridgelabz.census.StateCSVHeader import StateCSVHeader


CENSUS_CSV_FILE_PATH = "/Users/LENOVO/PycharmProjects/census_analysis/com/bridgelabz/census/data/IndiaStateCensusData.csv"
CENSUS_STATE_CSV_FILE_PATH = "/Users/LENOVO/PycharmProjects/census_analysis/com/bridgelabz/census/data/IndiaStateCode.csv"

CENSUS_CSV_WRONG_FILE_PATH = "CSVFile/IndiaStateCensusData.csv"
CENSUS_CSV_WRONG_FILE_TYPE = "/Users/LENOVO/PycharmProjects/census_analysis/com/bridgelabz/census/data/IndiaStateCensusData.pdf"
CENSUS_CSV_WRONG_DELIMITER = "/Users/LENOVO/PycharmProjects/census_analysis/com/bridgelabz/census/data/IndiaStateCensusDataSpace.csv"
CENSUS_CSV_WRONG_STATE_CSV_DELIMITER = "/Users/LENOVO/PycharmProjects/census_analysis/com/bridgelabz/census/data/IndiaStateCodeSemicolon.csv"


# check if length of record is same or not


def test_givenIndiaCensusCSVFile_WhenCounted_ShouldReturnRecordsCount():
    csv = CSVFileLoader(IndiaCensusCSV(), CENSUS_CSV_FILE_PATH)
    csv_file = CSVFileReader(csv)
    assert csv_file.record_counter_in_csv() == 29

# check if length of record in state csv file is same or not


def test_givenStateCodeCSVFile_WhenCounted_ShouldReturnRecordsCount():
    csv = CSVFileLoader(StateCSVHeader(), CENSUS_STATE_CSV_FILE_PATH)
    csv_file = CSVFileReader(csv)
    assert csv_file.record_counter_in_csv() == 37

# check if file path is correct or not


def test_givenIndiaCensusCSVFile_WhenLoaded_IfPathIsWrong_ShouldRaiseCustomException():
    with pytest.raises(CensusAnalyserError):
        csv = CSVFileLoader(IndiaCensusCSV(), CENSUS_CSV_WRONG_FILE_PATH)
        csv.load_csv()


# check if state csv file is right or not


def test_givenStateCodeCSVFile_WhenLoaded_IfPathIsWrong_ShouldRaiseCustomException():
    with pytest.raises(CensusAnalyserError):
        csv = CSVFileLoader(StateCSVHeader(), CENSUS_CSV_WRONG_FILE_PATH)
        csv.load_csv()


# check if file type is right or not


def test_givenIndiaCensusCSVFile_WhenLoaded_IfExtensionIsWrong_ShouldRaiseCustomException():
    with pytest.raises(CensusAnalyserError):
        csv = CSVFileLoader(IndiaCensusCSV(), CENSUS_CSV_WRONG_FILE_TYPE)
        csv.load_csv()


# check if state csv file type is right or not


def test_givenStateCodeCSVFile_WhenLoaded_IfExtensionIsWrong_ShouldRaiseCustomException():
    with pytest.raises(CensusAnalyserError):
        csv = CSVFileLoader(StateCSVHeader(), CENSUS_CSV_WRONG_FILE_TYPE)
        csv.load_csv()


# check if delimiter is right or not


def test_givenIndiaCensusCSVFile_WhenLoaded_IfDelimiterIsWrong_ShouldRaiseCustomException():
    with pytest.raises(CensusAnalyserError):
        csv = CSVFileLoader(IndiaCensusCSV(), CENSUS_CSV_WRONG_DELIMITER)
        csv.load_csv()


# check if delimiter in state csv is right or not


def test_givenStateCodeCSVFile_WhenLoaded_IfDelimiterIsWrong_ShouldRaiseCustomException():
    with pytest.raises(CensusAnalyserError):
        csv = CSVFileLoader(StateCSVHeader(), CENSUS_CSV_WRONG_STATE_CSV_DELIMITER)
        csv.load_csv()


# check if file header is right or not


def test_givenIndiaCensusCSVFile_WhenLoaded_IfHeaderIsWrong_ShouldRaiseCustomException():
    with pytest.raises(CensusAnalyserError):
        csv = CSVFileLoader(IndiaCensusCSV(), CENSUS_STATE_CSV_FILE_PATH)
        csv.load_csv()


# check if state csv file header is right or not


def test_givenStateCodeCSVFile_WhenLoaded_IfHeaderIsWrong_ShouldRaiseCustomException():
    with pytest.raises(CensusAnalyserError):
        csv = CSVFileLoader(StateCSVHeader(), CENSUS_CSV_FILE_PATH)
        csv.load_csv()