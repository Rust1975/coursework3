from func import amount
from func import currency
from func import description
from func import extraction_date
from func import result_from
from func import result_to


def output_to_screen(idate=None, idescription=None, iresult_from=None,
                     iresult_to=None, iamount=None, icurrency=None):
    """Функция выводит последние пять успешно выполненных операций из списка операций
    """
    if idate is None:
        idate = extraction_date()
    if idate is None:
        return None

    if idescription is None:
        idescription = description()
    if idescription is None:
        return None

    if iresult_from is None:
        iresult_from = result_from()
    if iresult_from is None:
        return None

    if iresult_to is None:
        iresult_to = result_to()
    if iresult_to is None:
        return None

    if iamount is None:
        iamount = amount()
    if iamount is None:
        return None

    if icurrency is None:
        icurrency = currency()
    if icurrency is None:
        return None

    for i in range(0, len(idate)):
        print(f"{idate[i]} {idescription[i]}")
        if iresult_from[i] == "":
            print(f"{iresult_to[i]}")
        else:
            print(f"{iresult_from[i]} -> {iresult_to[i]}")
        print(f"{iamount[i]} {icurrency[i]}\n")


output_to_screen()
