# DR2 · TP2 — Estruturas de Dados e Algoritmos

Resolução dos 12 exercícios, em dois formatos com o mesmo código:

- [`DR2_TP2.ipynb`](DR2_TP2.ipynb): notebook executado, com notas curtas (decisão técnica e Big O) e as saídas reais.
- [`python/`](python): um arquivo por exercício, cada um executável.

```bash
python run_all.py            # roda todos os exercícios em sequência, com resumo no fim
python run_all.py --quiet    # só o resumo (OK/FALHA e tempo de cada um)
python python/ex01_maior_unico.py      # ou um exercício isolado
```

| Arquivo | Exercício |
|---|---|
| `hash_table.py` | hash table própria (usada nos Ex. 1, 2, 3, 5) |
| `ex01_maior_unico.py` | maior número único: `N²` → `N` |
| `ex02_interseccao.py` | interseção de arrays em `O(N+M)` |
| `ex03_primeiro_duplicado.py` | primeiro valor duplicado |
| `ex04_letra_ausente.py` | letra ausente do alfabeto |
| `ex05_primeiro_nao_repetido.py` | primeiro caractere não repetido |
| `ex06_selection_sort.py` | Selection Sort instrumentado |
| `ex07_insertion_sort.py` | Insertion Sort instrumentado |
| `ex08_pilha_ou_fila.py` | demonstração fila × pilha (justificativa no notebook) |
| `ex09_stack.py` | `Stack` com overflow/underflow |
| `ex10_queue.py` | `Queue` circular com ponteiros |
| `ex11_reverter_string.py` | reversão de string com pilha |
| `ex12_funcoes_hash.py` | análise de `h1`, `h2`, `h3` com `M = 10` |

Só biblioteca padrão. Os `assert` de cada script comparam as medições com as fórmulas teóricas.
