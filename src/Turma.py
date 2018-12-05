import sqlite3

from src import Aluno


class Turma():
    def __init__(self, **kwargs):
        self.__nome = kwargs['nome']
        self.__anoInicio = kwargs['anoInicio']
        self.__alunos = list()
        self.__id = 0
        if 'id' in kwargs:
            self.__id = kwargs['id']

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

    def addAlunos(self,matricula):

        if(self.obterQntAlunos() < 15):
            conn = sqlite3.connect("../BD/Escola.sdb")
            cursor = conn.cursor()
            cursor.execute("update aluno set turma=? where matricula=?",self.__id,matricula)
            conn.commit()
            cursor.close()
            conn.close()
        else:
            print("você não pode adicionar mais alunos á essa sala.")

    def listarAlunos(self):
        conn = sqlite3.connect("../BD/Escola.sdb")
        cursor = conn.cursor()
        cursor.execute("""select matricula,A.nome,endereco,email,R.nome,R.telefone from Aluno A
                       INNER JOIN Responsavel R on 
                       Aluno.responsavel = R.id where turma=?""",
                       self.__id)
        rows = cursor.fetchall()
        self.__alunos.clear()
        for row in rows:
            self.__alunos.append(Aluno(matricula=row[0],nome=row[1],
                                       endereco=row[2],email=row[3], nomeR=row[4],
                                       telefone=row[5]))
        conn.close()
        cursor.close()
        return self.__alunos

    def obterQntAlunos(self):
        return len(self.listarAlunos())

    def salvar(self,idCurso):
        conn = sqlite3.connect("../BD/Escola.sdb");
        cursor = conn.cursor();
        cursor.execute("""insert into Turma(nome, inicioEm, curso) 
                values (?,?,?)""", (self.nome, self.anoInicio, idCurso))
        conn.commit()
        cursor.close()
        conn.close()
