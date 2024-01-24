import pytest
from datetime import datetime
from src import func


@pytest.mark.parametrize("ipath, expected", [
    ('/home/rust/PycharmProjects/coursework3/operations.json', True),
    ('/home/rust/PycharmProjects/coursework3/text.txt', False),
    ('/home/rust/PycharmProjects/coursework3/operations111.json', False)
])


def test_read_file(ipath, expected):
    result = func.read_file(ipath)  # Чтение файла через функцию
    assert (result is not None) == expected

list1 = [
  {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364"
  },
  {
    "id": 939719570,
    "state": "EXECUTED",
    "date": "2018-06-30T02:08:58.425572"
  },
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041"
  }]


list2 = [
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
    "state": "EXECUTED",
    "date": "2018-06-30T02:08:58.425572"
  }]


@pytest.mark.parametrize("ilist, expected", [
    (list1, sorted(list2, key=lambda x: datetime.strptime(x['date'], "%Y-%m-%dT%H:%M:%S.%f"), reverse=True)),
    (list2, sorted(list2, key=lambda x: datetime.strptime(x['date'], "%Y-%m-%dT%H:%M:%S.%f"), reverse=True)),
    (None, None)
])
def test_sort_on_time(ilist, expected):
    assert func.sort_on_time(ilist) == expected
