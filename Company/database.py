"""База данных со списком работников с параметрами и константы налогов"""

list_of_employees = [
    {'id': int(1), 'name': 'MIkle', 'age': 20, 'wage': float(50_000)},
    {'id': int(2), 'name': 'Max', 'age': 25, 'wage': float(75_000)},
    {'id': int(3), 'name': 'Vitali', 'age': 24, 'wage': float(100_000)},
    {'id': int(4), 'name': 'Liza', 'age': 25, 'wage': float(75_000)},
    {'id': int(5), 'name': 'Vova', 'age': 24, 'wage': float(85_000)}
]
NDFL = 0.13    #ставка НДФЛ 13%
CONTRIBUTIONS_TO_FUNDS = 0.3    # совокупная ставка взносов в ФСС и ПФР 30%
