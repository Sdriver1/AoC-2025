def highestJoltage(path: str) -> int:
    total = 0

    with open(path, "r") as f:
        for line in f:
            nums = [int(c) for c in line.strip()]
            best = 0
            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    val = nums[i] * 10 + nums[j]
                    if val > best:
                        best = val
            total += best
    return total


if __name__ == "__main__":
    print(highestJoltage("d3.txt"))  # My answer was 17,443
