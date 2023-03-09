d1 = dict()
print(f"d1: {d1}")
print(f"type(d1): {type(d1)}")
caps = {'NC': 'Raleigh', 'VA': 'Richmond', 'WI': 'Madison', 'NJ': 'Trenton'}
caps['OH'] = "Columbus"
caps['OR'] = "Salem"
print(f"caps: {caps}")

airports = {
    'EWR': 'Newark',
    'YYZ': 'Toronto',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'LTN': 'London',  # (Luton)
    'LGW': 'London',  # (Gatwick)
    'LHR': 'London',  # (Heathrow)
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'YCC': 'Calgary',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'YOW': 'Ottawa',
    'IAD': 'Dulles',
}

print(f"airports['RDU']: {airports['RDU']}")
print(f"airports['MCO']: {airports['MCO']}")

code = 'CMH'
if code in airports:
    print(f"airports['CMH']: {airports['CMH']}")

print(f"airports.get('YCC'): {airports.get('YCC')}")

print(f"airports.get('CMH'): {airports.get('CMH')}")
print(f"airports.get('CMH', 'not found'): {airports.get('CMH', 'not found')}")

print(f"airports.setdefault('RDU', 'Durham'): {airports.setdefault('RDU', 'Durham')}")

print(f"airports.setdefault('CMH', 'Columbus'): {airports.setdefault('CMH', 'Columbus')}")

print(f"airports: {airports}")

for code, city in airports.items():
    print(code, city)
print('-' * 60)
print(f"airports.items(): {airports.items()}")

