import sqlite3

from src.Professor import Professor
from src.Turma import Turma

class Curso():
    def __init__(self, **kwargs):
        self.__nome = kwargs['nome']
        self.__cargaHoraria = kwargs['cargaHoraria']
        self.__coordenador = kwargs['coordenador']
        self.__turmas = list()
        self.__idCurso = 0
        if 'id' in kwargs:
            self.__idCurso = kwargs['id']
        self.listarTurmas()

    def salvar(self):
        conn = sqlite3.connect("../BD/Escola.sdb");
        cursor = conn.cursor();
        cursor.execute("""insert into Curso(nome, cargaHoraria, coordenador) 
        values (?,?,?)""",(self.nome,self.cargaHoraria,self.coordenador.registro))
        self.__idCurso = cursor.lastrowid
        conn.commit()
        cursor.close()
        conn.close()

    def listarTurmas(self,ano=None):
        conn = sqlite3.connect("../BD/Escola.sdb");
        cursor = conn.cursor()
        if ano is None:
            cursor.execute("select nome, inicioem from Turma where curso="+str(self.__idCurso))
        else:
            cursor.execute("select nome, inicioem from Turma where curso=?",
                           self.__idCurso)
        rows = cursor.fetchall()
        self.__turmas.clear()
        for row in rows:
            self.__turmas.append(Turma(nome=row[0],anoInicio=row[1]))
        return self.__turmas
        conn.close()
        cursor.close()

    def addTurma(self,nome,anoInicio):
        aux = Turma(nome=nome,anoInicio=anoInicio)
        aux.salvar(self.__idCurso)
        self.__turmas.append(aux)


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


    def __str__(self):
        return ("Curso: %s\nCarga Horaria: %i\nCoordenador: %i \tnome:%s\n"%(self.nome,self.cargaHoraria,
                self.coordenador.registro,self.coordenador.nome))

    def listarAlunos(self):
        alunos = list()
        for turma in self.__turmas:
            alunos.append(turma.listarAlunos())

        return alunos

    def obterQntAlunos(self):
        alunos = 0
        for turma in self.__turmas:
            alunos += turma.obterQntAlunos()

        return alunos

    @staticmethod
    def listarCursos():
        conn = sqlite3.connect("../BD/Escola.sdb")
        cursor = conn.cursor()
        cursor.execute("""select C.nome,C.cargaHoraria, P.nome,P.telefone
        ,P.email,P.areaAtuacao,P.qntAulas, P.registro, P.endereco from Curso C 
        INNER JOIN Professor P on C.coordenador = P.registro""")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()

        cursos = []
        for row in rows:
            coor = Professor(registro=row[7],nome=row[2],telefone=row[3],
                             email=row[4],atuacao=row[5]
                             ,qntAulas=row[6],endereco=row[8])
            cursos.append(Curso(nome=row[0],cargaHoraria=row[1],coordenador=coor))
        return cursos
