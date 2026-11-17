"""Exercício 10 — Fila (Queue) circular de capacidade fixa, com ponteiros de início e fim.

O contador de tamanho distingue fila cheia de fila vazia (nos dois casos inicio == fim).
"""


class QueueOverflowError(Exception):
    pass


class QueueUnderflowError(Exception):
    pass


class Queue:
    def __init__(self, capacidade):
        self._capacidade = capacidade
        self._dados = [None] * capacidade
        self._inicio = 0                       # próximo a sair
        self._fim = 0                          # próxima posição livre
        self._tamanho = 0

    def tamanho(self):
        return self._tamanho

    def esta_vazia(self):
        return self._tamanho == 0

    def esta_cheia(self):
        return self._tamanho == self._capacidade

    def enqueue(self, item):
        if self.esta_cheia():
            raise QueueOverflowError(f"fila cheia; {item!r} não inserido")
        self._dados[self._fim] = item
        self._fim = (self._fim + 1) % self._capacidade
        self._tamanho += 1

    def dequeue(self):
        if self.esta_vazia():
            raise QueueUnderflowError("fila vazia; nada a remover")
        item = self._dados[self._inicio]
        self._dados[self._inicio] = None
        self._inicio = (self._inicio + 1) % self._capacidade
        self._tamanho -= 1
        return item

    def estado(self):
        return (f"dados={self._dados} inicio={self._inicio} fim={self._fim} "
                f"tamanho={self._tamanho}/{self._capacidade}")


if __name__ == "__main__":
    fila = Queue(4)
    entraram, sairam = [], []
    print("criada:", fila.estado())
    roteiro = ["deq", "A", "B", "C", "D", "E", "deq", "deq", "F", "G", "deq", "deq", "deq", "deq", "deq"]
    for passo in roteiro:
        antes = fila.estado()
        try:
            if passo == "deq":
                x = fila.dequeue()
                sairam.append(x)
                print(f"dequeue() -> {x!r}")
            else:
                fila.enqueue(passo)
                entraram.append(passo)
                print(f"enqueue({passo!r})")
        except (QueueOverflowError, QueueUnderflowError) as e:
            print(f"{'dequeue()' if passo == 'deq' else f'enqueue({passo!r})'} ERRO {type(e).__name__}: {e}")
            assert fila.estado() == antes
        print("           ", fila.estado())

    print("\nEntraram:", entraram)
    print("Saíram:  ", sairam)
    assert entraram == sairam
    print("FIFO validado: ordem de saída = ordem de entrada.")
