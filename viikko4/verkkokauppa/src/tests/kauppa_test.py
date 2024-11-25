import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()

        # palautetaan aina arvo 42
        self.viitegeneraattori_mock.uusi.return_value = 42

        self.varasto_mock = Mock()

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 20
            if tuote_id == 3:
                return 0

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "leipä", 3)
            if tuote_id == 3:
                return Tuote(3, "jugurtti", 2)

        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called()

    def test_tilisiirto_kutsutaan_oikeilla_parametreilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 5)

    def test_kaksi_eri_tuotetta_tilisiirto_kutsutaan_oikeilla_parametreilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 8)

    def test_kaksi_samaa_tuotetta_tilisiirto_kutsutaan_oikeilla_parametreilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 10)

    def test_tuote_loppu_tilisiirto_kutsutaan_oikeilla_parametreilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 5)

    def test_aloita_asiointi_nollaa_edellisen_ostoksen_tiedot(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")
        self.pankki_mock.tilisiirto.assert_called_with(ANY, ANY, ANY, ANY, 3)

    def test_kauppa_pyytaa_uuden_viitenumeron_jokaiselle_maksutapahtumalle(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")
        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 1)

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")
        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 2)

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")
        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 3)
    
    def test_poista_korista_toimii(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.poista_korista(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with(ANY, ANY, ANY, ANY, 3)

    def test_tuotteen_nimi_ja_hinta_toimii(self):
        tuote = Tuote(1, "maito", 5)
        self.assertEqual(str(tuote), "maito")
        self.assertEqual(tuote.hinta, 5)
    
    def test_varaston_metodit_toimivat(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.varasto_mock.ota_varastosta.assert_called()
        
        self.kauppa.poista_korista(1)
        
        self.varasto_mock.palauta_varastoon.assert_called()

    def test_alusta_kirjanpito(self):
        from kirjanpito import Kirjanpito
        kirjanpito = Kirjanpito()
        tapahtumat = kirjanpito.tapahtumat
        self.assertEqual(len(tapahtumat), 0)

    def test_viitegeneraattori_kasvattaa_viitetta(self):
        from viitegeneraattori import Viitegeneraattori
        viitegen = Viitegeneraattori()
        viite1 = viitegen.uusi()
        viite2 = viitegen.uusi()
        self.assertEqual(viite2, viite1 + 1)

    def test_tuote_equals_vertailu(self):
        tuote1 = Tuote(1, "maito", 5)
        tuote2 = Tuote(1, "maito", 5)
        tuote3 = Tuote(2, "leipä", 3)
        
        self.assertEqual(tuote1, tuote2)
        self.assertNotEqual(tuote1, tuote3)
        
    def test_varasto_tuote_loytyi(self):
        from varasto import Varasto
        from kirjanpito import Kirjanpito
        
        kirjanpito = Kirjanpito()
        varasto = Varasto(kirjanpito)
        
        tuote = varasto.hae_tuote(1)
        self.assertEqual(tuote.nimi, "Koff Portteri")
        self.assertEqual(tuote.hinta, 3)
        self.assertEqual(varasto.saldo(1), 100)

    def test_varasto_tuote_ei_loydy(self):
        from varasto import Varasto
        from kirjanpito import Kirjanpito
        
        kirjanpito = Kirjanpito()
        varasto = Varasto(kirjanpito)
        
        tuote = varasto.hae_tuote(999)
        self.assertIsNone(tuote)

    def test_varasto_saldo_ja_otto(self):
        from varasto import Varasto
        from kirjanpito import Kirjanpito
        
        kirjanpito = Kirjanpito()
        varasto = Varasto(kirjanpito)
        
        tuote = varasto.hae_tuote(1)
        alkusaldo = varasto.saldo(1)
        
        varasto.ota_varastosta(tuote)
        self.assertEqual(varasto.saldo(1), alkusaldo - 1)
        self.assertEqual(len(kirjanpito.tapahtumat), 1)
        self.assertEqual(kirjanpito.tapahtumat[0], "otettiin varastosta Koff Portteri")
        
        varasto.palauta_varastoon(tuote)
        self.assertEqual(varasto.saldo(1), alkusaldo)
        self.assertEqual(len(kirjanpito.tapahtumat), 2)
        self.assertEqual(kirjanpito.tapahtumat[1], "palautettiin varastoon Koff Portteri")

    def test_kaikkien_tuotteiden_alustus(self):
        from varasto import Varasto
        from kirjanpito import Kirjanpito
        
        kirjanpito = Kirjanpito()
        varasto = Varasto(kirjanpito)
        
        self.assertEqual(varasto.saldo(1), 100)
        self.assertEqual(varasto.saldo(2), 25)
        self.assertEqual(varasto.saldo(3), 30)
        self.assertEqual(varasto.saldo(4), 40)
        self.assertEqual(varasto.saldo(5), 15)
        
        tuote = varasto.hae_tuote(2)
        self.assertEqual(tuote.nimi, "Fink Bräu I")
        self.assertEqual(tuote.hinta, 1)
        
        tuote = varasto.hae_tuote(5)
        self.assertEqual(tuote.nimi, "Weihenstephaner Hefeweisse")
        self.assertEqual(tuote.hinta, 4)