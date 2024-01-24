import pytest
import os
from src import func


@pytest.mark.parametrize("ipath, expected", [
    ('/home/rust/PycharmProjects/coursework3/operations.json', True),
    ('/home/rust/PycharmProjects/coursework3/text.txt', False),
    ('/home/rust/PycharmProjects/coursework3/operations111.json', False)
])


def test_read_file(ipath, expected):
    result = func.read_file(ipath)  # Чтение файла через функцию
    assert (result is not None) == expected


'''
def test read_file(input, expected):
    assert input * input == expected
'''