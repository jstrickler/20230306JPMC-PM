from pprint import pprint

knight_data = {}

with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        # fields = line.split(':')
        # name = fields[0]
        # title = fields[1]
        #  etc 
        name, title, color, quest, comment = line.split(':')
        knight_data[name] = title, color, quest, comment

pprint(knight_data)
print()

print(f"data['Galahad']: {knight_data['Galahad']}")
galahad_data = knight_data['Galahad']
print(f"galahad_data[0]: {galahad_data[0]}")
print(f"data['Galahad'][0]: {knight_data['Galahad'][0]}")
print()

for name, data in knight_data.items():
    print(data[0], name, data[2])
print()


