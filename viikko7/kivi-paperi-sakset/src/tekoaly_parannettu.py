from tekoaly_interface import TekoalyInterface

class TekoalyParannettu(TekoalyInterface):
    def __init__(self, muistin_koko):
        self._muisti = [None] * muistin_koko
        self._vapaa_muisti_indeksi = 0

    def aseta_siirto(self, siirto):
        if self._vapaa_muisti_indeksi == len(self._muisti):
            for i in range(1, len(self._muisti)):
                self._muisti[i - 1] = self._muisti[i]
            self._vapaa_muisti_indeksi -= 1
        self._muisti[self._vapaa_muisti_indeksi] = siirto
        self._vapaa_muisti_indeksi += 1

    def anna_siirto(self):
        if self._vapaa_muisti_indeksi <= 1:
            return "k"
        viimeisin_siirto = self._muisti[self._vapaa_muisti_indeksi - 1]
        siirrot = {"k": 0, "p": 0, "s": 0}

        for i in range(0, self._vapaa_muisti_indeksi - 1):
            if viimeisin_siirto == self._muisti[i]:
                seuraava = self._muisti[i + 1]
                siirrot[seuraava] += 1

        if siirrot["k"] > siirrot["p"] and siirrot["k"] > siirrot["s"]:
            return "p"
        elif siirrot["p"] > siirrot["k"] and siirrot["p"] > siirrot["s"]:
            return "s"
        else:
            return "k"