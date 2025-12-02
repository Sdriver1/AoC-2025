def rotations(path: str) -> int:
    with open(path, "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    dial = 50
    zero_count = 0
    for rot in lines:
        direction = rot[0]
        distance = int(rot[1:])
        if direction == "L":
            dial = (dial - distance) % 100
        else:
            dial = (dial + distance) % 100

        if dial == 0:
            zero_count += 1

    return zero_count


if __name__ == "__main__":
    answer = rotations("data/d1p1.txt")
    print(f"{answer}") # My puzzle answer was 1078
