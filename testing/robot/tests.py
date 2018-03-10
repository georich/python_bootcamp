import pytest
from robot import Robot

class TestRobot:
    def test_charge(self):
        mega_man = Robot("Mega Man", battery=50)
        mega_man.charge()
        assert mega_man.battery == 100
    
    def test_say_name(self):
        mega_man = Robot("Mega Man", battery=50)
        assert mega_man.say_name() == "Beep boop. I am MEGA MAN"
        assert mega_man.battery == 49

    def test_learn_skill(self):
        mega_man = Robot("Mega Man", battery=50)
        assert mega_man.learn_skill("Laser Beams", 20) == "Woah, I know LASER BEAMS!"
        assert mega_man.battery == 30
    