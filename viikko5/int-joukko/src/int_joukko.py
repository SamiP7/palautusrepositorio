KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")  # heitin vaan jotain :D
        else:
            self.kapasiteetti = kapasiteetti
            self.kasvatuskoko = kasvatuskoko

        self.lukujono = [0] * self.kapasiteetti

        self.alkioiden_lkm = 0

    def kuuluuko_luku_lukujonoon(self, luku):
        lukujen_maara_lukujonossa = 0

        for alkio in range(0, self.alkioiden_lkm):
            if luku == self.lukujono[alkio]:
                lukujen_maara_lukujonossa += 1

        if lukujen_maara_lukujonossa > 0:
            return True
        else:
            return False

    def lisaa_lukujonoon(self, luku):

        if not self.kuuluuko_luku_lukujonoon(luku):
            self.lukujono[self.alkioiden_lkm] = luku
            self.alkioiden_lkm += 1

            if self.alkioiden_lkm % len(self.lukujono) == 0:
                taulukko_old = self.lukujono
                self.kopioi_taulukko(self.lukujono, taulukko_old)
                self.lukujono = [0] * (self.alkioiden_lkm + self.kasvatuskoko)
                self.kopioi_taulukko(taulukko_old, self.lukujono)

            return True

        return False

    def poista_lukujonosta(self, luku):
        kohta_mista_alkio_loytyy = -1
        apu_luku = 0

        for alkio in range(0, self.alkioiden_lkm):
            if luku == self.lukujono[alkio]:
                kohta_mista_alkio_loytyy = alkio  # siis luku löytyy tuosta kohdasta :D
                self.lukujono[kohta_mista_alkio_loytyy] = 0
                break

        if kohta_mista_alkio_loytyy != -1:
            for alkio in range(kohta_mista_alkio_loytyy, self.alkioiden_lkm - 1):
                apu_luku = self.lukujono[alkio]
                self.lukujono[alkio] = self.lukujono[alkio + 1]
                self.lukujono[alkio + 1] = apu_luku

            self.alkioiden_lkm -= 1
            return True

        return False

    def kopioi_taulukko(self, taulukko1, taulukko2):
        for alkio in range(0, len(taulukko1)):
            taulukko2[alkio] = taulukko1[alkio]

    def return_alkioiden_lkm(self):
        return self.alkioiden_lkm

    def muunna_taulu_int_lukujonoksi(self):
        taulu = [0] * self.alkioiden_lkm

        for alkio in range(0, len(taulu)):
            taulu[alkio] = self.lukujono[alkio]

        return taulu

    @staticmethod
    def yhdista_taulut_int_lukujonoksi(taulu1, taulu2):
        int_joukko = IntJoukko()
        a_taulu = taulu1.muunna_taulu_int_lukujonoksi()
        b_taulu = taulu2.muunna_taulu_int_lukujonoksi()

        for alkio in range(0, len(a_taulu)):
            int_joukko.lisaa_lukujonoon(a_taulu[alkio])

        for i in range(0, len(b_taulu)):
            int_joukko.lisaa_lukujonoon(b_taulu[i])

        return int_joukko

    @staticmethod
    def yhdista_taulujen_leikkaus_lukujonoksi(taulu1, taulu2):
        taulujen_leikkaus = IntJoukko()
        a_taulu = taulu1.muunna_taulu_int_lukujonoksi()
        b_taulu = taulu2.muunna_taulu_int_lukujonoksi()

        for alkio_a in range(0, len(a_taulu)):
            for alkio_b in range(0, len(b_taulu)):
                if a_taulu[alkio_a] == b_taulu[alkio_b]:
                    taulujen_leikkaus.lisaa_lukujonoon(b_taulu[alkio_b])

        return taulujen_leikkaus

    @staticmethod
    def taulujen_erotus_lukujonona(taulu1, taulu2):
        taulujen_erotus = IntJoukko()
        a_taulu = taulu1.muunna_taulu_int_lukujonoksi()
        b_taulu = taulu2.muunna_taulu_int_lukujonoksi()

        for alkio in range(0, len(a_taulu)):
            taulujen_erotus.lisaa_lukujonoon(a_taulu[alkio])

        for alkio in range(0, len(b_taulu)):
            taulujen_erotus.poista_lukujonosta(b_taulu[alkio])

        return taulujen_erotus

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.lukujono[0]) + "}"
        else:
            tuotos = "{"
            for alkio in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.lukujono[alkio])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.lukujono[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos
