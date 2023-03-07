
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
