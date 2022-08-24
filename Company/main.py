from calculations import fot, crate_sum_of_ndfl, create_sum_of_contributions_to_funds,create_list_id_of_employees

company_profit= float(input('Введите доход компании-'))

def company_information(company_profit):
    """создали функцию company_information, в которую выводится информация о компании"""
    print('1. Сотрудников в компании', max(create_list_id_of_employees()))
    print('2. Фонд оплаты труда=', fot(), 'рублей')
    print('3. Уплатить НДФЛ=', crate_sum_of_ndfl(), 'рубей')
    print('4. Взносов уплатить =', create_sum_of_contributions_to_funds(), 'рублей')
    print('*Чистая прибыль=',company_profit-fot(), 'рублей')

company_information(company_profit)
