"""
Clase Coche base para el Examen de la UD4
Refactorización
Extrae una superclase Vehículo con los campos
    num_serie
    fabricante
    color
:autor: Jaime Rabasco
"""


class vEHICLE:
    def __init__(self, num_serie, cilindrada, fabricante, color):
        self.num_serie = num_serie;
        self.fabricante = fabricante;
        self.color = color;


class Coche(vEHICLE):

    num_serie = 1;
    cilindrada = 1000;
    fabricante = 'seat';
    color = 'rojo';

    def __init__(self):
        pass

    @property
    def num_serie(self):
        return self.__num_serie

    @num_serie.setter
    def num_serie(self, value):
        self.__num_serie = value

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value: int):
        self.__color = value

    @property
    def cilindrada(self):
        return self.__cilindrada

    @cilindrada.setter
    def cilindrada(self, value):
        self.__cilindrada = value

    @property
    def fabricante(self):
        return self.__fabricante

    @fabricante.setter
    def fabricante(self, value):
        self.__fabricante = value
