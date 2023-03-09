
data1 = ['red', 'green', 'blue', 'purple', 'green', 'black', 'green']
data2 = ['purple', 'pink', 'teal', 'green', 'blue', 'aqua', 'pink', 'pink', 'black']


s1 = set(data1)
s2 = set(data2)
s1.add('teal')

print(f"s1: {s1}")
print(f"s2: {s2}")

print("common:", s1 & s2)  # intersection
print("only one:", s1 ^ s2)  # xor
print("all:", s1 | s2) # union
print("only s1:", s1 - s2)
print("only s2:", s2 - s1)

