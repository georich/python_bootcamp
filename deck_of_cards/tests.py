from deck_of_cards import Card, Deck
import pytest

class TestCard:
    @pytest.fixture
    def set_up_test_card(self):
        self.test_card = Card("A", "Spades")
    
    def test_init(self, set_up_test_card):
        assert self.test_card.suit == "Spades"
        assert self.test_card.value == "A"
