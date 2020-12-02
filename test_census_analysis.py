import pytest

from com.bridgelabz.census.census_analyzer_error import CensusAnalyserError
from com.bridgelabz.census.csv_generator import CSVGenerator
from com.bridgelabz.census.CSVLoader import CSVFileLoader
from com.bridgelabz.census.csv_generator import CSVGenerator
from com.bridgelabz.census.Csv_header import IndiaCensusCSV
from com.bridgelabz.census.state_csv_header import StateCSVHeader


CENSUS_CSV_FILE_PATH = "/Users/LENOVO/PycharmProjects/census_analysis/com/bridgelabz/census/data/IndiaStateCensusData.csv"
CENSUS_STATE_CSV_FILE_PATH = "/Users/LENOVO/PycharmProjects/census_analysis/com/bridgelabz/census/data/IndiaStateCode.csv"

CENSUS_CSV_WRONG_FILE_PATH = "CSVFile/IndiaStateCensusData.csv"
CENSUS_CSV_WRONG_FILE_TYPE = "/Users/LENOVO/PycharmProjects/census_analysis/com/bridgelabz/census/data/IndiaStateCensusData.pdf"
CENSUS_CSV_WRONG_DELIMITER = "/Users/LENOVO/PycharmProjects/census_analysis/com/bridgelabz/census/data/IndiaStateCensusDataSpace.csv"
CENSUS_CSV_WRONG_STATE_CSV_DELIMITER = "/Users/LENOVO/PycharmProjects/census_analysis/com/bridgelabz/census/data/IndiaStateCodeSemicolon.csv"


# check if length of record is same or not


def test_record_counter():
    csv = CSVGenerator(IndiaCensusCSV(), CENSUS_CSV_FILE_PATH)
    csv_loader = CSVFileLoader()
    csv_loader.generateCSV(csv.header, csv.path)
    assert csv_loader.record_counter_in_csv() == 29

# check if length of record in state csv file is same or not


def test_record_counter_in_state_csv():
    csv = CSVGenerator(StateCSVHeader(), CENSUS_STATE_CSV_FILE_PATH)
    csv_loader = CSVFileLoader()
    csv_loader.generateCSV(csv.header, csv.path)
    assert csv_loader.record_counter_in_csv() == 37

# check if file path is correct or not


def test_raises_exception_on_wrong_file():
    with pytest.raises(CensusAnalyserError):
        csv = CSVGenerator(IndiaCensusCSV(), CENSUS_CSV_WRONG_FILE_PATH)
        csv_loader = CSVFileLoader()
        csv_loader.generateCSV(csv.header, csv.path)
        csv_loader.record_counter_in_csv()

# check if state csv file is right or not


def test_raises_exception_on_wrong_state_file():
    with pytest.raises(CensusAnalyserError):
        csv = CSVGenerator(StateCSVHeader(), CENSUS_CSV_WRONG_FILE_PATH)
        csv_loader = CSVFileLoader()
        csv_loader.generateCSV(csv.header, csv.path)
        csv_loader.record_counter_in_csv()

# check if file type is right or not


def test_raises_exception_on_wrong_file_type():
    with pytest.raises(CensusAnalyserError):
        csv = CSVGenerator(IndiaCensusCSV(), CENSUS_CSV_WRONG_FILE_TYPE)
        csv_loader = CSVFileLoader()
        csv_loader.generateCSV(csv.header, csv.path)
        csv_loader.record_counter_in_csv()

# check if state csv file type is right or not


def test_raises_exception_on_wrong_state_file_type():
    with pytest.raises(CensusAnalyserError):
        csv = CSVGenerator(StateCSVHeader(), CENSUS_CSV_WRONG_FILE_TYPE)
        csv_loader = CSVFileLoader()
        csv_loader.generateCSV(csv.header, csv.path)
        csv_loader.record_counter_in_csv()

# check if delimiter is right or not


def test_raises_exception_on_wrong_delimiter():
    with pytest.raises(CensusAnalyserError):
        csv = CSVGenerator(IndiaCensusCSV(), CENSUS_CSV_WRONG_DELIMITER)
        csv_loader = CSVFileLoader()
        csv_loader.generateCSV(csv.header, csv.path)
        csv_loader.record_counter_in_csv()

# check if delimiter in state csv is right or not


def test_raises_exception_on_wrong_delimiter_in_state_csv():
    with pytest.raises(CensusAnalyserError):
        csv = CSVGenerator(StateCSVHeader(), CENSUS_CSV_WRONG_STATE_CSV_DELIMITER)
        csv_loader = CSVFileLoader()
        csv_loader.generateCSV(csv.header, csv.path)
        csv_loader.record_counter_in_csv()

# check if file header is right or not


def test_raises_exception_on_wrong_header():
    with pytest.raises(CensusAnalyserError):
        csv = CSVGenerator(IndiaCensusCSV(), CENSUS_STATE_CSV_FILE_PATH)
        csv_loader = CSVFileLoader()
        csv_loader.generateCSV(csv.header, csv.path)
        csv_loader.record_counter_in_csv()

# check if state csv file header is right or not


def test_raises_exception_on_state_csv_wrong_header():
    with pytest.raises(CensusAnalyserError):
        csv = CSVGenerator(StateCSVHeader(), CENSUS_CSV_FILE_PATH)
        csv_loader = CSVFileLoader()
        csv_loader.generateCSV(csv.header, csv.path)
        csv_loader.record_counter_in_csv()