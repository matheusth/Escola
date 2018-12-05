
class Turma():
    def __init__(self, **kwargs):
        self.__nome = kwargs['nome']
        self.__anoInicio = kwargs['anoInicio']
        self.__aluno = list()

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def anoInicio(self):
        return self.__anoInicio

    @anoInicio.setter
    def anoInicio(self, anoInicio):
        self.__anoInicio = anoInicio