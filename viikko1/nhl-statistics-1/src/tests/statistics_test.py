import unittest
from statistics import Statistics
from player import Player
from statistics import SortBy

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )
    
    def test_pelaajan_haku(self):
        p = str(self.statistics.search("Semenko"))       
        print(p)
        self.assertEqual(p, "Semenko EDM 4 + 12 = 16")

    def test_pelaajaa_ei_ole(self):
        self.assertEqual(self.statistics.search("Crosby"), None)

    def test_pelaajien_lajittelu_pisteiden_mukaan(self):
        tulos = ""
        for i in self.statistics.top(0):
            tulos = str(i)
        self.assertEqual(tulos, "Gretzky EDM 35 + 89 = 124")

    def test_joukkue_loytyy(self):
        oikein = []
        for i in PlayerReaderStub.get_players(self):
            if str(i.team) == "EDM":
                oikein.append(str(i))
        a = []
        for i in self.statistics.team("EDM"):
            a.append(str(i))
            
        self.assertEqual(a, oikein)
    
    def test_pelaajien_luokittelu_syottejen_mukaan(self):
        tulos = ""
        for i in self.statistics.top(0, SortBy.ASSISTS):
            tulos = str(i)
        self.assertEqual(tulos, "Gretzky EDM 35 + 89 = 124")

    def test_pelaajien_luokittelu_maalien_mukaan(self):
        tulos = ""
        for i in self.statistics.top(0, SortBy.GOALS):
            tulos = str(i)
        self.assertEqual(tulos, "Lemieux PIT 45 + 54 = 99")