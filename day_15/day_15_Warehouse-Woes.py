import time, os
from rich.console import Console

console = Console()


def imprimir_mapa(mapa: list[list[str]]):
    # print("\033[H", end="")

    mapping = {
        '#': "[blue]#[/blue]",
        '@': "[bold red]@[/bold red]",
        'O': "[green]O[/green]",
        '.': "[grey15]*[/grey15]",
        '[': "[green][[/green]",
        ']': "[green]][/green]"
    }

    for linha in mapa:
        line = "".join(mapping.get(c, c) for c in linha)
        console.print(line)


def gps(mapa: list[list[str]]) -> int:
    total = 0

    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if mapa[i][j] == 'O':
                total += i * 100 + j

    return total


def mover(mapa: list[list[str]], movimentos: str, bot_indx: tuple[int, int], parte_2: bool = False):
    bot_str, vazio, caixa, obstaculo = '@', '.', 'O' if not parte_2 else '[]', '#'
    dict_movimentos = {
        '<': (0, -1),
        '^': (-1, 0),
        '>': (0, +1),
        'v': (+1, 0)
    }

    for m in movimentos:
        # imprimir_mapa(mapa)
        # time.sleep(0.1)

        mi, mj = dict_movimentos[m]
        i, j = bot_indx[0], bot_indx[1]
        prox_i, prox_j = mi + i, mj + j

        if mapa[prox_i][prox_j] == obstaculo:
            continue

        elif mapa[prox_i][prox_j] == vazio:
            mapa[prox_i][prox_j], mapa[i][j] = bot_str, vazio
            bot_indx = (prox_i, prox_j)

        elif mapa[prox_i][prox_j] == caixa:
            temp_i, temp_j = prox_i, prox_j
            while mapa[temp_i][temp_j] == caixa:
                temp_i += mi
                temp_j += mj

            if mapa[temp_i][temp_j] == vazio:
                mapa[temp_i][temp_j], mapa[i][j], mapa[prox_i][prox_j] = caixa, vazio, bot_str
                bot_indx = (prox_i, prox_j)

            elif mapa[temp_i][temp_j] == obstaculo:
                continue


def main():
    with open('input.txt', 'r', encoding='utf-8') as f:
        dados = f.read().split('\n\n')

    mapa = [[l for l in linha] for linha in dados[0].strip().split()]
    movimentos = dados[1].replace('\n', '')

    index_robo = tuple
    for i in range(len(mapa)):
        if '@' in mapa[i]:
            index_robo = (i, mapa[i].index('@'))

    os.system('cls' if os.name == 'nt' else 'clear')
    mover(mapa, movimentos, index_robo)
    print(gps(mapa))


if __name__ == '__main__':
    main()
