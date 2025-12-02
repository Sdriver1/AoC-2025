def invalidIds(path: str) -> int:
    with open(path, "r") as f:
        line = f.read().strip()

    parts = line.split(",")
    total = 0

    for r in parts:
        start_str, end_str = r.split("-")
        start, end = int(start_str), int(end_str)

        for n in range(start, end + 1):
            s = str(n)

            if is_invalid(s):
                total += n

    return total


def is_invalid(s: str) -> bool:
    length = len(s)

    for size in range(1, length // 2 + 1):
        if length % size == 0:
            block = s[:size]
            repeats = length // size
            if repeats >= 2 and block * repeats == s:
                return True
    return False


if __name__ == "__main__":
    print(invalidIds("d2.txt"))
