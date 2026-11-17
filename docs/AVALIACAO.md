# Critérios de Avaliação — Atividade Final de AED II

A nota é um **conceito**: **A**, **B**, **C** ou **D**. Ele é atribuído a partir de cinco critérios:

| # | Critério | O que é avaliado |
|---|----------|------------------|
| 1 | Completude do código | Funcionalidades 3.1 a 3.6 implementadas, corretas e respeitando as regras |
| 2 | Clareza da explicação no código | Como métodos, funções e classes estão explicados e escritos |
| 3 | Documentação do aluno | O `RELATORIO` (seção 5 do README) |
| 4 | Entrega no prazo | Envio pelo Blackboard até **08/12** |
| 5 | Bônus | API de consulta via linha de comando (item 3.7 do README) |

> **Importante:** o **conceito A só é alcançável com o bônus feito**. Sem bônus, o conceito máximo é **B**.

---

## Critério 1 — Completude do código

Cada uma das seis funcionalidades (3.1 a 3.6) é classificada como:

- **Completa:** funciona para os dados fornecidos e para os casos de borda, usa a estrutura pedida implementada pelo aluno e respeita as regras da seção 4.
- **Parcial:** existe, mas tem erros em alguns casos, ou está incompleta (por exemplo, AVL sem rebalanceamento, ou consulta por intervalo que percorre a árvore inteira).
- **Ausente:** não foi implementada, não roda, ou usa estrutura proibida (`dict`, `set`, `heapq`, `sorted`, `Map`, `Set`, `.sort()` etc.).

Pontos verificados em cada funcionalidade:

| Funcionalidade | Pontos verificados |
|---|---|
| 3.1 BUSCAR (hash) | Função de hash própria, tratamento de colisões, usuário inexistente |
| 3.2 SUGERIR (grafo + heap) | Exclui o próprio usuário e quem ele já segue, ordena por conexões em comum, usa heap própria |
| 3.3 COMUNIDADES (grafo) | Trata o grafo como não dirigido, conta e ordena os componentes, conta os isolados |
| 3.4 POSTS_ENTRE (AVL) | Rotações corretas, árvore balanceada, consulta por intervalo sem percorrer tudo, datas incluídas |
| 3.5 TOP_SEGUIDOS / TOP_CURTIDOS (heap) | Heap própria correta, `k` maior que o total |
| 3.6 RANKING (ordenação) | Algoritmo O(n log n) próprio, fórmula de engajamento, desempate alfabético |

| Nível | Descrição |
|---|---|
| **Excelente** | As 6 funcionalidades estão completas |
| **Bom** | 5 completas e no máximo 1 parcial |
| **Regular** | Pelo menos 3 completas, e as demais parciais ou ausentes |
| **Insuficiente** | Menos de 3 completas |

---

## Critério 2 — Clareza e forma da explicação no código (métodos, funções e classes)

Pontos avaliados:

- **Explicação de cada classe:** toda classe tem uma descrição do que representa e de qual estrutura implementa (docstring em Python, comentário `/** ... */` em JS).
- **Explicação de cada método e função:** todo método e função relevante explica o que faz, os parâmetros, o retorno e, quando fizer sentido, a complexidade (por exemplo, `O(log n)`).
- **Comentários nos trechos difíceis:** as partes não óbvias estão comentadas, como rotações da AVL, `sift-up`/`sift-down` da heap, função de hash e reconstrução de resultados no grafo. Comentários que só repetem o código não contam.
- **Nomes:** variáveis, funções e classes têm nomes descritivos e consistentes (por exemplo, `inserir`, `rotacao_direita`, `buscar_intervalo`).
- **Organização:** cada estrutura fica separada (em arquivo ou classe própria), sem código duplicado e com funções de tamanho razoável.

| Nível | Descrição |
|---|---|
| **Excelente** | Todas as classes e métodos explicados, trechos difíceis comentados, código organizado e legível |
| **Bom** | Quase tudo explicado, com pequenas lacunas ou poucos nomes ruins |
| **Regular** | Explicação só em parte do código, ou organização confusa (tudo em um único arquivo, funções enormes) |
| **Insuficiente** | Praticamente sem explicação e difícil de entender |

---

## Critério 3 — Documentação feita pelo aluno (RELATORIO)

O relatório deve cobrir os cinco itens da seção 5 do README:

1. **O que foi feito:** quais funcionalidades foram implementadas e quais ficaram incompletas.
2. **Como foi feito:** a organização do código e o papel de cada arquivo.
3. **Escolhas tomadas e por quê:** hash, colisões, tamanho da tabela, AVL, heap de máximo ou de mínimo, algoritmo de ordenação, representação do grafo.
4. **Complexidade de cada comando, com justificativa.**
5. **Testes feitos manualmente:** entradas, saídas obtidas e casos de borda.

| Nível | Descrição |
|---|---|
| **Excelente** | Os 5 itens completos, escolhas bem justificadas, complexidades corretas e testes que incluem casos de borda |
| **Bom** | Os 5 itens presentes, com justificativas ou testes superficiais em algum ponto |
| **Regular** | Falta 1 ou 2 itens, ou o conteúdo é muito raso |
| **Insuficiente** | Sem relatório, ou faltam 3 itens ou mais |

---

## Critério 4 — Entrega no prazo

| Situação | Efeito |
|---|---|
| Enviado pelo Blackboard **até 08/12**, com link do repositório e `.zip` | Atende |
| Enviado **após 08/12** | O conceito final fica limitado a **C** |
| Não enviado | Conceito **D** |

---

## Critério 5 — Bônus: API de consulta via linha de comando (item 3.7)

O bônus é considerado **feito** quando:

- todas as funcionalidades de 3.1 a 3.6 são acessíveis por argumentos;
- existe o comando `ajuda`, e um comando inválido também mostra a ajuda;
- a opção `--json` gera JSON válido;
- erros produzem mensagem clara e código de saída diferente de 0;
- a API usa as estruturas do próprio aluno, sem violar a seção 4;
- a API está documentada no relatório.

Se faltar algum desses pontos, o bônus conta como **não feito** para fins de conceito A.

---

## Como o conceito final é definido

| Conceito | Requisitos (todos obrigatórios) |
|---|---|
| **A** | Código **Excelente** · Clareza **Excelente** ou **Bom** · Documentação **Excelente** · Entregue **no prazo** · **Bônus feito** |
| **B** | Código pelo menos **Bom** · Clareza pelo menos **Bom** · Documentação pelo menos **Bom** · Entregue **no prazo** |
| **C** | Código pelo menos **Regular** · Clareza pelo menos **Regular** · Documentação pelo menos **Regular** |
| **D** | Não atinge os requisitos do conceito C, há cópia ou plágio, ou não foi entregue |

### Observações

- **Plágio:** cópia entre alunos ou duplas, ou de fontes externas sem citação, resulta em **D** para todos os envolvidos.
- **Execução:** o professor pode pedir que o aluno explique trechos do código. Se o aluno não souber explicar o próprio código, o conceito pode ser revisto.
- **Duplas:** os dois integrantes recebem o mesmo conceito.
