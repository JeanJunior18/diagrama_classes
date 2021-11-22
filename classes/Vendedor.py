from classes.Funcionario import Funcionario

class EquipeVenda:
    def __init__(self, _nome):
        self.nome = _nome

class Vendedor(Funcionario):
    def __init__(self, _nome, _nascimento, _cpf, _endereco, _equipe):
        super().__init__(_nome, _nascimento, _cpf, _endereco)
        equipe = _equipe

    def getSalario(self):
        return 999.9