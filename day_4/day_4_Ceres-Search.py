def part_1(arquivo: str) -> int:
    arquivo = arquivo.split()

    cont_horizontal = 0
    for i in range(len(arquivo)):
        for j in range(len(arquivo[i]) - 3):
            palavra = arquivo[i][j] + arquivo[i][j+1] + arquivo[i][j+2] + arquivo[i][j+3]
            if palavra == 'XMAS' or palavra == 'SAMX':
                cont_horizontal += 1

    cont_vertical = 0
    for i in range(len(arquivo) - 3):
        for j in range(len(arquivo[i])):
            palavra = arquivo[i][j] + arquivo[i+1][j] + arquivo[i+2][j] + arquivo[i+3][j]
            if palavra == 'XMAS' or palavra == 'SAMX':
                cont_vertical += 1

    cont_diagonal_direita = 0
    for i in range(len(arquivo) - 3):
        for j in range(len(arquivo[i]) - 3):
            palavra = arquivo[i][j] + arquivo[i+1][j+1] + arquivo[i+2][j+2] + arquivo[i+3][j+3]
            if palavra == 'XMAS' or palavra == 'SAMX':
                cont_diagonal_direita += 1

    cont_diagonal_esquerda = 0
    for i in range(len(arquivo) - 3):
        for j in range(3, len(arquivo[i])):
            palavra = arquivo[i][j] + arquivo[i+1][j-1] + arquivo[i+2][j-2] + arquivo[i+3][j-3]
            if palavra == 'XMAS' or palavra == 'SAMX':
                cont_diagonal_esquerda += 1

    return cont_horizontal + cont_vertical + cont_diagonal_direita + cont_diagonal_esquerda


def main():
    with open('Ceres.txt', 'r', encoding='utf-8') as arquivo:
        arquivo = arquivo.read()

    print(part_1(arquivo))


if __name__ == '__main__':
    main()
