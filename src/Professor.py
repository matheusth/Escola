import sqlite3

from src.Pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__registro = kwargs['registro']
        self.__telefone = kwargs['telefone']
        self.__atuacao = kwargs['atuacao']
        self.__qntAulas = kwargs['qntAulas']

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

    @property
    def qntAulas(self):
        return self.__qntAulas

    @qntAulas.setter
    def qntAulas(self, qntAulas):
        self.__qntAulas = qntAulas

    def salvar(self):
        conn = sqlite3.connect("../BD/Escola.sdb")
        cursor = conn.cursor()
        cursor.execute("""insert into Professor(nome,telefone, email, endereco,qntAulas,areaAtuacao) 
                        values (?,?,?,?,?,?)""",
                       (self.nome,self.telefone, self.email, self.endereco,self.__qntAulas,self.atuacao))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def listarProfessores():
        conn = sqlite3.connect("../BD/Escola.sdb")
        cursor = conn.cursor();
        cursor.execute("""select * from Professor""")
        rows = cursor.fetchall()
        professores = []
        for row in rows:
            aux = Professor(registro=row[0],nome=row[1],telefone=row[2]
                             ,email=row[3],qntAulas=row[4],atuacao=row[5],
                             endereco=row[6])
            professores.append(aux)
        cursor.close()
        conn.close()

        return professores
