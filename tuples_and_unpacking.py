person = "Bill", "Gates", "Microsoft", "1955-10-28"

thing = "a", [1, 2, 3], 4.5, ["spam", "ham"]

print(f"person: {person}")
print(f"type(person): {type(person)}")
print(person[0], person[1])

print(f"person[:2]: {person[:2]}")

# iterable unpacking
first_name, last_name, product, dob = person
print(first_name, last_name)
print()

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', 'NeXT', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', 'Sun', '1944-08-17'),
    ('Grace', 'Hopper', 'COBOL', '1906-12-09'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', 'git', '1969-12-28'),
]
print(f"people[0]: {people[0]}")
print(f"people[0][0]: {people[0][0]}")
print(f"people[0][0][0]: {people[0][0][0]}")
print()

for first_name, last_name, *product, dob in people:
    print(first_name, last_name, product, dob)
print()


