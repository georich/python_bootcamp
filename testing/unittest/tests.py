import unittest
from activites import eat, nap

class ActivityTests(unittest.TestCase):
    def test_eat_healthy(self):
        """eat should have a positive message for healthy eating"""
        self.assertEqual(eat("broccoli", is_healthy=True), "I'm eating broccoli, because my body is a temple")

    def test_eat_unhealthy(self):
        """indicate the user is eating whatever they want"""
        self.assertEqual(eat("pizza", is_healthy=False), "I'm eating pizza, because I can!")
    
    def test_short_nap(self):
        """short naps are refreshing"""
        self.assertEqual(nap(1), "I'm feeling refreshed after my 1 hour nap")
    
    def test_long_nap(self):
        """napping for too long should be discouraged"""
        self.assertEqual(nap(3), "Ugh I overslept, I didn't mean to nap for 3 hours!")

if __name__ == "__main__":
    unittest.main()
