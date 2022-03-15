class Animal(object):
    def __init__(self, especie: str) -> None:
        self.__especie = especie

    @property
    def especie(self):
        return self.__especie

    @especie.setter
    def especie(self, value: str):
        self.__especie = value


class Mamimero(Animal):

    def __init__(self, especie, mamar=True) -> None:
        self.__mamar = mamar
        super().__init__(especie)

    def mamar(self):
        if Mamimero:
            print(f'O animal da especie {self._Animal__especie} está mamando!')


gorila = Mamimero('primata')
gorila.mamar()

