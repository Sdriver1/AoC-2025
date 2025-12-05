def rangeSearch(path: str) -> int:
    with open(path, "r") as f:
        lines = [line.strip() for line in f]
    blank_index = lines.index("")

    ranges = []
    for r in lines[:blank_index]:
        start_str, end_str = r.split("-")
        ranges.append((int(start_str), int(end_str)))

    fresh_count = 0
    for val in [int(x) for x in lines[blank_index + 1:]]:
        for start, end in ranges:
            if start <= val <= end:
                fresh_count += 1
                break

    return fresh_count


if __name__ == "__main__":
    print(rangeSearch("d5.txt"))  # My Answer was 615
