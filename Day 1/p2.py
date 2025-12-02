def clicks0(path: str) -> int:
    with open(path, "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    dial = 50
    zero_count = 0
    for rot in lines:
        direction = rot[0]
        distance = int(rot[1:])
        step = 1 if direction == "R" else -1

        for _ in range(distance):
            dial = (dial + step) % 100
            if dial == 0:
                zero_count += 1

    return zero_count


if __name__ == "__main__":
    answer = clicks0("d1.txt")
    print(f"{answer}") # My puzzle answer was 6412
