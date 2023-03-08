

cities = ["Paris", "Columbus", "Little Elm", "Mumbai"]

rev_cities = reversed(cities)
print(f"rev_cities: {rev_cities}")

for city in rev_cities:
    print(city)
print()
print('-' * 60)
# this makes a copy of cities in reverse order
# print(f"cities[::-1]: {cities[::-1]}")


enum_cities = enumerate(cities)
print(f"enum_cities: {enum_cities}")
for i, city in enum_cities:
    print(i, city)
print()
print(f"list(enumerate(cities)): {list(enumerate(cities))}")
print()


for i in range(10):
    print("I LOVE PYTHON!!")
print()

#   range(stop)   range(start, stop)  range(start, stop, step)
for i in range(1, 11):
    print(i, i * '*')
print()

print('-' * 60)

print(f"'wocka' * 3: {'wocka' * 3}")

print(f"'*' * 25: {'*' * 25}")

data = [0] * 25
print(f"data: {data}")

flags = [False] * 10
print(f"flags: {flags}")





