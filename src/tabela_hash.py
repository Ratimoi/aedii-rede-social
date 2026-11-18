"""Classe para o requisito 3.1 de BUSCAR @usuario: tabela hash"""

class TabelaHash:
    """Tabela hash com encadeamento: cada gaveta é uma lista de pares [chave, valor]"""

    def __init__(self, tamanho):
        """Construtor da classe com tamanho das gavetas"""
        self.tamanho = tamanho
        self.gavetas = [[] for _ in range(tamanho)]

    def buscar(self, chave):
        """Busca a chave dentro das gavetas e a retorna caso exista"""
        gaveta = self.calcular_hash(chave, self.tamanho)
        for par in self.gavetas[gaveta]:
            if par[0] == chave:
                return par[1]
        return None

    def calcular_hash(self, texto, tamanho):
        """Faz o cálculo da hash do usuário"""
        h = 0
        for c in texto:
            h = h * 31 + ord(c)
        return h % tamanho

    def inserir(self, chave, valor):
        """Insere o valor dentro da sua respectiva gaveta ao calcular o hash"""
        gaveta = self.calcular_hash(chave, self.tamanho)
        self.gavetas[gaveta].append([chave, valor])


if __name__ == "__main__":
    t = TabelaHash(7)
    t.inserir("@ana", "dados da ana")
    t.inserir("@bia", "dados da bia")
    print(t.gavetas)
    print(t.buscar("@ana"))
    print(t.buscar("@nao_tem"))
