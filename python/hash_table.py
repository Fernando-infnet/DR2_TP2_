"""Tabela hash própria: encadeamento separado, capacidade prima, fator de carga <= 0,75."""


def _proximo_primo(n):
    while True:
        if n >= 2 and all(n % d for d in range(2, int(n ** 0.5) + 1)):
            return n
        n += 1


class HashTable:
    def __init__(self, capacidade=17, fator_max=0.75):
        self.capacidade = capacidade
        self.fator_max = fator_max
        self.buckets = [[] for _ in range(capacidade)]
        self.tamanho = 0
        self.acessos = 0                       # nº de put/get/contains

    @staticmethod
    def _hash(chave):
        if isinstance(chave, str):             # hash polinomial para strings
            h = 0
            for ch in chave:
                h = (h * 31 + ord(ch)) & 0xFFFFFFFF
            return h
        return chave                           # inteiros: o próprio valor

    def _bucket(self, chave):
        return self.buckets[self._hash(chave) % self.capacidade]

    def put(self, chave, valor):
        self.acessos += 1
        bucket = self._bucket(chave)
        for par in bucket:
            if par[0] == chave:
                par[1] = valor
                return
        bucket.append([chave, valor])
        self.tamanho += 1
        if self.tamanho / self.capacidade > self.fator_max:
            self._redimensionar()

    def get(self, chave, padrao=None):
        self.acessos += 1
        for k, v in self._bucket(chave):
            if k == chave:
                return v
        return padrao

    def contains(self, chave):
        self.acessos += 1
        return any(k == chave for k, _ in self._bucket(chave))

    def _redimensionar(self):                  # custo amortizado O(1) por inserção
        antigos = self.buckets
        self.capacidade = _proximo_primo(self.capacidade * 2)
        self.buckets = [[] for _ in range(self.capacidade)]
        for bucket in antigos:
            for k, v in bucket:
                self.buckets[self._hash(k) % self.capacidade].append([k, v])


if __name__ == "__main__":
    t = HashTable()
    for i in range(1000):
        t.put(i * 16, i)
    assert t.tamanho == 1000 and all(t.get(i * 16) == i for i in range(1000))
    assert not t.contains(5) and t.contains(32)
    print("HashTable OK | capacidade final:", t.capacidade)
