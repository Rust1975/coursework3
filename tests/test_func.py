import pytest
from src import func

'''
@pytest.mark.parametrize("input, expected", [
    (5, 25),
    (7, 49),
    (8, 64),
])
'''
def test read_file(input, expected):
    assert input * input == expected

def test_read_file():
    try:
        with open('/home/rust/PycharmProjects/coursework3/operations.json', 'r', encoding='utf-8') as file:
            file_content = file.read()
    except IOError as e:
        pytest.fail(f"Ошибка при открытии файла: {e}")