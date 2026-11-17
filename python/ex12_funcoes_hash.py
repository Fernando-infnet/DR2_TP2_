"""Exercício 12 — Distribuição das funções hash h1, h2, h3 com M = 10."""
import random

M = 10
FUNCOES = {"h1 = k mod 10": lambda k: k % M,
           "h2 = 7k mod 10": lambda k: (7 * k) % M,
           "h3 = k² mod 10": lambda k: (k * k) % M}


def distribuicao(chaves, h):
    """Carga de cada um dos M buckets."""
    carga = [0] * M
    for k in chaves:
        carga[h(k)] += 1
    return carga


def chi2(carga):
    """Desvio da distribuição uniforme (0 = perfeita)."""
    esperado = sum(carga) / M
    return sum((c - esperado) ** 2 / esperado for c in carga)


if __name__ == "__main__":
    print("Bucket de cada último dígito:")
    for nome, h in FUNCOES.items():
        mapa = [h(d) for d in range(10)]
        print(f"  {nome:15} {mapa}  buckets alcançáveis: {len(set(mapa))}")
    assert sorted(FUNCOES["h2 = 7k mod 10"](d) for d in range(10)) == list(range(10))   # h2 é permutação

    rng = random.Random(12)
    conjuntos = {"consecutivas 0..99": list(range(100)),
                 "múltiplos de 10": [10 * i for i in range(100)],
                 "pares": [2 * i for i in range(100)],
                 "aleatórias": [rng.randrange(10 ** 6) for _ in range(100)]}

    print(f"\n{'conjunto':>19} {'função':>8} {'usados':>6} {'maior carga':>11} {'χ²':>5}  carga por bucket")
    for nome_c, chaves in conjuntos.items():
        for nome_f, h in FUNCOES.items():
            carga = distribuicao(chaves, h)
            usados = sum(1 for c in carga if c)
            print(f"{nome_c:>19} {nome_f[:2]:>8} {usados:>6} {max(carga):>11} {chi2(carga):>5.0f}  {carga}")
