import sqlite3

from src.Pessoa import Pessoa

class Responsavel():
    def __init__(self, **kwargs):
        self.__nome = kwargs['nomeR']
        self.__telefone = kwargs['telefone']

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    def salvar(self):
        conn = sqlite3.connect("../BD/Escola.sdb");
        cursor = conn.cursor()
        cursor.execute("select id from Responsavel where nome=? and telefone=?",(self.nome,self.telefone))
        data = cursor.fetchone()
        if data is None:
            cursor.execute("""insert into Responsavel(nome, telefone) 
                               values (?,?)""", (self.nome, self.telefone))
            id = cursor.lastrowid
        else:
            id = data
        conn.commit()
        cursor.close()
        conn.close()
        return id