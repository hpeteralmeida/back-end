# Declaração de classe
class Aluno:
    # Atributos (dados)
    def __init__(self):
        self.nome = ""
        self.idade = 0
       
    # Métodos de instanciação:
    def aniversario(self):
        self.idade += 1
    def mensagem(self):
        return f"{self.nome} é Aluno(a) e tem {self.idade} anos de idade."
    
# Declaração de Objetos

primeiroaluno = Aluno()
primeiroaluno.nome = "Pedro" # se depois do "." o nome estiver sem "()", ele é um atributo
primeiroaluno.idade = 20
primeiroaluno.aniversario() # se tiver "()", é um método
print(primeiroaluno.mensagem())

segundoaluno = Aluno()
segundoaluno.nome = "Maria"
segundoaluno.idade = 19
segundoaluno.aniversario()
print(segundoaluno.mensagem())

# é possível criar quantos objetos forem necessários a partir da classe.
terceiroaluno = Aluno()
terceiroaluno.nome = "João"
terceiroaluno.idade = 18
terceiroaluno.aniversario()
print(terceiroaluno.mensagem())
