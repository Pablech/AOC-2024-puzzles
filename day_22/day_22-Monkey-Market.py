import time
import os
from collections import defaultdict
from concurrent.futures import ProcessPoolExecutor

def proximo_segredo(n):
    n = (n ^ (n * 64)) % 16777216
    n = (n ^ (n // 32)) % 16777216
    n = (n ^ (n * 2048)) % 16777216
    return n

def processar_chunk(numeros_chunk):
    local_bananas = defaultdict(int)
    total_p1 = 0
    
    for n in numeros_chunk:
        precos = [n % 10]
        for _ in range(2000):
            n = proximo_segredo(n)
            precos.append(n % 10)
        total_p1 += n
        
        vistos = set()
        for i in range(len(precos) - 4):
            v1, v2 = precos[i+1]-precos[i], precos[i+2]-precos[i+1]
            v3, v4 = precos[i+3]-precos[i+2], precos[i+4]-precos[i+3]
            seq_id = (v1+9) + (v2+9)*20 + (v3+9)*400 + (v4+9)*8000
            
            if seq_id not in vistos:
                local_bananas[seq_id] += precos[i+4]
                vistos.add(seq_id)
                
    return total_p1, local_bananas

def main():
    with open('input.txt', 'r') as f:
        numeros = [int(line) for line in f if line.strip()]

    inicio = time.perf_counter()
    
    nucleos = os.cpu_count()
    chunk_size = len(numeros) // (nucleos // 2)
    chunks = [numeros[i:i + chunk_size] for i in range(0, len(numeros), chunk_size)]

    total_bananas_global = defaultdict(int)
    total_p1_global = 0

    with ProcessPoolExecutor(max_workers=nucleos) as executor:
        resultados = executor.map(processar_chunk, chunks)
        
        for p1_parcial, dict_parcial in resultados:
            total_p1_global += p1_parcial
            for seq_id, valor in dict_parcial.items():
                total_bananas_global[seq_id] += valor

    fim = time.perf_counter()
    
    print(f"Parte 1: {total_p1_global}")
    print(f"Parte 2: {max(total_bananas_global.values())}")
    print(f"Tempo total: {fim - inicio:.4f}s")

if __name__ == '__main__':
    main()