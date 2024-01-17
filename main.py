from CadastroProdutos import CadastroProdutos
from ListarProdutos import ListarProdutos
from EditarProduto import EditarProduto
from DeletarProduto import DeletarProduto


def separar():
   print('\n---------------------------------------------------------\n')

# --------------------------------------------------------------------------------------


menu = """
         --Sistema--
            
[1] - Cadastrar novo produto;
[2] - Editar Produto;
[3] - Deletar Produto;
[4] - Listar produtos;
[0] - Sair.
"""

# --------------------------------------------------------------------------------------

while True:
   separar()
   print(menu)
   opc = str(input('Qual acao deseja realizar? '))

   if opc == '0':
      break

   elif opc == '1':
      separar()
      print('###Cadastrar novo produto###')
      nome = str(input(' - Digite o nome do produto: '))
      valor = float(input(' - Digite o valor do produto: '))
      estoque = int(input(' - Digite a quantidade em estoque: '))

      novo_produto = CadastroProdutos(nome, valor, estoque)
      novo_produto.confirmar()
   elif opc == '2':
      separar()
      print('###Editar produto###\nOBS: Deixe em branco caso não queira alterar o campo.')
      id_referido = input('id do produto(obrigatorio): ')
      novo_nome = input('Novo nome do produto: ')

      if novo_nome == "":
         novo_nome = None

      novo_valor = input('Novo valor do produto: ')

      if novo_valor == "":
         novo_valor = None

      novo_estoque = input('Novo quantidade em estoque: ')

      if novo_estoque == "":
         novo_estoque = None

      editar = EditarProduto(id_referido, novo_nome, novo_valor, novo_estoque)
      editar.confirmar()
   elif opc == '3':
      separar()
      id_referido = int(input('id do produto(obrigatorio): '))
      delprod = DeletarProduto(id_referido)
      delprod.confirmar()
   elif opc == '4':
      separar()
      ListarProdutos.listar()
   else:
      separar()
      print('Operação inexistente.')
