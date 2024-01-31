import json
import os
from datetime import datetime


def read_file(ipath=None):
    """Функция возвращает данные из файла *.json"""
    if ipath is None:
        ipath_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        ipath = os.path.abspath(os.path.join(ipath_dir, "operations.json"))
    try:
        with open(ipath, 'r', encoding='utf-8') as file:
            file_content = file.read()
        return json.loads(file_content)
    except IOError as e:
        print(f"Ошибка при открытии файла: {e}")
        return None
    except ValueError as e:
        print(f"Ошибка при парсинге файла в формат JSON, расположенного по адресу:\n"
              f"{ipath}: {e}")
        return None


def sort_on_time(ipath=None):
    """
        Сортировка по ключу 'date'
        Если ключ "date" отсутствует, используется значение по умолчанию "1970-01-01T00:00:00.000".
    """
    json_data_sort = read_file(ipath)
    if json_data_sort is None:
        return None
    json_data_sort.sort(key=lambda x: datetime.strptime(x.get("date", "1970-01-01T00:00:00.000"),
                                                        "%Y-%m-%dT%H:%M:%S.%f"), reverse=True)
    return json_data_sort


def first_executed_operations(ipath=None, operations=None, up_bounder=None):
    """Функция выводит указанное число первых значений из отсортированного по убыванию списка
       по ключу "state" =+ "EXECUTED"
    """
    if operations is None:
        operations = sort_on_time(ipath)
    if operations is None:
        return None
    if up_bounder is None:
        return None
    result_list = []
    for x in operations:
        item = x
        if item["state"] == "EXECUTED":
            result_list.append(item)
            if len(result_list) == up_bounder:
                break
    return result_list


def extraction_date(operations=None):
    """
        Функция возвращает даты из списка словарей по ключу "date"
    """
    if operations is None:
        operations = first_executed_operations(None, None, 5)
    if operations is None:
        return None
    idate = []
    for x in operations:
        # Применяем метод .strftime к экземпляру класса datetime.fromisoformat(x["date"])
        # и результат добавляем в список idate
        idate.append(datetime.fromisoformat(x["date"]).strftime("%d.%m.%Y"))
    return idate


def description(operations=None):
    """
        Функция возвращает "описание операции" из списка словарей по ключу "description"
    """
    if operations is None:
        operations = first_executed_operations(None, None, 5)
    if operations is None:
        return None
    idescription = []
    for x in operations:
        idescription.append(x["description"])
    return idescription


def result_from(operations=None):
    """
        Функция возвращает откуда переводится, из списка словарей по ключу "from".
        Номер карты замаскирован и не отображается целиком в формате
        XXXX XX** **** XXXX (видны первые 6 цифр и последние 4, разбито
        по блокам по 4 цифры, разделенных пробелом).
    """
    if operations is None:
        operations = first_executed_operations(None, None, 5)
    if operations is None:
        return None
    iresult_from = []
    for x in operations:
        str0 = x.get("from", "")
        if str0 == "":
            iresult_from.append(str0)
        else:
            str1 = str0.split()[-1]  # Цифровая часть строки - хвост
            str2 = str0.replace(str1, "").strip()  # Текстовая часть строки - голова
            str3 = str1[:6] + "******" + str1[12:]
            str4 = " ".join(str3[i:i + 4] for i in range(0, len(str3), 4))
            str0 = str2 + " " + str4
            iresult_from.append(str0)
    return iresult_from


def result_to(operations=None):
    """
        Функция возвращает куда переводится, из списка словарей по ключу "to"
        Номер счета замаскирован и не отображается целиком в формате  **XXXX
        (видны только последние 4 цифры номера счета).
    """
    if operations is None:
        operations = first_executed_operations(None, None, 5)
    if operations is None:
        return None
    iresult_to = []
    for x in operations:
        str0 = x.get("to", "")
        if str0 == "":
            iresult_to.append(str0)
        else:
            str1 = str0.split()[-1]  # цифровая часть строки - хвост
            str2 = str0.replace(str1, "").strip()  # текстовая часть строки - голова
            str3 = "**" + str1[-4:]
            str0 = str2 + " " + str3
            iresult_to.append(str0)
    return iresult_to


def amount(operations=None):
    """
        Функция возвращает сумму первода из списка словарей по ключам "operationAmount" и "amount"
    """
    if operations is None:
        operations = first_executed_operations(None, None, 5)
    if operations is None:
        return None
    iamount = []
    for x in operations:
        iamount.append(x["operationAmount"]["amount"])
    return iamount


def currency(operations=None):
    """
        Функция возвращает валюту перевода из списка словарей по ключам "operationAmount", "currency" и "name"
    """
    if operations is None:
        operations = first_executed_operations(None, None, 5)
    if operations is None:
        return None
    icurrency = []
    for x in operations:
        icurrency.append(x["operationAmount"]["currency"]["name"])
    return icurrency


'''
read_file()
[print(item) for item in first_executed_operations(5)]
[print(item) for item in result_from()]
[print(item) for item in result_to()]
[print(item) for item in amount()]
[print(item) for item in currency()]
print(len(result_from()))
'''