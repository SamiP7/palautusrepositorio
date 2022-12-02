from enum import Enum
from tkinter import ttk, constants, StringVar


class Komento(Enum):
    SUMMA = 1
    EROTUS = 2
    NOLLAUS = 3
    KUMOA = 4

class Summa:
    def __init__(self, sovellus, arvo):
        self.sovellus = sovellus
        self.arvo = arvo
        self._edellinen_arvo = 0

    def suorita(self):
        self._edellinen_arvo = self.sovellus.tulos
        self.sovellus.plus(self.arvo)

    def kumoa(self):
        self.sovellus.aseta_arvo(self._edellinen_arvo)

class Erotus:
    def __init__(self, sovellus, arvo):
        self.sovellus = sovellus
        self.arvo = arvo
        self._edellinen_arvo = 0

    def suorita(self):
        self._edellinen_arvo = self.sovellus.tulos
        self.sovellus.miinus(self.arvo)

    def kumoa(self):
        self.sovellus.aseta_arvo(self._edellinen_arvo)

class Nollaus:
    def __init__(self, sovellus):
        self.sovellus = sovellus
        self._edellinen_arvo = 0

    def suorita(self):
        self._edellinen_arvo = self.sovellus.tulos
        self.sovellus.nollaa()

    def kumoa(self):
        self.sovellus.aseta_arvo(self._edellinen_arvo)

class Kumoa:
    def __init__(self, sovellus):
        self.sovellus = sovellus

    def suorita(self):
        pass


class Kayttoliittyma:
    def __init__(self, sovelluslogiikka, root):
        self._sovelluslogiikka = sovelluslogiikka
        self._root = root

    
    def _lue_syote(self):
        arvo = 0

        try:
            arvo = int(self._syote_kentta.get())
        except Exception:
            pass

        return arvo


    def hae_komento(self, komento, arvo):
        if komento == Komento.SUMMA:
            self._sovellus.plus(arvo)
        elif komento == Komento.EROTUS:
            self._sovellus.miinus(arvo)
        elif komento == Komento.NOLLAUS:
            self._sovellus.nollaa()
        elif komento == Komento.KUMOA:
            pass


    def kaynnista(self):
        self._tulos_var = StringVar()
        self._tulos_var.set(self._sovelluslogiikka.tulos)
        self._syote_kentta = ttk.Entry(master=self._root)

        tulos_teksti = ttk.Label(textvariable=self._tulos_var)

        summa_painike = ttk.Button(
            master=self._root,
            text="Summa",
            command=lambda: self._suorita_komento(Komento.SUMMA)
        )

        erotus_painike = ttk.Button(
            master=self._root,
            text="Erotus",
            command=lambda: self._suorita_komento(Komento.EROTUS)
        )

        self._nollaus_painike = ttk.Button(
            master=self._root,
            text="Nollaus",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.NOLLAUS)
        )

        self._kumoa_painike = ttk.Button(
            master=self._root,
            text="Kumoa",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.KUMOA)
        )

        tulos_teksti.grid(columnspan=4)
        self._syote_kentta.grid(columnspan=4, sticky=(constants.E, constants.W))
        summa_painike.grid(row=2, column=0)
        erotus_painike.grid(row=2, column=1)
        self._nollaus_painike.grid(row=2, column=2)
        self._kumoa_painike.grid(row=2, column=3)

    def _suorita_komento(self, komento):
        self._komennot = {
            Komento.SUMMA: Summa(self._sovelluslogiikka, self._lue_syote()),
            Komento.EROTUS: Erotus(self._sovelluslogiikka, self._lue_syote()),
            Komento.NOLLAUS: Nollaus(self._sovelluslogiikka),
            Komento.KUMOA: Kumoa(self._sovelluslogiikka)
        }
        
        if (komento == Komento.KUMOA):
            self._komento_olio.kumoa()
        else:
            self._komento_olio = self._komennot[komento]
            self._komento_olio.suorita()
        
        self._kumoa_painike["state"] = constants.NORMAL

        if self._sovelluslogiikka.tulos == 0:
            self._nollaus_painike["state"] = constants.DISABLED
        else:
            self._nollaus_painike["state"] = constants.NORMAL

        self._syote_kentta.delete(0, constants.END)
        self._tulos_var.set(self._sovelluslogiikka.tulos)

