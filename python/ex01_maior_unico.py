"""Exercício 1 — Maior número único: laços aninhados O(N²) x hash table O(N)."""
import random
from hash_table import HashTable


def maior_unico_quadratico(lista):
    """Retorna (resultado, comparações)."""
    comparacoes = 0
    melhor = None
    for i in range(len(lista)):
        unico = True
        for j in range(len(lista)):
            if i != j:
                comparacoes += 1
                if lista[i] == lista[j]:
                    unico = False
                    break
        if unico:
            if melhor is None:
                melhor = lista[i]
            else:
                comparacoes += 1
                if lista[i] > melhor:
                    melhor = lista[i]
    return melhor, comparacoes


def maior_unico_hash(lista):
    """Retorna (resultado, acessos à hash table)."""
    freq = HashTable()
    for x in lista:                            # 1ª passada: 2 acessos por elemento
        freq.put(x, freq.get(x, 0) + 1)
    melhor = None
    for x in lista:                            # 2ª passada: 1 acesso por elemento
        if freq.get(x) == 1 and (melhor is None or x > melhor):
            melhor = x
    return melhor, freq.acessos


if __name__ == "__main__":
    for lista, esperado in [([4, 1, 2, 2, 4, 7, 7, 3], 3), ([5, 5], None), ([], None), ([9], 9)]:
        assert maior_unico_quadratico(lista)[0] == maior_unico_hash(lista)[0] == esperado
    print("Casos pequenos OK\n")

    random.seed(42)
    print(f"{'N':>6} | {'comparações O(N²)':>18} | {'acessos hash':>12}")
    for n in [100, 500, 1000, 2000, 5000]:
        lista = random.sample(range(10 * n), n)          # todos únicos = pior caso
        r1, comps = maior_unico_quadratico(lista)
        r2, acessos = maior_unico_hash(lista)
        assert r1 == r2 == max(lista)
        assert comps == n * n - 1 and acessos == 3 * n   # fórmulas teóricas
        print(f"{n:>6} | {comps:>18,} | {acessos:>12,}")
