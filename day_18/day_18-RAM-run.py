import sys, collections, time, functools
from rich.console import Console
from rich.live import Live

console = Console()

def tempo_execucao(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        inicio = time.perf_counter()
        resultado = func(*args, **kwargs)
        fim = time.perf_counter()

        duracao = fim - inicio
        print(f"[{func.__name__}] tempo de execução: {duracao:.6f}s")

        return resultado
    return wrapper

def valida(grade: list[list[str]], visitados: set[tuple[int, int]], i: int, j: int) -> bool:
    if not (0 <= i < len(grade) and 0 <= j < len(grade[0])): return False
    if grade[i][j] == '#' or (i, j) in visitados: return False
    return True


def gera_frame(grade: list[list[str]], mapping: dict[str, str]) -> str:
    linhas_formatadas = []
    for linha in grade:
        linhas_formatadas.append("".join(mapping.get(c, c) for c in linha))
    return "\n".join(linhas_formatadas)


def imprime_grade(grade: list[list[str]], prev_S: dict[tuple[int, int], int], \
                    prev_T: dict[tuple[int, int], int], colisao: tuple[int, int], \
                    inicio: tuple[int, int], fim: tuple[int, int]) -> None:
    caminho_S = []
    curr = colisao
    while curr != inicio:
        caminho_S.append(curr)
        curr = prev_S[curr]
    caminho_S.append(inicio)
    caminho_S.reverse()

    caminho_T = []
    curr = colisao
    while curr != fim:
        caminho_T.append(curr)
        curr = prev_T[curr]
    caminho_T.append(fim)
    caminho_T.reverse()

    mapping = {
        '.': "[blue].[/blue]",
        '0': "[bold red]0[/bold red]",
        '#': "[green]#[/green]"
    }

    with Live(gera_frame(grade, mapping), refresh_per_second=10) as live:
        max_passos = max(len(caminho_S), len(caminho_T))
        
        for i in range(max_passos):
            if i < len(caminho_S):
                y, x = caminho_S[i]
                grade[y][x] = '0'
            
            if i < len(caminho_T):
                y, x = caminho_T[i]
                grade[y][x] = '0'

            live.update(gera_frame(grade, mapping))
            time.sleep(0.01)


def resolver_2(grade: list[list[str]], inicio: tuple[int, int], fim: tuple[int, int], parte: bool = False) -> int | bool:

    queues = {'S': collections.deque([inicio]), 'T': collections.deque([fim])}
    distancia = {'S': {inicio: 0}, 'T': {fim: 0}}
    previos = {'S': {}, 'T': {}}
    visitados = {'S': {inicio}, 'T': {fim}}

    while queues['S'] and queues['T']:
        lado = 'S' if len(queues['S']) <= len(queues['T']) else 'T'
        outro_lado = 'T' if lado == 'S' else 'S'

        for _ in range(len(queues[lado])):
            curr_i, curr_j = queues[lado].popleft()

            for ni, nj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                pi, pj = ni + curr_i, nj + curr_j
                pos = (pi, pj)

                if valida(grade, visitados[lado], pi, pj):
                    previos[lado][pos] = (curr_i, curr_j)
                    visitados[lado].add(pos)
                    distancia[lado][pos] = distancia[lado][(curr_i, curr_j)] + 1
                    queues[lado].append(pos)

                    if pos in visitados[outro_lado]:
                        if parte:
                            imprime_grade(grade, previos['S'], previos['T'], pos, inicio, fim)
                            return distancia['S'][pos] + distancia['T'][pos]
                        return True

    return False


def resolver(grade: list[list[str]], inicio: tuple[int, int], fim: tuple[int, int], parte: bool = False) -> int | bool:
    
    queue_inicio_S = collections.deque([inicio])
    queue_fim_T = collections.deque([fim])
    visitados_S, visitados_T = {inicio}, {fim}
    prev_S, prev_T = {}, {}
    dist_S, dist_T = {inicio: 0}, {fim: 0}
    colisao = None

    while queue_inicio_S and queue_fim_T:
        iS, jS = queue_inicio_S.popleft()
        iT, jT = queue_fim_T.popleft()

        for ni, nj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            piS, pjS = ni + iS, nj + jS
            piT, pjT = ni + iT, nj + jT

            if valida(grade, visitados_S, piS, pjS):
                queue_inicio_S.append((piS, pjS))
                prev_S[(piS, pjS)] = (iS, jS)
                visitados_S.add((piS, pjS))
                dist_S[(piS, pjS)] = dist_S[(iS, jS)] + 1

                if (piS, pjS) in visitados_T:
                    colisao = (piS, pjS)
                    queue_inicio_S.clear()

            if valida(grade, visitados_T, piT, pjT):
                queue_fim_T.append((piT, pjT))
                prev_T[(piT, pjT)] = (iT, jT)
                visitados_T.add((piT, pjT))
                dist_T[(piT, pjT)] = dist_T[(iT, jT)] + 1

                if (piT, pjT) in visitados_S:
                    colisao = (piT, pjT)
                    queue_fim_T.clear()

    if colisao and parte:
        imprime_grade(grade, prev_S, prev_T, colisao, inicio, fim)
        return dist_S[colisao] + dist_T[colisao]
    
    if colisao: 
        return True

    return False


def cria_grade(bytess: list[tuple[int, int]], altura: int, largura: int) -> list[str]:
    set_bytes = set(bytess)
    return [["." if (i, j) not in set_bytes else "#" for i in range(largura)] for j in range(altura)]

@tempo_execucao
def main(prompt: str):

    try:
        altura, largura, total_bytes, parte = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    except IndexError:
        print(prompt)
        sys.exit(0)

    with open("input.txt", "r", encoding="utf-8") as f:
        bytess = [tuple(map(int, linha.split(","))) for linha in f.read().strip().splitlines()]

    if parte == '1':
        print(resolver_2(cria_grade(bytess[:total_bytes], altura + 1, largura + 1), (0, 0), (altura, largura), True))
    elif parte == '2':
        low, high = 0, len(bytess) - 1
        candidato = None

        while low <= high:
            mid = (low + high) // 2
            grade = cria_grade(bytess[:mid + 1], altura + 1, largura + 1)

            if not resolver_2(grade, (0, 0), (altura, largura)):
                candidato = bytess[mid] 
                high = mid - 1
            else:
                low = mid + 1

        print(candidato)
    else:
        print(prompt)


if __name__ == "__main__":
    prompt = "Error: falta de parametros\nTry: python day_18-RAM-run.py N M bytes n\nN = altura\nM = largura\nbytes = quantidade de bytes\nn = 1 ou 2"
    main(prompt)
