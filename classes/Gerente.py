from classes.Funcionario import Funcionario

class Gerente(Funcionario):
    def __init__(self, _nome, _nascimento, _cpf, _endereco):
        super().__init__(_nome, _nascimento, _cpf, _endereco)

    def getSalario(self):
        return 999.9
