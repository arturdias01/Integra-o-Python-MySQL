import ConexaoBancoDeDados


class CadastroProdutos:
    def __init__(self, nome, valor, estoque):
        self.nome = nome
        self.valor = valor
        self.estoque = estoque

    def confirmar(self):
        print(f'Produto: {self.nome} | Valor: R${self.valor:.2f} | Quantidade estoque: {self.estoque}.')
        opc = str(input(' - Digite [1] para confirmar ou [2] para cancelar alterações: '))
        if opc == '1':
            self.salvar_alteracao()
            print('###Cadastro realizado com sucesso')

        else:
            print('###Cancelado...')

    def salvar_alteracao(self):
        comando = f'INSERT INTO produtos (nome, valor, estoque) VALUES ("{self.nome}", {self.valor}, {self.estoque})'
        ConexaoBancoDeDados.cursor.execute(comando)
        ConexaoBancoDeDados.conexao.commit()
