from src.Responsavel import Responsavel
from src.Aluno import Aluno
from src.Professor import Professor
from src.Turma import Turma
from src.Curso import Curso


aluno1 = Aluno(nome="Aluno1",
               endereco="Av. Black",
               email="aluno@gmail.com",
               matricula=56489641,
               nomeR="Resp1",telefone="(55) 5555-5555")

aluno1.salvar()
professores = Professor.listarProfessores();
curso1 = Curso(nome="Sistemas de Informação",cargaHoraria=2000,coordenador=professores[0])
curso1.salvar()
curso1.addTurma(nome="Sistemas de Informação2018a",anoInicio=2018)
professores[0].salvar()
turmas = print(curso1.listarTurmas())



