import json
from datetime import datetime

def read_file():
    """Функция возвращает данные из файла operations.json"""
    with open('/home/rust/PycharmProjects/coursework3/operations.json', 'r', encoding='utf-8') as file:
        file_content = file.read()
        # def output_to_screen():
        return json.loads(file_content)

def sort_on_time():
    """
        Сортировка по ключу 'date'
        Если ключ "date" отсутствует, используется значение по умолчанию "1970-01-01T00:00:00.000".
    """
    json_data_sort = read_file()
    json_data_sort.sort(key=lambda x: datetime.strptime(x.get("date", "1970-01-01T00:00:00.000"),
                                                   "%Y-%m-%dT%H:%M:%S.%f"), reverse=True)
    return json_data_sort


# def output_to_screen():
#
#     operations = json.loads(file)

print(sort_on_time())