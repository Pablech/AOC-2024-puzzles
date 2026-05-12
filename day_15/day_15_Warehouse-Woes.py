import time, os, sys
from rich.console import Console

console = Console()


def imprimir_mapa(mapa: list[list[str]], interface: bool = False):
    if interface:
        print("\033[H", end="")
        time.sleep(0.1)

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


def gps(mapa: list[list[str]], part_2: bool = False) -> int:
    total = 0

    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if not part_2 and mapa[i][j] == 'O':
                total += i * 100 + j
            if part_2 and mapa[i][j] == '[':
                total += i * 100 + j

    return total


def mover_caixa_part_2(mapa: list[list[str]], i: int, j: int, direcao: tuple[int, int], dir_str: str) -> tuple[
    int, int]:
    bot_str, vazio, caixa, obstaculo = '@', '.', ('[', ']'), '#'
    mi, mj = direcao

    if dir_str in '<>':
        temp_i, temp_j = i, j
        while mapa[temp_i][temp_j] not in caixa:
            temp_i += mi
            temp_j += mj

        if mapa[temp_i][temp_j] == vazio:
            while temp_j > j:
                mapa[temp_i][temp_j] = caixa[1]
                temp_j -= mj
                mapa[temp_i][temp_j] = caixa[0]
                temp_j -= mj
            return mi, mj

        if mapa[temp_i][temp_j] == obstaculo:
            return i, j

    else:
        temp_i, temp_j = i, j
        if dir_str in '^v' and mapa[temp_i][temp_j] == caixa[0]:
            while mapa[temp_i][temp_j] not in caixa and mapa[temp_i][temp_j + 1] not in caixa:
                temp_i += mi
                temp_j += mj

            if mapa[temp_i][temp_j] == vazio and mapa[temp_i][temp_j + 1] == vazio:
                mapa[i][j], mapa[i + mi][j + mj], mapa[temp_i][temp_j], mapa[temp_i][temp_j + 1] = vazio, bot_str, \
                caixa[0], caixa[1]
                return i + mi, j + mj

            if mapa[temp_i][temp_j] == obstaculo:
                return i, j

        if dir_str in '^v' and mapa[temp_i][temp_j] == caixa[1]:
            while mapa[temp_i][temp_j - 1] not in caixa and mapa[temp_i][temp_j] not in caixa:
                temp_i += mi
                temp_j += mj

            if mapa[temp_i][temp_j - 1] == vazio and mapa[temp_i][temp_j] == vazio:
                mapa[i][j], mapa[i + mi][j + mj], mapa[temp_i][temp_j - 1], mapa[temp_i][temp_j] = vazio, bot_str, \
                caixa[0], caixa[1]
                return i + mi, j + mj

            if mapa[temp_i][temp_j] == obstaculo:
                return i, j

    return i, j


def mover_caixa_part_1(mapa: list[list[str]], i: int, j: int, direcao: tuple[int, int]) -> tuple[int, int]:
    bot_str, vazio, caixa, obstaculo = '@', '.', 'O', '#'
    mi, mj = direcao

    temp_i, temp_j = i, j
    while mapa[temp_i][temp_j] == caixa:
        temp_i += mi
        temp_j += mj

    if mapa[temp_i][temp_j] == vazio:
        mapa[temp_i][temp_j], mapa[i - mi][j - mj], mapa[i][j] = caixa, vazio, bot_str

    elif mapa[temp_i][temp_j] == obstaculo:
        return i - mi, j - mj

    return i, j


def mover(mapa: list[list[str]], movimentos: str, bot_indx: tuple[int, int], parte_2: bool = False,
          interface: bool = False):
    bot_str, vazio, caixa, obstaculo = '@', '.', 'O' if not parte_2 else '[]', '#'
    dict_movimentos = {
        '<': (0, -1),
        '^': (-1, 0),
        '>': (0, +1),
        'v': (+1, 0)
    }

    for m in movimentos:
        mi, mj = dict_movimentos[m]
        i, j = bot_indx[0], bot_indx[1]
        prox_i, prox_j = mi + i, mj + j

        if mapa[prox_i][prox_j] == obstaculo:
            continue

        elif mapa[prox_i][prox_j] == vazio:
            mapa[prox_i][prox_j], mapa[i][j] = bot_str, vazio
            bot_indx = (prox_i, prox_j)

        elif not parte_2 and mapa[prox_i][prox_j] == caixa:
            bot_indx = mover_caixa_part_1(mapa, prox_i, prox_j, dict_movimentos[m])

        elif parte_2 and mapa[prox_i][prox_j] in caixa:
            bot_indx = mover_caixa_part_2(mapa, prox_i, prox_j, dict_movimentos[m], m)

        if interface:
            imprimir_mapa(mapa, interface)


def main():
    modo = sys.argv[1] if len(sys.argv) > 1 else 'resultado'
    parte = True if '--part2' in sys.argv else False
    
    with open('input.txt', 'r', encoding='utf-8') as f:
        dados = f.read().split('\n\n')

    mapa = [[l for l in linha] for linha in dados[0].strip().split()]
    movimentos = dados[1].replace('\n', '')

    mapa_2 = ''
    if parte:
        for i in range(len(mapa)):
            for j in range(len(mapa[i])):
                if mapa[i][j] == '@':
                    mapa_2 += '@.'
                elif mapa[i][j] == '.':
                    mapa_2 += '..'
                elif mapa[i][j] == '#':
                    mapa_2 += '##'
                elif mapa[i][j] == 'O':
                    mapa_2 += '[]'
            mapa_2 += '\n'
        mapa = [[l for l in linha] for linha in mapa_2.strip().split()]

    index_robo = tuple
    for i in range(len(mapa)):
        if '@' in mapa[i]:
            index_robo = (i, mapa[i].index('@'))

    if modo == '--gui':
        os.system('cls' if os.name == 'nt' else 'clear')
        mover(mapa, movimentos, index_robo, parte, True)
    elif modo == '--map':
        mover(mapa, movimentos, index_robo, parte)
        imprimir_mapa(mapa)
    else:
        mover(mapa, movimentos, index_robo, parte)

    print(f'Resultado: {gps(mapa, parte)}')


if __name__ == '__main__':
    main()
