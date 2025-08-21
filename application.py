def find_missing_ranges(frames: list[int]) -> dict:
    quicksort(frames)
    gaps = []
    longest_gap = None
    missing_count = max(frames) - len(frames)

    max_gap_size = 0

    for i in range(len(frames) - 1):
        a, b = frames[i], frames[i+1]
        if b > a + 1:
            gap = [a+1, b-1]
            gaps.append(gap)
            gap_size = b - a - 1
            if gap_size > max_gap_size:
                max_gap_size = gap_size
                longest_gap = gap

    return {
        "gaps": gaps,
        "longest_gap": longest_gap,
        "missing_count": missing_count
    }

# Example usage
frames = [1,2,3,5,6,10,11,16]
result = find_missing_ranges(frames)
print(result)
