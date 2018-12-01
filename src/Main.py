from Responsavel import Responsavel
from Aluno import Aluno

responsavel1 = Responsavel(nome="Responsavel1",
                           endereco="Av. Teste",
                           email="teste@123.com",
                           id=123,
                           telefone="62 12345 - 6789")

print(responsavel1.nome)
print(responsavel1.endereco)
print(responsavel1.email)
print(responsavel1.id)
print(responsavel1.telefone)
print()
print()
responsavel2 = Responsavel(nome="Responsavel2",
                           endereco="Av. Brasil",
                           email="teste@gmail.com",
                           id=56,
                           telefone="62 98765 - 4321")

print(responsavel2.nome)
print(responsavel2.endereco)
print(responsavel2.email)
print(responsavel2.id)
print(responsavel2.telefone)

aluno1 = Aluno(nome="Aluno1",
               endereco="Av. Black",
               email="aluno@gmail.com",
               matricula=56489641,
               responsavel=responsavel1)

print(aluno1.nome)
print(aluno1.endereco)
print(aluno1.email)
print(aluno1.matricula)
print(aluno1.responsavel)



