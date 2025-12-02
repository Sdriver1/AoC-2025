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

            if len(s) % 2 == 0:
                half = len(s) // 2
                if s[:half] == s[half:]:
                    total += n

    return total

if __name__ == "__main__":
    print(invalidIds("d2.txt"))
