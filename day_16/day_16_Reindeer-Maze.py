from typing import List, Set, Tuple
from queue import PriorityQueue


def part_1(grade: List[List[str]], d_ini: str, start: Tuple[int, int]) -> int | None:
    dirs_dict = {'L': (0, 1), 'S': (1, 0), 'O': (0, -1), 'N': (-1, 0)}
    dirs_keys = list(dirs_dict.keys())
    visitados: Set[tuple[int, int, str]] = set()

    pq = PriorityQueue()
    pq.put((0, start[0], start[1], d_ini))

    while pq:
        cost, r, c, d = pq.get()

        if (r, c, d) in visitados: continue
        visitados.add((r, c, d))

        if grade[r][c] == 'E': return cost

        dr, dc = dirs_dict[d]
        nr, nc = dr + r, dc + c
        if grade[nr][nc] != '#':
            pq.put((cost + 1, nr, nc, d))

        idx = dirs_keys.index(d)

        gir_dir = dirs_keys[(idx + 1) % 4]
        pq.put((cost + 1000, r, c, gir_dir))

        gir_dir = dirs_keys[(idx - 1) % 4]
        pq.put((cost + 1000, r, c, gir_dir))

    return None


def main():
    with open('input.txt', 'r', encoding='utf-8') as f:
        grade = [list(linha) for linha in f.read().strip().split()]

    start = Tuple[int, int]
    for r in range(len(grade)):
        if 'S' in grade[r]:
            start = (r, grade[r].index('S'))

    print(part_1(grade, 'L', start))


if __name__ == '__main__':
    main()
