import pytest
from datetime import datetime
from src import func


@pytest.mark.parametrize("ipath, expected", [
    ("C:/Users/homepc/PycharmProjects/coursework3/operations.json", True),
    ("C:/Users/homepc/PycharmProjects/coursework3/text.txt", False),
    ("C:/Users/homepc/PycharmProjects/coursework3/operations111.json", False)
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

# @pytest.mark.parametrize("ipath, operations, up_bounder, expected", [
#     (list3, 3, list3.remove[{"id": 41428829,"state": "CANCELED","date": "2019-07-03T18:35:29.512364"}])
# ])
def test_first_executed_operations():
    assert func.first_executed_operations(ipath1, None, 1)[0] == list1[0]
    assert func.first_executed_operations(ipath1, None, 3) == list1[:2]

