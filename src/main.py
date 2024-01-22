from func import extraction_date
from func import description
from func import result_from
from func import result_to
from func import amount
from func import currency

def output_to_screen():
    """Функция выводит последние пять успешно выполненных операций из списка операций
    """
    idate = extraction_date()
    idescription = description()
    iresult_from = result_from()
    iresult_to = result_to()
    iamount = amount()
    icurrency = currency()
    for i in range(0, len(idate)):
        print(f"{idate[i]} {idescription[i]}")
        if iresult_from[i] == "":
            print(f"{iresult_to[i]}")
        else:
            print(f"{iresult_from[i]} -> {iresult_to[i]}")
        print(f"{iamount[i]} {icurrency[i]}\n")


output_to_screen()