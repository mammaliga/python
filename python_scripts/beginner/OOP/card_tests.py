from cards import Card, Deck
import unittest

class CardTests(unittest.TestCase):
	def setUp(self):
		self.card = Card("Diamonds", "J")

	def test_init(self):
		"""карта должна иметь заданные масть и значение"""
		self.assertEqual(self.card.suit, "Diamonds")
		self.assertEqual(self.card.value, "J")

	def test_repr(self):
		"""при вызове инстанции карты, возвращается ее масть и значение"""
		self.assertEqual(repr(self.card), "J of Diamonds")


class DeckTests(unittest.TestCase):
	def setUp(self):
		self.deck = Deck()

	def test_init(self):
		"""создается лист с пятидесятью двумя инстациями карт"""
		self.assertTrue(isinstance(self.deck.cards, list))
		self.assertEqual(len(self.deck.cards), 52)

	def test_count(self):
		self.assertEqual(self.deck.count(), 52)
		self.deck.cards.pop()
		self.assertEqual(self.deck.count(), 51)

	def test_repr(self):
		"""при вызове инстанции колоды, возвращается информация об колличестве карт в колоде"""
		self.assertEqual(repr(self.deck), "Deck of 52 cards")

	def test_sufficient_deal(self):
		"""раздать достающие карты"""
		cards = self.deck._deal(10)
		self.assertEqual(len(cards), 10)
		self.assertEqual(self.deck.count(), 42)

	def test_insuffucient_deal(self):
		"""раздать карты при пустой колоде"""
		cards = self.deck_deal(52)








if __name__ == "__main__":
	unittest.main()