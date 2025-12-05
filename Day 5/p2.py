def rangeSearchID(path: str) -> int:
    with open(path, "r") as f:
        lines = [line.strip() for line in f]
    blank_index = lines.index("")

    ranges = []
    for r in lines[:blank_index]:
        start_str, end_str = r.split("-")
        ranges.append((int(start_str), int(end_str)))
    ranges.sort()

    merged = []
    cur_start, cur_end = ranges[0]
    for start, end in ranges[1:]:
        if start <= cur_end + 1:
            cur_end = max(cur_end, end)
        else:
            merged.append((cur_start, cur_end))
            cur_start, cur_end = start, end
    merged.append((cur_start, cur_end))

    total = 0
    for start, end in merged:
        total += (end - start + 1)

    return total


if __name__ == "__main__":
    print(rangeSearchID("d5.txt"))  # My answer was 353716783056994
