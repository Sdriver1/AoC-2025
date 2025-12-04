def forkliftAccess(path):
    with open(path, "r") as f:
        grid = [list(line.rstrip("\n")) for line in f]

    rows = len(grid)
    cols = len(grid[0])

    def neighbors(r, c):
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    yield nr, nc

    total_accessible = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "@":
                continue
            adj = sum(1 for nr, nc in neighbors(r, c) if grid[nr][nc] == "@")
            if adj < 4:
                total_accessible += 1
    return total_accessible


if __name__ == "__main__":
    print(forkliftAccess("d4.txt"))  # My answer was 1349
