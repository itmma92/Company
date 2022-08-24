"""Модуль для расчета параметров"""

from database import list_of_employees, NDFL, CONTRIBUTIONS_TO_FUNDS


def create_list_of_names():
    """создание списка имен по предприятию"""
    list_of_names = [item['name'] for item in list_of_employees]
    return(list_of_names)

def create_list_wages_after_tax():
    """создание списка: заработная плата после вычета налогов"""
    list_wages_after_tax =[item['wage'] for item in list_of_employees]
    return(list_wages_after_tax)

def create_list_id_of_employees():
    """создание списка: id работников"""
    list_id_of_employees = [item['id'] for item in list_of_employees]
    return(list_id_of_employees)

def create_sum_wages_employees():
    """сумма заработной платы по предприятию после вычета налогов"""
    sum_wages_employees = sum(create_list_wages_after_tax())
    return(sum_wages_employees)

def fot():
    """сумма заработной платы по предприятию с учетом налогов"""
    sum_of_fot = create_sum_wages_employees()*CONTRIBUTIONS_TO_FUNDS+create_sum_wages_employees()
    return(sum_of_fot)

def create_sum_of_contributions_to_funds():
    """сумма взносов с заработной платы по предприятию"""
    sum_of_contributions_to_funds = create_sum_wages_employees()*CONTRIBUTIONS_TO_FUNDS
    return(sum_of_contributions_to_funds)

def crate_sum_of_ndfl():
    """сумма НДФЛ с заработной платы работников по предприятию"""
    sum_of_ndfl = create_sum_wages_employees()*NDFL
    return(sum_of_ndfl)

def calculate_max_wage():
    """максимальная заработная плата на руки по предприятию"""
    max_wage = max(create_list_wages_after_tax())
    return(max_wage)

def calculate_min_wage():
    """минимальная заработная плата на руки по предприятию"""
    min_wage = min(create_list_wages_after_tax())
    return(min_wage)

def calculate_medium_wage():
    """нахождение средней заработной платы по предприятию"""
    medium_wage = create_sum_wages_employees()/max(create_list_id_of_employees())
    return(medium_wage)

def create_list_of_names_and_wage():    #разобраться в ВС
    """создание списков работников с заработной платой"""
    global list_of_names_and_wage
    for name,wage in zip(create_list_of_names(),create_list_wages_after_tax()):
        list_of_names_and_wage = (name,wage)
    return(list_of_names_and_wage)

def create_list_of_names_and_ndfl():    #разобраться в ВС
    """создание списков работников с НДФЛ по каждому работнику"""
    global list_of_names_and_ndfl
    for name,wage in zip(create_list_of_names(),create_list_wages_after_tax()):
        list_of_names_and_ndfl = (name,wage*NDFL)
    return(list_of_names_and_ndfl)

def create_list_of_names_and_contributions_to_funds():    #разобраться в ВС
    """создание списков работников с взносами в фонды по каждому работнику"""
    global list_of_names_and_contributions_to_funds
    for name,wage in zip(create_list_of_names(),create_list_wages_after_tax()):
        list_of_names_and_contributions_to_funds = (name,wage*CONTRIBUTIONS_TO_FUNDS)
    return(list_of_names_and_contributions_to_funds)
