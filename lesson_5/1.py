# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
# Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

from collections import namedtuple


Company = namedtuple(
    'Company', 'name profit_1 profit_2 profit_3 profit_4 profit_average')

company_count = int(input('Input count company: '))

companys = []
for x in range(0, company_count):
    name = input('Input name company: ')
    p1 = int(input('Input profit for 1 quarter: '))
    p2 = int(input('Input profit for 2 quarter: '))
    p3 = int(input('Input profit for 3 quarter: '))
    p4 = int(input('Input profit for 4 quarter: '))
    profit_average = (p1 + p2 + p3 + p4) / 4
    company = Company(name, p1, p2, p3, p4, profit_average)
    companys.append(company)

all_profit_average = 0
for x in range(0, company_count):
    all_profit_average = all_profit_average + companys[x].profit_average

all_profit_average = all_profit_average / company_count

print('Lists companys with profit more average: ')
for x in range(0, company_count):
    if (companys[x].profit_average > all_profit_average):
        print(companys[x].name)

print('Lists companys with profit less average: ')
for x in range(0, company_count):
    if (companys[x].profit_average < all_profit_average):
        print(companys[x].name)
