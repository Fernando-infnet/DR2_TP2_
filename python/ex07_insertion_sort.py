"""Exercício 7 — Insertion Sort instrumentado e comparação com o Selection Sort."""
from ex06_selection_sort import selection_sort, gerar_cenarios


def insertion_sort(lista):
    """Retorna (lista ordenada, comparações, deslocamentos)."""
    a = list(lista)
    comparacoes = deslocamentos = 0
    for i in range(1, len(a)):
        chave = a[i]
        j = i - 1
        while j >= 0:
            comparacoes += 1
            if a[j] > chave:
                a[j + 1] = a[j]                # desloca para a direita
                deslocamentos += 1
                j -= 1
            else:
                break
        a[j + 1] = chave
    return a, comparacoes, deslocamentos


if __name__ == "__main__":
    N = 1000
    print(f"{'estado inicial':>18} | {'Insertion: comps':>16} | {'deslocs':>8} | {'Selection: comps':>16}")
    resultados = {}
    for nome, lista in gerar_cenarios(N).items():
        saida, comps, desl = insertion_sort(lista)
        assert saida == sorted(lista)
        resultados[nome] = (comps, desl)
        print(f"{nome:>18} | {comps:>16,} | {desl:>8,} | {selection_sort(lista)[1]:>16,}")

    assert resultados["ordenada"] == (N - 1, 0)                                  # melhor caso
    assert resultados["invertida"] == (N * (N - 1) // 2, N * (N - 1) // 2)       # pior caso
    print("\nMelhor caso (ordenada): N-1 comparações, 0 deslocamentos.")
    print("Pior caso (invertida): N(N-1)/2 comparações e deslocamentos.")
