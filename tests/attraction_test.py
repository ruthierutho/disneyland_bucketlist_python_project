import unittest
from models.attraction import Attraction
from models.land import Land
from models.park import Park

class TestAttraction(unittest.TestCase):

    def setUp(self):
        self.park1 = Park("Magic Kingdom")
        self.land1 = Land("Fantasyland", self.park1, "Fairytale", True)
        self.attraction1 = Attraction("It's a small world", self.land1, True, 1, "So cute!")

    def test_attraction_has_name(self):
        self.assertEqual("It's a small world", self.attraction1.name)

    def test_attraction_has_land(self):
        self.assertEqual("Fantasyland", self.attraction1.land.name)
    
    def test_attraction_land_has_park(self):
        self.assertEqual("Magic Kingdom", self.attraction1.land.park.name)

    def test_attraction_has_visit_true(self):
        self.assertEqual(True, self.attraction1.visited)

    def test_attraction_has_visit_count(self):
        self.assertEqual(1, self.attraction1.visit_count)

    def test_attraction_has_notes(self):
        self.assertEqual("So cute!", self.attraction1.notes)
