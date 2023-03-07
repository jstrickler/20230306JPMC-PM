cave_man = "Fred Flintstone"
town = "Bedrock"
value = 38.34871

print(cave_man)  # \n
print(town)  # \n

print(cave_man, town, value)
print()

#  str(cave_man) + " " + str(town) + " " + str(value) + "\n"

print(cave_man, town, sep=', ')
print(cave_man, town, value, sep='#')

print(f"{cave_man} {town} #{value} 2 + 2 = {2 + 2}")

item = "death ray"
price = 5832343
print(f"I bought a {item} for ${price:,.2f}")
print("I bought a {} for ${:,.2f}".format(item, price))


print("first part", end=" ")
print("more", end=" ")
print("more", end=" ")
print("last part")


