
fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

f0 = []
for f in fruits:
    item = f.upper()
    f0.append(item)
print(f"f0: {f0}\n")

#    [item for var in iterable if condition]
f1 = [f.upper() for f in fruits]
print(f"f1: {f1}\n")

f2 = [f.title() for f in fruits if f.startswith('p')]
print(f"f2: {f2}\n")

f3 = [f for f in fruits if f.startswith('p')]
print(f"f3: {f3}\n")

foods = ['spam', 'spam', 'spam', 'ham', 'toast', 'eggs', 'toast', 'spam']
good_foods = [f for f in foods if f != 'spam']
print(f"good_foods: {good_foods}\n")

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]
n1 = [round(x / 23, 3) for x in nums if x > 300]
print(f"n1: {n1}\n")


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

dobs = [p[3] for p in people]
print(f"dobs: {dobs}\n")

names = [f"{p[0]} {p[1]}" for p in people]
print(f"names: {names}\n")

names_gen = (f"{p[0]} {p[1]}" for p in people if p[0].startswith('L'))
print(f"names_gen: {names_gen}")
for name in names_gen:
    print(name)
print()
