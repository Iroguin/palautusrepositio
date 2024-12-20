from kps import KiviPaperiSakset
from tekoaly_parannettu import TekoalyParannettu

class KPSParempiTekoaly(KiviPaperiSakset):
    def __init__(self):
        self._tekoaly = TekoalyParannettu(10)

    def _ensimmaisen_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")

    def _toisen_siirto(self):
        return self._tekoaly.anna_siirto()

    def _aseta_siirto(self, siirto):
        self._tekoaly.aseta_siirto(siirto)