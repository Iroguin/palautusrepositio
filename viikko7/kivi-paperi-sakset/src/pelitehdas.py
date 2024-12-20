from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly
from kps import KiviPaperiSakset

class PeliTehdas:
    @staticmethod
    def luo_peli(tyyppi: str) -> KiviPaperiSakset:
        pelit = {
            "a": KPSPelaajaVsPelaaja,
            "b": KPSTekoaly,
            "c": KPSParempiTekoaly
        }
        
        peli_luokka = pelit.get(tyyppi)
        if not peli_luokka:
            raise ValueError("Virheellinen pelityyppi")
            
        return peli_luokka()