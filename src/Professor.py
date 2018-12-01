from Pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__registro = kwargs['registro']
        self.__telefone = kwargs['telefone']
        self.__atuacao = kwargs['atuacao']

    @property
    def registro(self):
        return self.__registro

    @registro.setter
    def registro(self, registro):
        self.__registro = registro

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    @property
    def atuacao(self):
        return self.__atuacao

    @atuacao.setter
    def atuacao(self, atuacao):
        self.__atuacao = atuacao

