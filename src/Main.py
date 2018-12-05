from src.Responsavel import Responsavel
from src.Aluno import Aluno
from src.Professor import Professor
from src.Turma import Turma
from src.Curso import Curso


aluno1 = Aluno(nome="Aluno1",
               endereco="Av. Black",
               email="aluno@gmail.com",
               nomeR="Resp1",telefone="(55) 5555-5555")
print(aluno1.matricula)
aluno1.salvar()
print(aluno1.matricula)
professores = Professor.listarProfessores();

curso1 = Curso(nome="Informatica",cargaHoraria=2000,coordenador=professores[0])
curso = Curso.listarCursos()[3]
curso1.addTurma(nome="Informatica2018a",anoInicio=2018)
professores[0].atuacao = "POO"
professores[0].salvar()
curso1.salvar()
curso1.addTurma(nome="Sistemas de Informação2018c",anoInicio=2020)
turmas = curso1.listarTurmas()
for turma in turmas:
    print("Turma: %s"%turma.nome)

for alunos in curso1.listarAlunos():
    for row in alunos:
        print(row.nome)

print(Professor.listarProfessores()[0].nome,"   ",Professor.listarProfessores()[0].qntAulas);
turmas[0].addAlunos(3)
#print(curso1.listarTurmas())
#print(curso1.obterQntAlunos())



