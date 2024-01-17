import ConexaoBancoDeDados


class ListarProdutos:
    @classmethod
    def listar(cls):
        comando = f'SELECT * FROM produtos'
        ConexaoBancoDeDados.cursor.execute(comando)
        resultado = ConexaoBancoDeDados.cursor.fetchall()

        for linha in resultado:
            print(linha)
