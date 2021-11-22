class Estado:
    def __init__(self, _nome, _sigla):
        self.nome = _nome
        self.sigla = _sigla

class Cidade:
    def __init__(self, _nome, _estado):
        self.nome = _nome
        self.estado = _estado

class Endereco:
    def __init__(self, _rua, _numero, _bairro, _cep, _cidade):
        self.rua = _rua
        self.numero = _numero
        self.bairro = _bairro
        self.cep = _cep
        self.cidade = _cidade

class Funcionario:
    def __init__(self, _nome, _nascimento, _cpf, _endereco):
        self.nome = _nome
        self.nascimento = _nascimento
        self.cpf = _cpf
        self.endereco = _endereco

    def getNome(self):
        return self.nome
    
    def getNascimento(self):
        return self.nascimento
    
    def getCpf(self):
        return self.cpf

    def getEnderecos(self):
        return self.endereco
