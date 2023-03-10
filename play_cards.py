from carddeck import CardDeck
from jokerdeck import JokerDeck

d1 = CardDeck("Wanda")
d2 = CardDeck("Vision")

print(f"d1: {d1}")
print(f"d2: {d2}")

print(f"d1.dealer: {d1.dealer}")

print(f"d2.get_dealer(): {d2.get_dealer()}")

d1.dealer = "Tony"
print(f"d1.dealer: {d1.dealer}")

try:
    d2.dealer = 47.8
except TypeError as err:
    print(err)
else:
    print(d2.dealer)

d1.shuffle()
print(d1.cards)
print('-' * 60)
for i in range(5):
    card = d1.draw()
    print(f"card: {card}")

print(f"len(d1): {len(d1)}")
print('-' * 60)
j1 = JokerDeck("Natasha")
print(f"j1: {j1}")
print(f"len(j1): {len(j1)}")
j1.shuffle()
print(j1.cards)
for i in range(10):
    print(j1.draw())
print(f"j1: {j1}")

