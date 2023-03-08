
list1 = list()  # empty list
print(f"list1: {list1}")
print(f"type(list1): {type(list1)}")
list2 = [1, 2, 3]
list3 = ['alpha', 'bravo', 'charlie']
list4 = [5, 'bravo', True, [8, 9, 10]]
list5 = []

cities = ["Paris", "Columbus", "Little Elm", "Mumbai"]
print(f"cities: {cities}")
print(f"cities[0]: {cities[0]}")
print(f"len(cities): {len(cities)}")

cities.insert(0, "Jacksonville")
print(f"cities: {cities}")
cities.insert(3, "Chicago")
print(f"cities: {cities}")

cities.append("Constantinople")
cities.append("Durham")
print(f"cities: {cities}")
print(f"len(cities): {len(cities)}")

more_cities = ["Bangalore", "Tampa", "Los Angeles"]

print(f"len(cities): {len(cities)}")

cities.append(more_cities)
print(f"len(cities): {len(cities)}")

print(f"cities: {cities}")
print(f"cities[-1]: {cities[-1]}")

cities.extend(more_cities)
print(f"cities: {cities}")
print(f"len(cities): {len(cities)}")

# LIST.insert(pos, obj)   LIST.append(obj)   LIST.extend(iterable)

del cities[8]
print(f"cities: {cities}")

cities.remove('Chicago')
print(f"cities: {cities}")

city = cities.pop()
print(f"city: {city}")
print(f"cities: {cities}")

city = cities.pop(0)
print(f"city: {city}")
print(f"cities: {cities}")

#  del LIST[pos]   LIST.remove(value)   LIST.pop(pos=-1)

print(f"cities[0]: {cities[0]}")
print(f"cities[7]: {cities[7]}")
print(f"cities[-1]: {cities[-1]}")

#  [start:stop]  [:stop]   [start:]  [:]  [start:stop:step]  [::]
print(f"cities[0:3]: {cities[0:3]}")
print(f"cities[:3]: {cities[:3]}")
print(f"cities[3:6]: {cities[3:6]}")
print(f"cities[3:7]: {cities[3:7]}")
print(f"cities[5:len(cities)]: {cities[5:len(cities)]}")
print(f"cities[5:]: {cities[5:]}")
print(f"cities[-4:]: {cities[-4:]}")
print(f"cities[::2]: {cities[::2]}")
print(f"cities[1::3]: {cities[1::3]}")

s = "These are not the droids you want"
print(f"s[::2]: {s[::2]}")
print(f"s[1::2]: {s[1::2]}")

print(f"cities: {cities}")
print()

# for VAR ... in ITERABLE:
for city in cities:
    print(city)
print()

s = "abc"
for ch in s:
    print(ch)
print()

print(f"cities: {cities}")

for city in 'Mumbai', 'Anchorage', 'Augusta', 'Durham':
    print(city, city in cities)
print()

s = "Later, Alice visited with the Mad Hatter"
print(f"'Alice' in s: {'Alice' in s}")
print(f"'Betsy' in s: {'Betsy' in s}")
print('-' * 60)

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

print(len(cities), min(cities), max(cities), sorted(cities))
print()
print(len(nums), min(nums), max(nums), sorted(nums), sum(nums))
print()

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Grace', 'Hopper', 'COBOL', '1906-12-09'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

def by_company(person):
    return person[2]

for person in sorted(people, key=by_company):
    print(person)
print()


















