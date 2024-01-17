import ConexaoBancoDeDados


class EditarProduto:
    def __init__(self, identificacao, nome, valor, estoque):
        self.identificacao = int(identificacao)
        self.nome = nome
        self.valor = valor
        self.estoque = estoque

    def __processo(self):
        if self.nome is not None:
            self.__editar_nome()

        if self.valor is not None:
            self.__editar_valor()

        if self.estoque is not None:
            self.__editar_estoque()

    def __imprimir_produto(self):
        comando = f'SELECT * FROM produtos WHERE id = {self.identificacao}'
        ConexaoBancoDeDados.cursor.execute(comando)
        resultado = ConexaoBancoDeDados.cursor.fetchall()
        print(resultado)

    def __editar_nome(self):
        comando = f'UPDATE produtos SET nome = "{self.nome}" WHERE id = {self.identificacao}'
        ConexaoBancoDeDados.cursor.execute(comando)
        ConexaoBancoDeDados.conexao.commit()

    def __editar_valor(self):
        comando = f'UPDATE produtos SET valor = {self.valor} WHERE id = {self.identificacao}'
        ConexaoBancoDeDados.cursor.execute(comando)
        ConexaoBancoDeDados.conexao.commit()

    def __editar_estoque(self):
        comando = f'UPDATE produtos SET estoque = {self.estoque} WHERE id = {self.identificacao}'
        ConexaoBancoDeDados.cursor.execute(comando)
        ConexaoBancoDeDados.conexao.commit()


    def confirmar(self):
        print()
        self.__imprimir_produto()
        print(f'Novo nome: {self.nome} | Novo Valor: {self.valor} | Nova quantidade em estoque: {self.estoque}')
        print('\nConfirmar alteracao? (acao nao pode ser disfeita)')
        resposta = input("\n[1] - Confirmar [2] - Cancelar: ")

        if resposta == '1':
            self.__processo()

