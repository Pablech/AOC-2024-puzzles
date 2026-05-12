import collections
import sys
import time
from functools import wraps


def medir_tempo(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.perf_counter()
        resultado = func(*args, **kwargs)
        fim = time.perf_counter()
        print(f'[TEMPO] {func.__name__} levou {fim - inicio:.4f} segundos.\n')
        return resultado
    return wrapper


def encontrar_caminho(grade, inicio, fim):
    global CACHE_CAMINHOS

    invalido = ' '
    linhas, colunas = len(grade), len(grade[0])
    inicio_str, fim_str = grade[inicio[0]][inicio[1]], grade[fim[0]][fim[1]]
    
    if (inicio_str, fim_str) in CACHE_CAMINHOS:
        return CACHE_CAMINHOS[(inicio_str, fim_str)]

    if inicio_str == invalido or fim_str == invalido:
        return []

    movimentos = {(-1, 0): '^', (1, 0): 'v', (0, -1): '<', (0, 1): '>'}
    direcoes = list(movimentos.keys())

    caminhos = []
    tamanho_minimo = float('inf')

    fila = collections.deque([(inicio, '', {inicio})])
    
    while fila:
        (linha, coluna), caminho, visitados = fila.popleft()

        if len(caminho) >= tamanho_minimo:
            continue

        for nl, nc in direcoes:
            prox_linha, prox_col = linha + nl, coluna + nc

            if not (0 <= prox_linha < linhas and 0 <= prox_col < colunas):
                continue
                
            if grade[prox_linha][prox_col] == invalido:
                continue

            if (prox_linha, prox_col) in visitados:
                continue

            novo_caminho = caminho + movimentos[(nl, nc)]
            novo_visitado = visitados | {(prox_linha, prox_col)}

            if grade[prox_linha][prox_col] == fim_str:
                if len(novo_caminho) < tamanho_minimo:
                    tamanho_minimo = len(novo_caminho)
                    caminhos = [novo_caminho + 'A']
                
                elif len(novo_caminho) == tamanho_minimo:
                    caminhos.append(novo_caminho + 'A')
                    
            else:
                if len(novo_caminho) < tamanho_minimo:
                    fila.append(((prox_linha, prox_col), novo_caminho, novo_visitado))

    if not caminhos:
        if inicio == fim:
            caminhos = ['A']
        
    CACHE_CAMINHOS[(inicio_str, fim_str)] = caminhos
    return caminhos


def calcular_custo(inicio, fim, profundidade, max_profundidade):
    global CACHE_ROBOS

    chave_cache = (inicio, fim, profundidade)

    if chave_cache in CACHE_ROBOS[profundidade]:
        return CACHE_ROBOS[profundidade][chave_cache]

    caminhos = encontrar_caminho(GRADE_CURSOR, NOS_CURSOR[inicio], NOS_CURSOR[fim])

    if profundidade == max_profundidade - 1:
        resultado = len(caminhos[0])
    else:
        melhor_custo = float('inf')
        for caminho in caminhos:
            custo_atual = 0
            caminho = 'A' + caminho
            for i in range(len(caminho) - 1):
                custo_atual += calcular_custo(caminho[i], caminho[i + 1], profundidade + 1, max_profundidade)
            
            melhor_custo = min(melhor_custo, custo_atual)
        
        resultado = melhor_custo

    CACHE_ROBOS[profundidade][chave_cache] = resultado
    return resultado


def entrada():
    max_profundidade = 2
    
    if len(sys.argv) > 1:
        try:
            max_profundidade = int(sys.argv[1])
            if max_profundidade > 996:
                max_profundidade = 966
                print(f'Número máximo de profundidade é: 966\nRodando com: {max_profundidade}')
        except ValueError:
            print(f'Aviso: {sys.argv[1]} inválido.\nRodando com: {max_profundidade}')

    return max_profundidade


@medir_tempo
def main(codes, max_profundidade):    
    total = 0

    for code in codes:
        code_int = int(code.replace('A', ''))
        code = 'A' + code
        custo_code = 0

        for i in range(len(code) - 1):
            inicio, fim = code[i], code[i + 1]
            caminhos_teclado = encontrar_caminho(GRADE_TECLADO, NOS_TECLADO[inicio], NOS_TECLADO[fim])

            custos_caminhos = []
            for c in caminhos_teclado:
                c = 'A' + c
                soma = 0

                for j in range(len(c) - 1):
                    soma += calcular_custo(c[j], c[j + 1], 0, max_profundidade)
                
                custos_caminhos.append(soma)

            custo_code += min(custos_caminhos)

        total += custo_code * code_int
    
    print(f'\nValor total: {total}\nPara {max_profundidade} de profundidade.')


if __name__ == '__main__':
    global GRADE_TECLADO, GRADE_CURSOR, NOS_TECLADO, NOS_CURSOR, CACHE_ROBOS, CACHE_CAMINHOS

    max_profundidade = entrada()
    dados = [' ^A<v>', '789456123 0A']

    CACHE_CAMINHOS = {}
    CACHE_ROBOS = [{} for _ in range(max_profundidade + 1)]

    GRADE_TECLADO = [list(dados[1][i : i + 3]) for i in range(0, len(dados[1]), 3)]
    GRADE_CURSOR = [list(dados[0][i : i + 3]) for i in range(0, len(dados[0]), 3)]

    NOS_TECLADO = {GRADE_TECLADO[i][j]: (i, j) for i in range(len(GRADE_TECLADO)) 
                    for j in range(len(GRADE_TECLADO[0])) if GRADE_TECLADO[i][j] != ' '}
    NOS_CURSOR = {GRADE_CURSOR[i][j]: (i, j) for i in range(len(GRADE_CURSOR)) 
                    for j in range(len(GRADE_CURSOR[0])) if GRADE_CURSOR[i][j] != ' '}

    with open('input.txt', 'r', encoding='utf-8') as f:
        codes = [linha.strip() for linha in f.readlines()]

    main(codes, max_profundidade)