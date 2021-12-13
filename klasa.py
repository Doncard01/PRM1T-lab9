class Codec:
    def __init__(self, slownik):
        self.__slownik = slownik
        self.__odwrotny = odwroc(self.__slownik)

    def koduj(self, lista):
        if type(lista) is not list:
            raise TypeError("Parametr nie jest lista!")
        else:
            konwert = []
            for i in lista:
                if i not in self.__slownik.keys():
                    raise MojBlad("W tekscie znajduje sie znak, ktorego nie ma w slowniku!")
                else:
                    konwert.append(self.__slownik[i])
        return konwert

    def dekoduj(self, kod):
        if type(kod) is not list:
            raise TypeError("Parametr nie jest lista!")
        else:
            konwert = []
            for i in kod:
                if i not in self.__odwrotny.keys():
                    raise MojBlad("W tekscie znajduje sie znak, ktorego nie ma w slowniku!")
                else:
                    konwert.append(self.__odwrotny[i])
            return konwert

class MojBlad(Exception):
    def __init__(self, klucz, wiadomosc="Nie rozpoznano klucza"):
        self.klucz = klucz
        self.wiadomosc = wiadomosc
        super().__init__(self.wiadomosc)

    def __str__(self):
        return f"{self.klucz} - {self.wiadomosc}"


def odwroc(slownik):
    odwrotny = {}
    for key, value in slownik.items():
        odwrotny[value] = key
    return odwrotny