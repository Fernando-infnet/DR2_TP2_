"""Exercício 8 — Demonstração: atendimento por ordem de chegada com fila x pilha."""
from ex09_stack import Stack
from ex10_queue import Queue


if __name__ == "__main__":
    chegadas = ["R1", "R2", "R3", "R4", "R5"]
    fila, pilha = Queue(len(chegadas)), Stack(len(chegadas))
    for r in chegadas:
        fila.enqueue(r)
        pilha.push(r)
    ordem_fila = [fila.dequeue() for _ in chegadas]
    ordem_pilha = [pilha.pop() for _ in chegadas]
    print("Chegada:        ", chegadas)
    print("Atendido (FILA):", ordem_fila)
    print("Atendido (PILHA):", ordem_pilha)
    assert ordem_fila == chegadas and ordem_pilha != chegadas
