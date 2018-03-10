import pytest
from activities import eat, nap

class TestEat:
    def test_eat_healthy(self):
        """eat should have a positive message for healthy eating"""
        assert eat("broccoli", is_healthy=True) == "I'm eating broccoli, because my body is a temple"

    def test_eat_unhealthy(self):
        """indicate the user is eating whatever they want"""
        assert eat("pizza", is_healthy=False) == "I'm eating pizza, because I can!"
    
    def test_eat_healthy_boolean(self):
        """check if the value for is_healthy is a boolean"""
        with pytest.raises(ValueError):
            eat("broccoli", is_healthy="definitely not a boolean")

class TestNap:
    def test_short_nap(self):
        """short naps are refreshing"""
        assert nap(1) == "I'm feeling refreshed after my 1 hour nap"

    def test_long_nap(self):
        """napping for too long should be discouraged"""
        assert nap(3) == "Ugh I overslept, I didn't mean to nap for 3 hours!"
