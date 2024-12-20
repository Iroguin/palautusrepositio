class Tuomari:
    def __init__(self):
        self.ekan_pisteet = 0
        self.tokan_pisteet = 0
        self.tasapelit = 0

    def kirjaa_siirto(self, ekan_siirto, tokan_siirto):
        if self._tasapeli(ekan_siirto, tokan_siirto):
            self.tasapelit += 1
        elif self._eka_voittaa(ekan_siirto, tokan_siirto):
            self.ekan_pisteet += 1
        else:
            self.tokan_pisteet += 1

    def __str__(self):
        return (
            f"Pelitilanne: {self.ekan_pisteet} - {self.tokan_pisteet}\n"
            f"Tasapelit: {self.tasapelit}"
        )

    def _tasapeli(self, eka, toka):
        return eka == toka

    def _eka_voittaa(self, eka, toka):
        voittavat_siirrot = {
            ("k", "s"),
            ("s", "p"),
            ("p", "k")
        }
        return (eka, toka) in voittavat_siirrot