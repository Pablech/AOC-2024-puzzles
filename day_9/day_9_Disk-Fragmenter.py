def descompacta_arquivo(arquivo: str) -> list[str]:
    blocos = [int(arquivo[i]) for i in range(len(arquivo)) if i % 2 == 0]
    espacos = [int(arquivo[i]) for i in range(len(arquivo)) if i % 2 == 1]
    arquivo_descompactado = ''

    for i in range(len(blocos)):
        try:
            arquivo_descompactado += (str(i) + ' ') * blocos[i] + '. ' * espacos[i]
        except IndexError:
            if len(blocos) >= len(espacos):
                arquivo_descompactado += (str(i) + ' ') * blocos[i]
            else:
                arquivo_descompactado += '. ' * espacos[i]
    return arquivo_descompactado.split()


def corrige_arquivo(arquivo_descompactado: list[str]) -> list[str]:
    tamanho_final = len(arquivo_descompactado) - arquivo_descompactado.count('.')
    j = len(arquivo_descompactado) - 1
    arquivo_corrigido = []

    for i in range(tamanho_final):
        if arquivo_descompactado[i] == '.':
            while True:
                if arquivo_descompactado[j] != '.':
                    arquivo_corrigido.append(arquivo_descompactado[j])
                    j -= 1
                    break
                else:
                    j -= 1
        else:
            arquivo_corrigido.append(arquivo_descompactado[i])

    return arquivo_corrigido


def part_1(arquivo_corrigido: list[str]) -> int:
    total = 0

    for i in range(len(arquivo_corrigido)):
        try:
            total += i * int(arquivo_corrigido[i])
        except ValueError:
            print(arquivo_corrigido[i], i)

    return total


def main():
    with open('input.txt', 'r', encoding='utf-8') as f:
        arquivo = f.read().replace('\n', '')

    print(part_1(corrige_arquivo(descompacta_arquivo(arquivo))))


if __name__ == '__main__':
    main()
