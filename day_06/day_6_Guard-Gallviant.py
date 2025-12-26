import time, sys, os

MAPA = []
VISITADOS_PART_1 = []
VISITADOS_PART_2 = []


def imprime_mapa():
    sys.stdout.write('\033[H')

    for linha in MAPA:
        sys.stdout.write(''.join(linha) + '\n')

    sys.stdout.flush()


def inicio() -> tuple[int, int]:
    global MAPA

    indx_iniciais = ()

    for i in range(len(MAPA)):
        if '^' in MAPA[i]:
            indx_iniciais = (i, MAPA[i].index('^'))
            MAPA[indx_iniciais[0]][indx_iniciais[1]] = '▲'

    return indx_iniciais


def mover(movimento: str, atual: tuple[int, int], proximo: tuple[int, int]) -> bool:
    global MAPA, VISITADOS_PART_1, VISITADOS_PART_2

    atual_i, atual_j = atual
    proximo_i, proximo_j = proximo
    marcacao = '✗'
    movimentos = ['▲', '▶', '▼', '◀']
    movimento_atual = movimentos.index(movimento)

    if MAPA[proximo_i][proximo_j] == '#':
        if movimento_atual + 1 <= 3:
            MAPA[atual_i][atual_j] = movimentos[movimento_atual + 1]
        else:
            MAPA[atual_i][atual_j] = movimentos[0]
        return True
    else:
        try:
            MAPA[proximo_i][proximo_j] = movimentos[movimento_atual]
            MAPA[atual_i][atual_j] = marcacao
            VISITADOS_PART_1.append((proximo_i, proximo_j))
            VISITADOS_PART_2.append((MAPA[atual_i][atual_j], atual_i, atual_i))
            return True
        except IndexError:
            return False


def part_1():
    global VISITADOS_PART_1, MAPA, VISITADOS_PART_2

    i, j = inicio()
    VISITADOS_PART_1.append((i, j))
    VISITADOS_PART_2.append((MAPA[i][j], i, j))
    avancar = True
    atual, proximo = (), ()

    while avancar:
        movimento = MAPA[i][j]
        atual = (i, j)
        if movimento == '▲':
            proximo = (i - 1, j)

        if movimento == '▶':
            proximo = (i, j + 1)

        if movimento == '▼':
            proximo = (i + 1, j)

        if movimento == '◀':
            proximo = (i, j - 1)

        i, j = proximo
        try:
            if MAPA[i][j] == '#':
                i, j = atual
        except IndexError:
            i, j = atual
            MAPA[i][j] = '✗'
            break

        avancar = mover(movimento=movimento, atual=atual, proximo=proximo)

        # DESCOMENTE PARA VER O GUARDA ANDANDO PELO MAPA
        # imprime_mapa()
        # time.sleep(0.03)


def main():
    global MAPA

    with open('input.txt', 'r', encoding='utf-8') as arquivo:
        MAPA = [list(linha) for linha in arquivo.read().splitlines()]

    os.system('cls' if os.name == 'nt' else 'clear')

    part_1()
    print(f'Total part 1: {len(set(VISITADOS_PART_1))}')

if __name__ == '__main__':
    main()
