import sqlite3

from src.Responsavel import Responsavel
from src.Pessoa import Pessoa
class Aluno(Pessoa):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__matricula = 0
        self.__responsavel = Responsavel(**kwargs)

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    @property
    def responsavel(self):
        return self.__responsavel

    @responsavel.setter
    def responsavel(self, responsavel):
        self.__responsavel = responsavel

    def salvar(self):
        respId = self.responsavel.salvar()
        conn = sqlite3.connect("../BD/Escola.sdb")
        cursor = conn.cursor()
        cursor.execute("""insert into Aluno(nome, email, endereco, responsavel) 
                values (?,?,?,?)""", (self.nome,self.email,self.endereco,respId[0]))
        self.matricula = cursor.lastrowid
        conn.commit()
        cursor.close()
        conn.close()