"""Executa todos os scripts de python/ em ordem e resume o resultado.

Uso:  python run_all.py            (mostra a saída completa de cada exercício)
      python run_all.py --quiet    (mostra só o resumo)
"""
import subprocess
import sys
import time
from pathlib import Path

PASTA = Path(__file__).parent / "python"
quiet = "--quiet" in sys.argv

scripts = sorted(PASTA.glob("ex*.py"))
scripts.insert(0, PASTA / "hash_table.py")           # infraestrutura primeiro

resultados = []
for script in scripts:
    print(f"\n{'=' * 70}\n{script.name}\n{'=' * 70}")
    ini = time.perf_counter()
    proc = subprocess.run([sys.executable, str(script)], capture_output=True, text=True, cwd=PASTA)
    seg = time.perf_counter() - ini
    if not quiet or proc.returncode != 0:
        print(proc.stdout, end="")
        print(proc.stderr, end="", file=sys.stderr)
    resultados.append((script.name, proc.returncode == 0, seg))

print(f"\n{'=' * 70}\nRESUMO\n{'=' * 70}")
for nome, ok, seg in resultados:
    print(f"{'OK  ' if ok else 'FALHA'}  {nome:32} {seg:6.2f}s")
falhas = sum(1 for _, ok, _ in resultados if not ok)
print(f"\n{len(resultados) - falhas}/{len(resultados)} scripts passaram.")
sys.exit(1 if falhas else 0)
