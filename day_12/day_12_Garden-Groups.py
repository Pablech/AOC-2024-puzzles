def main():
    with open('input.txt', 'r', encoding='utf-8') as f:
        mapa = [list(linha) for linha in f.read().splitlines()]


if __name__ == '__main__':
    main()
