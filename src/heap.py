"""Árvore Heap usada nos comandos TOP_SEGUIDOS, TOP_CURTIDOS (3.5) e SUGERIR (3.2)."""

class HeapMaxima:
    """Árvore Heap Máxima: possui uma única lista com todos os valores da árvore."""

    def __init__(self):
        """
        Construtor da classe e serve para criar a lista da árvore.

        Parâmetros:
            Nenhum.

        Retorno:
            Retorna None por ser o construtor.

        Complexidade: O(1) cria uma única lista.
        """
        self.itens = []

    def inserir(self, valor):
        """
        Insere o valor na sua posição correspondente da árvore.

        Parâmetros:
            valor (int): valor inteiro.
            
        Retorno:
            Retorna None, apenas insere.

        Complexidade: O(log n), pois executa um sift-up.
        """
        self.itens.append(valor)
        i = len(self.itens) - 1
        pai = (i - 1) // 2

        # Sift-up: enquanto o valor for maior que o pai, troca os dois de lugar,
        # subindo até o topo ou até encontrar um pai maior.
        while i > 0 and valor > self.itens[pai]:
            self.itens[i] = self.itens[pai]
            self.itens[pai] = valor
            i = pai
            pai = (i - 1) // 2

    def remover_maior(self):
        """
        Remove o maior valor da árvore.

        Parâmetros:
            Nenhum.

        Retorno:
            Retorna o valor removido e None caso esteja vazia.
            
        Complexidade: O(log n), pois executa um sift-down.
        """
        if not self.itens:
            return None
        
        maior = self.itens[0]
        ultimo = self.itens.pop()
        
        if not self.itens:
            return maior
        
        self.itens[0] = ultimo
        i = 0
        while True:
            maior_indice = i
            esquerda = 2 * i + 1
            direita = 2 * i + 2

            if esquerda < len(self.itens) and self.itens[esquerda] > self.itens[maior_indice]:
                maior_indice = esquerda

            if direita < len(self.itens) and self.itens[direita] > self.itens[maior_indice]:
                maior_indice = direita

            if maior_indice == i:
                break
            else:
                self.itens[i], self.itens[maior_indice] = self.itens[maior_indice], self.itens[i]
                i = maior_indice

        return maior


if __name__ == "__main__":
    h = HeapMaxima()
    h.inserir(10)
    h.inserir(30)
    h.inserir(20)
    h.inserir(50)
    h.inserir(40)
    print(h.itens)
    h.remover_maior()
    h.remover_maior()
    h.remover_maior()
    h.remover_maior()
    h.remover_maior()
    print(h.itens)
