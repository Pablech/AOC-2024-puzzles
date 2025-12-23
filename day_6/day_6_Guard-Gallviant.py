import time, sys, os

MAPA = []
VISITADOS = set()


def imprime_mapa():
    sys.stdout.write("\033[H")

    for linha in MAPA:
        sys.stdout.write("".join(linha) + "\n")

    sys.stdout.flush()


def inicio() -> tuple[int, int]:
    indx_iniciais = ()

    for i in range(len(MAPA)):
        if '^' in MAPA[i]:
            indx_iniciais = (i, MAPA[i].index('^'))
            MAPA[int(indx_iniciais[0])][int(indx_iniciais[1])] = '▲'

    return indx_iniciais


def mover(movimento: str, atual: tuple[int, int], proximo: tuple[int, int]) -> bool:
    global MAPA, VISITADOS

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
            VISITADOS.add((proximo_i, proximo_j))
            return True
        except IndexError:
            MAPA[atual_i][atual_j] = marcacao
            return False


def part_1():
    global VISITADOS, MAPA

    i, j = inicio()
    VISITADOS.add((i, j))
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
            break

        avancar = mover(movimento=movimento, atual=atual, proximo=proximo)

        # DESCOMENTE AS DUAS PRÓXIMAS LINHAS PARA VER O GUARDA ANDANDO PELO MAPA
        # imprime_mapa()
        # time.sleep(0.03)


def main():
    global MAPA

    with open('mapa.txt', 'r', encoding='utf-8') as arquivo:
        MAPA = [list(linha) for linha in arquivo.read().splitlines()]

    os.system('cls' if os.name == 'nt' else 'clear')

    part_1()
    print(f'Total: {len(VISITADOS)}')


if __name__ == '__main__':
    main()
