from deck_of_cards import Card, Deck
import pytest

class TestCard:
    @pytest.fixture
    def set_up_test_card(self):
        self.test_card = Card("A", "Spades")
    
    def test_init(self, set_up_test_card):
        assert self.test_card.suit == "Spades"
        assert self.test_card.value == "A"

    def test_repr(self, set_up_test_card):
        assert repr(self.test_card) == "A of Spades"

class TestDeck:
    @pytest.fixture
    def set_up_test_deck(self):
        self.deck = Deck()
    
    def test_init(self, set_up_test_deck):
        assert len(self.deck.cards) == 52
        assert isinstance(self.deck.cards, list)
    
    def test_repr(self, set_up_test_deck):
        assert repr(self.deck) == "Deck of 52 cards."
