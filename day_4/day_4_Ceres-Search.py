def part_1(arquivo: list[str]) -> int:
    cont = 0
    linhas = len(arquivo)
    colunas = len(arquivo[0])
    palavras = ['XMAS', 'SAMX']

    for i in range(linhas):
        for j in range(colunas):

            if j < colunas - 3:
                teste = arquivo[i][j] + arquivo[i][j+1] + arquivo[i][j+2] + arquivo[i][j+3]
                cont += 1 if teste in palavras else 0

            if i < linhas - 3:
                teste = arquivo[i][j] + arquivo[i+1][j] + arquivo[i+2][j] + arquivo[i+3][j]
                cont += 1 if teste in palavras else 0

            if i < linhas - 3 and j < colunas - 3:
                teste =  arquivo[i][j] + arquivo[i+1][j+1] + arquivo[i+2][j+2] + arquivo[i+3][j+3]
                cont += 1 if teste in palavras else 0

            if i < linhas - 3 and j > 2:
                teste =  arquivo[i][j] + arquivo[i+1][j-1] + arquivo[i+2][j-2] + arquivo[i+3][j-3]
                cont += 1 if teste in palavras else 0

    return cont


def part_2(arquivo: list[str]) -> int:
    cont_x_mas = 0
    palavras = ['MAS', 'SAM']

    for i in range(1, len(arquivo) - 1):
        for j in range(1, len(arquivo[i]) - 1):
            if arquivo[i][j] == 'A':
                diagonal_direita = arquivo[i - 1][j - 1] + arquivo[i][j] + arquivo[i + 1][j + 1]
                diagonal_esquerda = arquivo[i + 1][j - 1] + arquivo[i][j] + arquivo[i - 1][j + 1]
                if diagonal_direita in palavras and diagonal_esquerda in palavras:
                    cont_x_mas += 1

    return cont_x_mas


def main():
    with open('input.txt', 'r', encoding='utf-8') as arquivo:
        arquivo = arquivo.read()

    arquivo = arquivo.split()

    print(part_1(arquivo))
    print(part_2(arquivo))


if __name__ == '__main__':
    main()
