"""Exercício 2 — Interseção de arrays em O(N + M) com hash table."""
import random
from hash_table import HashTable


def interseccao_quadratica(a, b):
    """Linha de base O(N·M). Retorna (resultado, comparações)."""
    comps, resultado = 0, []
    for x in b:
        achou = False
        for y in a:
            comps += 1
            if x == y:
                achou = True
                break
        if achou:
            repetido = False
            for r in resultado:
                comps += 1
                if r == x:
                    repetido = True
                    break
            if not repetido:
                resultado.append(x)
    return resultado, comps


def interseccao_hash(a, b):
    """Retorna (resultado, acessos). Sem funções prontas de interseção."""
    tabela = HashTable()
    for x in a:
        tabela.put(x, True)                    # N acessos
    resultado = []
    for y in b:
        if tabela.get(y) is True:              # M acessos
            resultado.append(y)
            tabela.put(y, False)               # marca: não repete no resultado
    return resultado, tabela.acessos


if __name__ == "__main__":
    for a, b, esperado in [([1, 2, 3, 4], [3, 4, 5, 6], [3, 4]),
                           ([1, 2, 2, 3], [2, 2, 3, 3, 9], [2, 3]),
                           ([], [1], []), (["a", "b"], ["b", "z"], ["b"])]:
        assert interseccao_quadratica(a, b)[0] == interseccao_hash(a, b)[0] == esperado
    print("Casos pequenos OK\n")

    print(f"{'N = M':>6} | {'comparações O(N·M)':>19} | {'acessos hash':>12}")
    for n in [200, 1000, 2000]:
        a, b = list(range(n)), list(range(n // 2, n // 2 + n))
        random.shuffle(b)
        (r1, comps), (r2, acessos) = interseccao_quadratica(a, b), interseccao_hash(a, b)
        assert r1 == r2 and len(r2) == n // 2 and acessos <= 3 * n
        print(f"{n:>6} | {comps:>19,} | {acessos:>12,}")

    # Validação em escala: resposta conhecida por construção ([N/2, N)), sem usar set
    N = 200_000
    a, b = list(range(N)), list(range(N // 2, N // 2 + N))
    random.shuffle(a); random.shuffle(b)
    resultado, acessos = interseccao_hash(a, b)
    marcado = [False] * N
    for r in resultado:
        assert N // 2 <= r < N and not marcado[r]
        marcado[r] = True
    assert len(resultado) == N // 2
    print(f"\nN = M = {N:,}: interseção com {len(resultado):,} elementos, {acessos:,} acessos (≤ 3N). OK")
