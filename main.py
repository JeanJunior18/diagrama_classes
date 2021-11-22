from datetime import datetime
from classes.Funcionario import Estado, Cidade, Endereco, Funcionario
from classes.Vendedor import Vendedor, EquipeVenda
from classes.Gerente import Gerente

objetoEstado = Estado('Maranhão', 'MA')
objetoCidade = Cidade('Codó', objetoEstado)
objetoEndereco = Endereco('Rua Claudin', 123, 'Clovis', '64000-000', objetoCidade)
objetoEquipeVendas = EquipeVenda('Dream Team')

objetoVendedor = Vendedor('Jean Junior', datetime(2001, 3, 6), '111.222.333-44', objetoEndereco, objetoEquipeVendas)
objetoGerente = Gerente('Tardely', datetime(2001, 3, 6), '111.222.333-44', objetoEndereco)

print(objetoVendedor.getNome())
print(objetoGerente.getNome())