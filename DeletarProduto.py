import ConexaoBancoDeDados

class DeletarProduto:
    def __init__(self, identificacao):
        self.identificacao = identificacao

    def confirmar(self):
        print('Confirmar alteracao? (acao nao pode ser disfeita)\n')
        comando = f'SELECT * FROM produtos WHERE id = {self.identificacao}'
        ConexaoBancoDeDados.cursor.execute(comando)
        resultado = ConexaoBancoDeDados.cursor.fetchall()
        print(resultado)
        resposta = input("\n[1] - Confirmar [2] - cancelar: ")

        if resposta == '1':
            self.__deletar()

    def __deletar(self):
        comando = f'DELETE FROM produtos WHERE id = {self.identificacao}'
        ConexaoBancoDeDados.cursor.execute(comando)
        ConexaoBancoDeDados.conexao.commit()
