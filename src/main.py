"""
Atividade Final - AED II - Rede Social

Faz a implementação de uma rede social utilizando as mais diversas estruturas e algoritmos de dados estudados durante a disciplina em uma única implementação.

Comandos aceitos:
    BUSCAR:
        Use BUSCAR @nome_usuario para procurar o usuário dentro da rede social

    TOP_SEGUIDOS:
        Use TOP_SEGUIDOS k (k é um número natural) para procurar os usuários mais seguidos até k
    
    TOP_CURTIDOS:
        Use TOP_CURTIDOS k (k é um número natural) para procurar os mais posts mais curtidos até k

    SAIR:
        Utilize para sair da aplicação
"""
import aedlib  # biblioteca base do projeto (obrigatória - não remova)

from tabela_hash import TabelaHash
from heap import HeapMaxima

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
    for u in usuarios:
        tabela.inserir(u[1], u)

    # Contadores indexados pelo id do usuário (ids vão de 1 a 2000).
    # Calculados uma vez só, para o BUSCAR responder em O(1).

    segue = [0] * (len(usuarios) + 1)
    seguidores_qtd = [0] * (len(usuarios) + 1)
    posts_qtd = [0] * (len(usuarios) + 1)

    for s in seguidores:
        segue[int(s[0])] += 1
        seguidores_qtd[int(s[1])] += 1

    for p in posts:
        posts_qtd[int(p[1])] += 1

    while True:
        try:
            comando = input("> ")
        except EOFError:
            break
        
        partes = comando.split()

        if not partes:
            continue

        match partes[0].upper():
            case "SAIR":
                break

            case "BUSCAR":
                if len(partes) < 2:
                    print("Comando inválido: insira o usuário que deseja buscar\n")
                    continue
                usuario = tabela.buscar(partes[1])
                if usuario is None:
                    print(f"Usuário {partes[1]} não encontrado\n")
                else:
                    print(f"Nome: {usuario[2]}")
                    print(f"Data de cadastro: {usuario[3]}")
                    print(f"Seguindo: {segue[int(usuario[0])]}")
                    print(f"Seguidores: {seguidores_qtd[int(usuario[0])]}")
                    print(f"Posts: {posts_qtd[int(usuario[0])]}\n")

            case "TOP_CURTIDOS":
                if len(partes) < 2 or not partes[1].isdigit():
                    print("Comando inválido: insira o número de posts\n")
                    continue

                heap = HeapMaxima()
                for p in posts:
                    heap.inserir([int(p[3]), p])

                k = int(partes[1])
                for posicao in range(1, k + 1):
                    item = heap.remover_maior()
                    if item is None:
                        break
                    post = item[1]
                    autor = usuarios[int(post[1]) - 1][1]
                    print(f"{posicao}. {post[4]} — {post[3]} curtidas — {autor} — {post[2]}")
                print()

            case "TOP_SEGUIDOS":
                if len(partes) < 2 or not partes[1].isdigit():
                    print("Comando inválido: insira o número de usuários\n")
                    continue

                heap = HeapMaxima()
                for u in usuarios:
                    heap.inserir([seguidores_qtd[int(u[0])], u[1]])

                k = int(partes[1])
                for posicao in range(1, k + 1):
                    item = heap.remover_maior()
                    if item is None:
                        break
                    print(f"{posicao}. {item[1]} — {item[0]} seguidores")
                print()

            case _:
                print("Comando inválido\n")

if __name__ == "__main__":
    main()
