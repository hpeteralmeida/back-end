
# Esse código será um upgrade do código do exercicio 000.

# Declaração de classe
class Aluno:
    # Atributos (dados)
    def __init__(self, nome = "", idade = 0):
        self.nome = nome
        self.idade = idade
        # "self" é um nome genérico para o objeto, que após ser nomeado
        # se torna o nome do objeto. Ele é necessário para acessar os 
        # atributos e métodos dentro da classe.

    # Métodos de instanciação:
    def aniversario(self):
        self.idade += 1

    def __str__(self): # Dunder Method
        return f"{self.nome} é Aluno(a) e tem {self.idade} anos de idade."
# Declaração de Objetos

'''primeiroaluno = Aluno()
primeiroaluno.nome = "Pedro" # se depois do "." o nome estiver sem "()", ele é um atributo
primeiroaluno.idade = 20
primeiroaluno.aniversario() # se tiver "()", é um método'''
# o ideal é criar um método para atribuir os valores dos atributos.

primeiroaluno = Aluno("Pedro", 20)
primeiroaluno.aniversario()
print(primeiroaluno)

segundoaluno = Aluno("Maria", 19)
segundoaluno.aniversario()
print(segundoaluno)

terceiroaluno = Aluno("João", 21)
terceiroaluno.aniversario()
print(terceiroaluno)

 

