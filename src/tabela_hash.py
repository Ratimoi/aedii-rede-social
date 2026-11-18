"""Classe para o requisito 3.1 de BUSCAR @usuario: tabela hash"""

def calcular_hash(texto, tamanho):
    """Faz o cálculo da hash do usuário"""
    h = 0
    for c in texto:
        h = h * 31 + ord(c)
    return h % tamanho

