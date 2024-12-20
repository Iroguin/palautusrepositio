from pelitehdas import PeliTehdas

def main():
    while True:
        print(
            "Valitse pelataanko"
            "\n (a) Ihmistä vastaan"
            "\n (b) Tekoälyä vastaan"
            "\n (c) Parannettua tekoälyä vastaan"
            "\nMuilla valinnoilla lopetetaan"
        )

        vastaus = input()
        if not vastaus.endswith(("a", "b", "c")):
            break
        print("Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s")
        try:
            peli = PeliTehdas.luo_peli(vastaus[-1])
            peli.pelaa()
        except ValueError as e:
            print(f"Virhe: {e}")
            break

if __name__ == "__main__":
    main()