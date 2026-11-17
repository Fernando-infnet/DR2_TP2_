"""Exercício 3 — Primeiro valor duplicado em O(N)."""
from hash_table import HashTable


def primeiro_duplicado(arr):
    """Retorna (valor duplicado, acessos). Para na primeira repetição detectada."""
    vistos = HashTable()
    for s in arr:
        if vistos.contains(s):
            return s, vistos.acessos
        vistos.put(s, True)
    return None, vistos.acessos


if __name__ == "__main__":
    testes = [(["maçã", "banana", "laranja", "uva", "banana", "pera"], "banana"),
              (["x", "y", "y"], "y"),
              (["a", "b", "c", "d", "a"], "a"),
              (["Python", "python", "Java", "C", "Java"], "Java"),   # diferencia maiúsculas
              (["", "a", ""], "")]
    for arr, esperado in testes:
        valor, acessos = primeiro_duplicado(arr)
        assert valor == esperado
        print(f"{str(arr):58} -> {valor!r:9} ({acessos} acessos)")

    print()
    for n in [1_000, 10_000, 100_000]:
        arr = [f"id{i}" for i in range(n)] + ["id0"]    # duplicata só no fim = pior caso
        valor, acessos = primeiro_duplicado(arr)
        assert valor == "id0" and acessos == 2 * n + 1
        print(f"N = {n + 1:>7,}: {acessos:>8,} acessos (= 2N + 1)")
