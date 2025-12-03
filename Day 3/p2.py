def best12_simple(line: str, k=12) -> int:
    digits = [int(c) for c in line.strip()]
    n = len(digits)
    answer = []

    start = 0
    for needed in range(k, 0, -1):
        end = n - needed
        best_digit = -1
        best_pos = start
        for i in range(start, end + 1):
            if digits[i] > best_digit:
                best_digit = digits[i]
                best_pos = i
        answer.append(best_digit)
        start = best_pos + 1
    return int("".join(str(d) for d in answer))


def total_joltage(path: str) -> int:
    total = 0
    with open(path) as f:
        for line in f:
            total += best12_simple(line)
    return total


if __name__ == "__main__":
    print(total_joltage("d3.txt"))  # My answer was 172167155440541
