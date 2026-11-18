"""Grafo de seguidores usado no comando COMUNIDADES (3.3)."""

class Grafo:
    """Grafo não dirigido representado por lista de adjacência: adjacente[i] guarda os vizinhos do usuário i."""

    def __init__(self, n):
        """
        Construtor da classe e serve para definir o tamanho do grafo e montá-lo.

        Parâmetros:
            n (int): tamanho do grafo.

        Retorno:
            Retorna None por ser o construtor.

        Complexidade: O(n), pois cria n listas vazias.
        """
        self.adjacente = [[] for _ in range(n + 1)]

    def adicionar_aresta(self, a, b):
        """
        Liga os usuários a e b nos dois sentidos, pois o grafo é não dirigido.

        Parâmetros:
            a (int): id do item a.
            b (int): id do item b.

        Retorno:
            Retorna None, pois apenas adiciona na lista de adjacência.

        Complexidade: O(1), pois faz apenas dois append.
        """
        self.adjacente[a].append(b)
        self.adjacente[b].append(a)

if __name__ == "__main__":
    import aedlib

    usuarios, seguidores, posts = aedlib.social_carregar_dados()

    g = Grafo(2000)
    for s in seguidores:
        g.adicionar_aresta(int(s[0]), int(s[1]))

    print(len(g.adjacente[1]))  # tem que dar 22
