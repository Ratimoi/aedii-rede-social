"""
Atividade Final - AED II - Rede Social
Ponto de partida em Python. Leia o README.md na raiz do repositório.

Este arquivo apenas carrega os dados. Todo o resto é com você:
crie suas próprias estruturas (hash, AVL, heap, grafo, ordenação)
em quantos arquivos quiser dentro desta pasta.
"""
import aedlib  # biblioteca base do projeto (obrigatória - não remova)


def main():
    usuarios, seguidores, posts = aedlib.social_carregar_dados()
    # usuarios:   [id, usuario, nome, data_cadastro]
    # seguidores: [seguidor, seguido]
    # posts:      [id, autor, data, curtidas, texto]

    print(f"Usuários carregados:  {len(usuarios)}")
    print(f"Conexões carregadas:  {len(seguidores)}")
    print(f"Posts carregados:     {len(posts)}")

    # TODO: construir as estruturas e implementar os comandos descritos no README.


if __name__ == "__main__":
    main()
