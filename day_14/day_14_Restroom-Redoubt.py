import re
import os


def imprimir(benders: list[list[int]], altura: int, largura: int, s: int):
    coordenadas = set()
    for bender in benders:
        x = (bender[0] + bender[2] * s) % largura
        y = (bender[1] + bender[3] * s) % altura
        coordenadas.add((x, y))

    matriz = [['#' if (x, y) in coordenadas else ' ' for x in range(largura)] for y in range(altura)]

    mapa = '\n'.join([''.join(linha) for linha in matriz])
    os.system('cls' if os.name == 'nt' else 'clear')

    print(mapa)


def part_2(benders: list[list[int]], altura: int, largura: int) -> int | None:
    def calcular_variancia(posicoes: list[int]) -> float:
        n = len(posicoes)
        if n == 0: return 0
        media = sum(posicoes) / n
        return sum((x - media) ** 2 for x in posicoes) / n

    min_var_x, tempo_x = float('inf'), 0
    min_var_y, tempo_y = float('inf'), 0

    for segundo in range(max(altura, largura)):
        if segundo < largura:
            seg_x = [(bender[0] + bender[2] * segundo) % largura for bender in benders]
            var_x = calcular_variancia(seg_x)
            if var_x < min_var_x:
                min_var_x, tempo_x = var_x, segundo

        if segundo < largura:
            seg_y = [(bender[1] + bender[3] * segundo) % largura for bender in benders]
            var_y = calcular_variancia(seg_y)
            if var_y < min_var_y:
                min_var_y, tempo_y = var_y, segundo

    for segundo in range(largura * altura):
        if segundo % largura == tempo_x and segundo % altura == tempo_y:
            imprimir(benders, altura, largura, segundo)
            return segundo

    return None


def part_1(benders: list[list[int]], segundos: int, largura: int, altura: int) -> int:
    metade_x, metade_y = largura // 2, altura // 2
    sup_esq = sup_dir = inf_esq = inf_dir = 0

    for bender in benders:
        x = (bender[0] + bender[2] * segundos) % largura
        y = (bender[1] + bender[3] * segundos) % altura

        if x == metade_x and y == metade_y:
            continue

        if x < metade_x and y < metade_y:
            sup_esq += 1
        elif x > metade_x and y < metade_y:
            sup_dir += 1
        elif x < metade_x and y > metade_y:
            inf_esq += 1
        elif x > metade_x and y > metade_y:
            inf_dir += 1

    return sup_esq * sup_dir * inf_esq * inf_dir


def main():
    with open('input.txt', 'r', encoding='utf-8') as f:
        dados = f.read().strip().split('\n')

    benders = [list(map(int, re.findall(r'-?\d+', linha))) for linha in dados]
    largura, altura = 101, 103
    segundos_part_1 = 100

    print(f'Total part 2: {part_2(benders, altura, largura)}')
    print(f'Total part 1: {part_1(benders, segundos_part_1, largura, altura)}')


if __name__ == '__main__':
    main()
