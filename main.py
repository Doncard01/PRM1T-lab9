import klasa

if __name__ == '__main__':
    morse_code = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
        'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..'}


    try:
        kodek = klasa.Codec(morse_code)

        tekst = lista(input("Podaj tekst do konwertowania: "))
        print(tekst)
        print(kodek.koduj(tekst))

        mors = input("Podaj wiadomosc kodem morsa: ")
        podzial = mors.split()
        list(podzial)
        print(podzial)
        print(kodek.dekoduj(podzial))

    except (klasa.MojBlad, TypeError) as err:
        print("Blad: ", err)
    finally:
        print("Program zakonczyl dzialanie")


