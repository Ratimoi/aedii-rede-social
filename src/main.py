"""
Atividade Final - AED II - Rede Social
Ponto de partida em Python. Leia o README.md na raiz do repositório.

Este arquivo apenas carrega os dados. Todo o resto é com você:
crie suas próprias estruturas (hash, AVL, heap, grafo, ordenação)
em quantos arquivos quiser dentro desta pasta.
"""
import aedlib  # biblioteca base do projeto (obrigatória - não remova)

from tabela_hash import TabelaHash

def main():
    """Carrega os dados e executa os comandos da rede social."""
    usuarios, seguidores, posts = aedlib.social_carregar_dados()
    # usuarios:   [id, usuario, nome, data_cadastro]
    # seguidores: [seguidor, seguido]
    # posts:      [id, autor, data, curtidas, texto]

    print(f"Usuários carregados:  {len(usuarios)}")
    print(f"Conexões carregadas:  {len(seguidores)}")
    print(f"Posts carregados:     {len(posts)}\n")

    tabela = TabelaHash(4001)
    for usuario in usuarios:
        tabela.inserir(usuario[1], usuario)

    segue = [0] * 2001
    seguidores_qtd = [0] * 2001
    posts_qtd = [0] * 2001

    for seguidor in seguidores:
        segue[int(seguidor[0])] += 1
        seguidores_qtd[int(seguidor[1])] += 1

    for post in posts:
        posts_qtd[int(post[1])] += 1

    while True:
        comando = input("> ")
        partes = comando.split()

        if not partes:
            continue

        match partes[0]:
            case "SAIR":
                break

            case "BUSCAR":
                if len(partes) < 2:
                    print("Comando inválido: insira o usuário que deseja buscar")
                    continue
                usuario = tabela.buscar(partes[1])
                if usuario is None:
                    print(f"Usuário {partes[1]} não encontrado")
                else:
                    print(f"Nome: {usuario[2]}")
                    print(f"Data de cadastro: {usuario[3]}")
                    print(f"Seguindo: {segue[int(usuario[0])]}")
                    print(f"Seguidores: {seguidores_qtd[int(usuario[0])]}")
                    print(f"Posts: {posts_qtd[int(usuario[0])]}\n")

            case _:
                print("Comando inválido")

if __name__ == "__main__":
    main()
