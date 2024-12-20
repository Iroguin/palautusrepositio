from abc import ABC, abstractmethod
from tuomari import Tuomari

class KiviPaperiSakset(ABC):
    def pelaa(self):
        """Template method that defines the game algorithm"""
        tuomari = Tuomari()
        ekan_siirto = self._ensimmaisen_siirto()
        tokan_siirto = self._toisen_siirto()

        if tokan_siirto:
            print(f"Tietokone valitsi: {tokan_siirto}")
        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(tuomari)
            ekan_siirto = self._ensimmaisen_siirto()
            tokan_siirto = self._toisen_siirto()
            if tokan_siirto:
                print(f"Tietokone valitsi: {tokan_siirto}")
            self._aseta_siirto(ekan_siirto)
        print("Kiitos!")
        print(tuomari)

    def _onko_ok_siirto(self, siirto):
        return siirto in ["k", "p", "s"]

    @abstractmethod
    def _ensimmaisen_siirto(self):
        pass

    @abstractmethod
    def _toisen_siirto(self):
        pass

    def _aseta_siirto(self, siirto):
        """Hook method for AI learning"""
        pass