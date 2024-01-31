import pytest
import os
from src import func

ipath_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


@pytest.mark.parametrize("ipath, expected", [
    # ("C:/Users/homepc/PycharmProjects/coursework3/operations.json", True),
    # ("C:/Users/homepc/PycharmProjects/coursework3/text.txt", False),
    # ("C:/Users/homepc/PycharmProjects/coursework3/operations111.json", False)
    (os.path.abspath(os.path.join(ipath_dir, "operations.json")), True),
    (os.path.abspath(os.path.join(ipath_dir, "text.txt")), False),
    (os.path.abspath(os.path.join(ipath_dir, "operations111.json")), False)
])
def test_read_file(ipath, expected):
    result = func.read_file(ipath)  # Чтение файла через функцию
    assert (result is not None) == expected


list1 = [
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041"
  },
  {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364"
  },
  {
    "id": 939719570,
    "state": "CANCELED",
    "date": "2018-06-30T02:08:58.425572"
  }]

ipath1 = "C:/Users/homepc/PycharmProjects/coursework3/tst.json"


def test_sort_on_time():
    assert func.sort_on_time(ipath1) == list1
    assert len(func.sort_on_time(None)) == 101


def test_first_executed_operations():
    assert func.first_executed_operations(ipath1, None, 1)[0] == list1[0]
    assert func.first_executed_operations(ipath1, None, 3) == list1[:2]


def test_extraction_date():
    assert func.extraction_date(None) == ['08.12.2019', '07.12.2019', '19.11.2019', '13.11.2019', '05.11.2019']
    result = func.first_executed_operations(ipath1, None, 5)
    assert func.extraction_date(result) == ['26.08.2019', '03.07.2019']


def test_description():
    assert func.description(None) == ['Открытие вклада', 'Перевод организации', 'Перевод организации',
                                      'Перевод со счета на счет', 'Открытие вклада']
    result = func.first_executed_operations(None, None, 2)
    assert func.description(result) == ['Открытие вклада', 'Перевод организации']


def test_result_from():
    assert func.result_from(None) == ['', 'Visa Classic 2842 87** **** 9012', 'Maestro 7810 84** **** 5568',
                                      'Счет 3861 14** **** 5566 9794', '']
    result = func.first_executed_operations(None, None, 2)
    assert func.result_from(result) == ['', 'Visa Classic 2842 87** **** 9012']


def test_result_to():
    assert func.result_to(None) == ['Счет **5907', 'Счет **3655', 'Счет **2869', 'Счет **8125', 'Счет **8381']
    result = func.first_executed_operations(None, None, 2)
    assert func.result_to(result) == ['Счет **5907', 'Счет **3655']


def test_amount():
    assert func.amount(None) == ['41096.24', '48150.39', '30153.72', '62814.53', '21344.35']
    result = func.first_executed_operations(None, None, 2)
    assert func.amount(result) == ['41096.24', '48150.39']


def test_currency():
    assert func.currency(None) == ['USD', 'USD', 'руб.', 'руб.', 'руб.']
    result = func.first_executed_operations(None, None, 2)
    assert func.currency(result) == ['USD', 'USD']
