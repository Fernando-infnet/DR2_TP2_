"""Exercício 4 — Letra ausente do alfabeto. Tempo O(N), espaço O(1)."""


def letras_ausentes(texto):
    presente = [False] * 26                    # estrutura auxiliar de tamanho fixo
    for ch in texto:                           # N iterações
        if "A" <= ch <= "Z":
            ch = chr(ord(ch) + 32)             # normaliza para minúscula
        if "a" <= ch <= "z":                   # ignora espaços, números, pontuação, acentos
            presente[ord(ch) - ord("a")] = True
    return [chr(ord("a") + i) for i in range(26) if not presente[i]]   # 26 iterações


if __name__ == "__main__":
    testes = [("The quick brown fox jumps over the lazy do", ["g"]),
              ("The quick brown fox jumps over the lazy dog", []),        # pangrama
              ("Pack my box with five dozen liquor jug!!! 123", ["s"]),
              ("  ABCDEFGHIJKLMNOPQRSTUVWXY  ", ["z"])]
    for texto, esperado in testes:
        r = letras_ausentes(texto)
        assert r == esperado
        print(f"{texto!r:50} -> ausentes: {r}")
