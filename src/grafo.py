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

    def comunidades(self):
        """
        Encontra as comunidades (componentes conexos) do grafo usando BFS.

        Parâmetros:
            Nenhum.

        Retorno:
            Retorna os tamanhos das comunidades.

        Complexidade: O(V + E), pois cada usuário entra na fila uma vez e cada aresta é olhada duas vezes.
        """
        visitados = [False] * len(self.adjacente)
        tamanhos = []

        for inicio in range(1, len(self.adjacente)):
            if visitados[inicio]:
                continue

            visitados[inicio] = True
            fila = [inicio]

            # a fila usa um índice em vez de pop(0), que é O(n)
            frente = 0

            while frente < len(fila):
                atual = fila[frente]
                frente += 1

                for vizinho in self.adjacente[atual]:
                    if not visitados[vizinho]:
                        # o vizinho é marcado ao entrar na fila, para não ser adicionado duas vezes
                        visitados[vizinho] = True
                        fila.append(vizinho)

            tamanhos.append(len(fila))
        return tamanhos

if __name__ == "__main__":
    import aedlib

    usuarios, seguidores, posts = aedlib.social_carregar_dados()

    g = Grafo(2000)
    for s in seguidores:
        g.adicionar_aresta(int(s[0]), int(s[1]))

    print(len(g.adjacente[1]))  # tem que dar 22

    t = g.comunidades()
    print(len(t), sum(t))  # soma tem que dar 2000
