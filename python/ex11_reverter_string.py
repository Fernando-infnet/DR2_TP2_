"""Exercício 11 — Reversão de string com pilha (sem slicing nem reversed)."""
from ex09_stack import Stack


def inverter_string(texto, verbose=False):
    pilha = Stack(max(1, len(texto)))
    for ch in texto:                           # empilha cada caractere
        pilha.push(ch)
        if verbose:
            print(f"  push({ch!r})  {pilha.estado()}")
    saida = []
    while not pilha.esta_vazia():              # desempilha até esvaziar
        ch = pilha.pop()
        saida.append(ch)
        if verbose:
            print(f"  pop() -> {ch!r}  {pilha.estado()}")
    return "".join(saida)


if __name__ == "__main__":
    print("Rastro para 'Pilha':")
    assert inverter_string("Pilha", verbose=True) == "ahliP"
    print()
    for s in ["Python", "", "a", "arara", "Estruturas de Dados", "ação é útil"]:
        r = inverter_string(s)
        n = len(s)
        assert len(r) == n and all(r[i] == s[n - 1 - i] for i in range(n))
        print(f"{s!r:24} -> {r!r}")
