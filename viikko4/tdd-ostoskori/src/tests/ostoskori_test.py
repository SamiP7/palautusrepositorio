import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korin_hinta_on_tuotteen_hinta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.hinta(), 3)

    def test_korissa_kaksi_tavaraa_kun_lisataan_eri_tuotteet(self):
        maito = Tuote("Maito", 3)
        suklaa = Tuote("Suklaa", 2)

        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(suklaa)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_on_korin_hinta_tuotteiden_hinnan_summa(self):
        maito = Tuote("Maito", 3)
        suklaa = Tuote("Suklaa", 2)

        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(suklaa)

        self.assertEqual(self.kori.hinta(), 5)

    def test_kahden_saman_tuotteen_lisayksen_jalkeen_on_korissa_kaksi_tuotetta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_saman_tuotteen_lisayksen_jalkeen_on_korin_hinta_tuotteiden_hinta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.hinta(), 6)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        ostokset = self.kori.ostokset()

        self.assertEqual(len(ostokset), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        ostos = self.kori.ostokset()[0]

        self.assertEqual(ostos.tuotteen_nimi(), maito.nimi())
        self.assertEqual(ostos.lukumaara(), 1)

    def test_kahden_eri_tuotteen_lisays_jalkeen_korissa_on_kaksi_ostosta(self):
        maito = Tuote("Maito", 3)
        suklaa = Tuote("Suklaa", 2)
        

        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(suklaa)

        ostokset = self.kori.ostokset()

        self.assertEqual(len(ostokset), 2)

    def test_saman_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostos(self):
        maito = Tuote("Maito", 3)
        
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        ostokset = self.kori.ostokset()

        self.assertEqual(len(ostokset), 1)

    
    def test_saman_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostos_jolla_sama_nimi_kuin_tuotteella_ja_lkm_kaksi(self):
        maito = Tuote("Maito", 3)
        
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        ostos = self.kori.ostokset()[0]

        self.assertEqual(ostos.tuotteen_nimi(), maito.nimi())
        self.assertEqual(self.kori.tavaroita_korissa(), 2)
        
    def test_korissa_kaksi_samaa_tuotetta_joista_toinen_poistetaan(self):
        maito = Tuote("Maito", 3)
        
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        self.kori.poista_tuote(maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_korissa_yksi_tuote_joka_poistetaan(self):
        maito = Tuote("Maito", 3)
        
        self.kori.lisaa_tuote(maito)
        self.kori.poista_tuote(maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_metodi_tyhjenna_tyhjentaa_korin(self):
        maito = Tuote("Maito", 3)
        
        self.kori.lisaa_tuote(maito)

        self.kori.tyhjenna()

        self.assertEqual(self.kori.tavaroita_korissa(), 0)
