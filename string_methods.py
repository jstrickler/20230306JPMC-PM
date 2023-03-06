actor = "Chris Hemsworth"
au = actor.upper()
print(au)
print(len(actor))  # actor.length()
print(actor.count('h'))
print(actor.count('worth'))
print(actor.count('H'))
print(actor.lower().count('h'))  # method chaining
print(actor.find('worth'))
print(actor.find('Chris'))
print(actor.find('Liam'))

print(actor.startswith('Chris'))
print(actor.startswith('Liam'))

path = "wombats.txt"

file_part = path.removesuffix('.txt')
print(file_part)

s = "        Fly me to the moon       "
print(s + "|")
print(s.lstrip() + "|")
print(s.rstrip() + "|")
print(s.strip() + "|")
print()

x = "spam;"
y = "ham:"
print(x.rstrip(":;"))
print(y.rstrip(":;"))
raw_amount = "$1234.56"
amount = raw_amount.lstrip("$")
print(amount)

x = "spam ham toast eggs"
print(x.split())
fields = x.split()
print(fields)

m = "Bill#Gates"
fields = m.split("#")
print(fields)



