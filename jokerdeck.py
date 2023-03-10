from carddeck import CardDeck

class JokerDeck(CardDeck):

    def _make_deck(self):
        super()._make_deck()
        joker = "JOKER", "JOKER"
        for i in range(2):
            self._cards.append(joker)


