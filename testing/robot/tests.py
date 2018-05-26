import pytest
from robot import Robot

class TestRobot:
    @pytest.fixture
    def set_up_megaman(self):
        self.mega_man = Robot("Mega Man", battery=50)
    
    def test_charge(self, set_up_megaman):
        # mega_man = Robot("Mega Man", battery=50)
        self.mega_man.charge()
        assert self.mega_man.battery == 100

    def test_say_name(self, set_up_megaman):
        # mega_man = Robot("Mega Man", battery=50)
        assert self.mega_man.say_name() == "Beep boop. I am MEGA MAN"
        assert self.mega_man.battery == 49

    def test_learn_skill(self, set_up_megaman):
        # mega_man = Robot("Mega Man", battery=50)
        assert self.mega_man.learn_skill("Laser Beams", 20) == "Woah, I know LASER BEAMS!"
        assert self.mega_man.battery == 30
    