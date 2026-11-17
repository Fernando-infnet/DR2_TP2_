"""Exercício 5 — Primeiro caractere não repetido em O(N)."""
from hash_table import HashTable


def primeiro_nao_repetido(texto):
    """Retorna (caractere ou None, acessos)."""
    freq = HashTable()
    for ch in texto:                           # fase 1: contagem de frequência
        freq.put(ch, freq.get(ch, 0) + 1)
    for ch in texto:                           # fase 2: ordem original preservada
        if freq.get(ch) == 1:
            return ch, freq.acessos
    return None, freq.acessos


if __name__ == "__main__":
    testes = [("swiss", "w"), ("stress", "t"), ("abcabcd", "d"), ("aabbcc", None),
              ("", None), ("x", "x"), ("Aa", "A"), ("hello world", "h")]
    for texto, esperado in testes:
        r, acessos = primeiro_nao_repetido(texto)
        assert r == esperado
        print(f"{texto!r:14} -> {r!r:5} ({acessos} acessos)")

    texto = "abcdefghij" * 50_000 + "Z"                       # resposta no fim = pior caso
    r, acessos = primeiro_nao_repetido(texto)
    assert r == "Z" and acessos == 3 * len(texto)
    print(f"\nN = {len(texto):,}: {acessos:,} acessos (= 3N)")
