# # year = int(input('Введите нужный год: '))
# # if (year % 4 == 0):
# #     print('Год високосный')
# # if (year % 4 != 0):
# #     print('Год не високосный')

year = int(input('Введите нужный год: '))
def is_year_leap(year):
 if (year % 4 == 0):
    return True
 else:
    return False
x = is_year_leap(year)
print(f"год {year}: {x}")
    


    