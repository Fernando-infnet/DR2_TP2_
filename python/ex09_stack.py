"""Exercício 9 — Pilha (Stack) de capacidade fixa com overflow/underflow explícitos.

O estado (array, índice do topo) fica encapsulado na instância e é alterado in-place:
nada é recriado a cada operação.
"""


class StackOverflowError(Exception):
    pass


class StackUnderflowError(Exception):
    pass


class Stack:
    def __init__(self, capacidade):
        self._capacidade = capacidade
        self._dados = [None] * capacidade
        self._topo = -1                        # -1 = pilha vazia

    def tamanho(self):
        return self._topo + 1

    def esta_vazia(self):
        return self._topo == -1

    def esta_cheia(self):
        return self._topo == self._capacidade - 1

    def push(self, item):
        if self.esta_cheia():
            raise StackOverflowError(f"pilha cheia; {item!r} não inserido")
        self._topo += 1
        self._dados[self._topo] = item

    def pop(self):
        if self.esta_vazia():
            raise StackUnderflowError("pilha vazia; nada a remover")
        item = self._dados[self._topo]
        self._dados[self._topo] = None
        self._topo -= 1
        return item

    def peek(self):
        if self.esta_vazia():
            raise StackUnderflowError("pilha vazia; sem topo")
        return self._dados[self._topo]

    def estado(self):
        return f"dados={self._dados} topo={self._topo} tamanho={self.tamanho()}/{self._capacidade}"


if __name__ == "__main__":
    pilha = Stack(3)
    print("criada:", pilha.estado())
    operacoes = [("pop()", pilha.pop), ("push(10)", lambda: pilha.push(10)),
                 ("push(20)", lambda: pilha.push(20)), ("push(30)", lambda: pilha.push(30)),
                 ("push(40)", lambda: pilha.push(40)), ("peek()", pilha.peek),
                 ("pop()", pilha.pop), ("pop()", pilha.pop), ("pop()", pilha.pop), ("pop()", pilha.pop)]
    for nome, op in operacoes:
        antes = pilha.estado()
        try:
            r = op()
            print(f"{nome:10} ok{'' if r is None else f' -> {r}'}")
        except (StackOverflowError, StackUnderflowError) as e:
            print(f"{nome:10} ERRO {type(e).__name__}: {e}")
            assert pilha.estado() == antes     # erro não altera o estado
        print("           ", pilha.estado())
