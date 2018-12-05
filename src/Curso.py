from src.Professor import Professor
from src.Turma import Turma

class Curso():
    def __init__(self, **kwargs):
        self.__nome = kwargs['nome']
        self.__cargaHoraria = kwargs['cargaHoraria']
        self.__coordenador = kwargs['coordenador']
        self.__turma = kwargs['turma']

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def cargaHoraria(self):
        return self.__cargaHoraria

    @cargaHoraria.setter
    def cargaHoraria(self, cargaHoraria):
        self.__cargaHoraria = cargaHoraria

    @property
    def coordenador(self):
        return self.__coordenador

    @coordenador.setter
    def coordenador(self, coordenador):
        self.__coordenador = coordenador

    @property
    def turma(self):
        return self.__turma

    @turma.setter
    def turma(self, turma):
        self.__turma = turma