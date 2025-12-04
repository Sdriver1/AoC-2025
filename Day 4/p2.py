def total_removed(path):
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

    total = 0
    while True:
        to_remove = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != "@":
                    continue

                adj = sum(1 for nr, nc in neighbors(r, c) if grid[nr][nc] == "@")
                if adj < 4:
                    to_remove.append((r, c))
        if not to_remove:
            break
        for r, c in to_remove:
            grid[r][c] = "."

        total += len(to_remove)

    return total


if __name__ == "__main__":
    print(total_removed("d4.txt"))  # My Answer was 8277
