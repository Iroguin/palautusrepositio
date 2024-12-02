class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=5, kasvatuskoko=5):
        self._validoi_parametrit(kapasiteetti, kasvatuskoko)
        self.kasvatuskoko = kasvatuskoko
        self.luvut = self._luo_lista(kapasiteetti)
        self.alkioiden_maara = 0

    def _validoi_parametrit(self, kapasiteetti, kasvatuskoko):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise ValueError("Kapasiteetin tulee olla positiivinen kokonaisluku")
        if not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise ValueError("Kasvatuskoon tulee olla positiivinen kokonaisluku")

    def kuuluu(self, n):
        for i in range(self.alkioiden_maara):
            if self.luvut[i] == n:
                return True
        return False

    def lisaa(self, n):
        if self.kuuluu(n):
            return False
        if self.alkioiden_maara == len(self.luvut):
            self._kasvata_listaa()
        self.luvut[self.alkioiden_maara] = n
        self.alkioiden_maara += 1
        return True
    
    def _kasvata_listaa(self):
        uusi_koko = len(self.luvut) + self.kasvatuskoko
        uusi_lista = self._luo_lista(uusi_koko)
        self._kopioi_arvot(self.luvut, uusi_lista)
        self.luvut = uusi_lista

    def _kopioi_arvot(self, lahde, kohde): #tää oli ärsyttävä
        for i in range(min(len(lahde), len(kohde))):
            kohde[i] = lahde[i]
    

    def poista(self, n):
        indeksi = self._etsi_luku(n)
        if indeksi == -1:
            return False
        self._siirra_alkioita_vasemmalle(indeksi)
        self.alkioiden_maara -= 1
        return True

    def kopioi_lista(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]
    
    def _etsi_luku(self, n):
        for i in range(self.alkioiden_maara):
            if self.luvut[i] == n:
                return i
        return -1

    def _siirra_alkioita_vasemmalle(self, indeksi):
        for i in range(indeksi, self.alkioiden_maara - 1):
            self.luvut[i] = self.luvut[i + 1]

    def mahtavuus(self):
        return self.alkioiden_maara

    def to_int_list(self):
        tulos = self._luo_lista(self.alkioiden_maara)
        self._kopioi_arvot(self.luvut, tulos)
        return tulos

    @staticmethod
    def yhdiste(a, b):
        tulos = IntJoukko()
        for luku in a.to_int_list() + b.to_int_list():
            tulos.lisaa(luku)
        return tulos

    @staticmethod
    def leikkaus(a, b):
        tulos = IntJoukko()
        for luku in a.to_int_list():
            if b.kuuluu(luku):
                tulos.lisaa(luku)
        return tulos

    @staticmethod
    def erotus(a, b):
        tulos = IntJoukko()
        for luku in a.to_int_list():
            if not b.kuuluu(luku):
                tulos.lisaa(luku)
        return tulos

    def __str__(self):
        if self.alkioiden_maara == 0:
            return "{}"
        
        alkiot = [str(self.luvut[i]) for i in range(self.alkioiden_maara)]
        return "{" + ", ".join(alkiot) + "}"