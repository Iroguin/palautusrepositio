class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self._edellinen_arvo = arvo

    def miinus(self, operandi):
        self._edellinen_arvo = self._arvo
        self._arvo = self._arvo - operandi

    def plus(self, operandi):
        self._edellinen_arvo = self._arvo
        self._arvo = self._arvo + operandi

    def nollaa(self):
        self._edellinen_arvo = self._arvo
        self._arvo = 0

    def aseta_arvo(self, arvo):
        self._arvo = arvo
    
    def kumoa(self):
        temp = self._arvo
        self._arvo = self._edellinen_arvo
        self._edellinen_arvo = temp

    def arvo(self):
        return self._arvo
