"""Tabela hash usada no comando BUSCAR (3.1)."""

class TabelaHash:
    """Tabela hash com encadeamento: cada gaveta é uma lista de pares [chave, valor] que caíram na mesma posição."""

    def __init__(self, tamanho):
        """
        Construtor da classe e serve para definir o tamanho da tabela hash e montá-la.

        Parâmetros:
            tamanho (int): tamanho da tabela hash, o ideal é que seja um número primo.
        Retorno:
            Retorna None por ser o construtor.
        Complexidade: O(n) cria n listas vazias, uma por gaveta.
        """
        self.tamanho = tamanho
        self.gavetas = [[] for _ in range(tamanho)]

    def buscar(self, chave):
        """
        Busca pelo valor associado com a chave.

        Parâmetros:
            chave (str): o @usuario.
        Retorno:
            o valor armazenado e None caso não exista.
        Complexidade: O(1) em média; O(n) no pior caso (todos estejam na mesma gaveta).
        """
        gaveta = self.calcular_hash(chave, self.tamanho)
        for par in self.gavetas[gaveta]:
            if par[0] == chave:
                return par[1]
        return None

    def calcular_hash(self, chave, tamanho):
        """
        Calcula o hash do usuario.

        Parâmetros:
            chave (str): o @usuário.
            tamanho (int): tamanho da tabela hash.
        Retorno:
            Retorna um índice de 0 até o tamanho - 1.
        Complexidade: O(k) onde k é o tamanho da chave.
        """
        h = 0
        for c in chave:
            h = h * 31 + ord(c) # O 31 serve para diferenciar a ordem dos caracteres (@ab != @ba)
        return h % tamanho

    def inserir(self, chave, valor):
        """
        Insere o valor na gaveta correspondente.

        Parâmetros:
            chave (str): o @usuário.
            valor (list): lista com os dados da chave.
        Retorno:
            Retorna None.
        Complexidade: O(1) pois faz um cálculo e um append.
        """
        gaveta = self.calcular_hash(chave, self.tamanho)
        self.gavetas[gaveta].append([chave, valor])


if __name__ == "__main__":
    t = TabelaHash(7)
    t.inserir("@ana", "dados da ana")
    t.inserir("@bia", "dados da bia")
    print(t.gavetas)
    print(t.buscar("@ana"))
    print(t.buscar("@nao_tem"))
