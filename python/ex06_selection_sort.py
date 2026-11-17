"""Exercício 6 — Selection Sort instrumentado."""
import random


def selection_sort(lista):
    """Retorna (lista ordenada, comparações, trocas)."""
    a = list(lista)
    comparacoes = trocas = 0
    for i in range(len(a) - 1):
        menor = i
        for j in range(i + 1, len(a)):
            comparacoes += 1
            if a[j] < a[menor]:
                menor = j
        if menor != i:
            a[i], a[menor] = a[menor], a[i]
            trocas += 1
    return a, comparacoes, trocas


def gerar_cenarios(n, seed=7):
    """Cinco estados iniciais para o mesmo N."""
    rng = random.Random(seed)
    quase = list(range(n))
    for _ in range(10):                        # 10 trocas curtas
        i = rng.randrange(n - 3)
        j = i + rng.randint(1, 3)
        quase[i], quase[j] = quase[j], quase[i]
    return {"ordenada": list(range(n)), "quase ordenada": quase,
            "aleatória": rng.sample(range(10 * n), n), "invertida": list(range(n, 0, -1)),
            "muitos duplicados": [rng.randint(0, 9) for _ in range(n)]}


if __name__ == "__main__":
    N = 1000
    print(f"{'estado inicial':>18} | {'comparações':>11} | {'trocas':>6}")
    for nome, lista in gerar_cenarios(N).items():
        saida, comps, trocas = selection_sort(lista)
        assert saida == sorted(lista)                        # sorted() só para conferir
        assert comps == N * (N - 1) // 2 and trocas <= N - 1
        print(f"{nome:>18} | {comps:>11,} | {trocas:>6}")
