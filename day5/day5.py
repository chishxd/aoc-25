ranges = []
ids = []


with open("day5/day5.txt") as f:
    parse_line = True
    for line in f:
        line = line.strip()
        if not line:
            parse_line = False
            continue

        if parse_line:
            a, b = map(int, line.split("-"))
            ranges.append((a, b))
        else:
            ids.append(int(line))


ranges.sort()
merged = []
for start, end in ranges:
    if not merged or start > merged[-1][1] + 1:
        merged.append([start, end])
    else:
        merged[-1][1] = max(merged[-1][1], end)

spoiled = 0
fresh = 0
for id in ids:
    lo = 0
    hi = len(merged) - 1
    ans = -1

    while lo <= hi:
        mid = (hi + lo) // 2
        if merged[mid][0] <= id:
            lo = mid + 1
            ans = mid
        else:
            hi = mid - 1
    
    if ans == -1:
        # print(f"{id} is spoiled")
        spoiled +=1
    else:
        s, e = merged[ans]
        if s <= id <= e:
            # print(f"{id} is fresh")
            fresh += 1
        else:
            # print(f"{id} is spoiled")
            spoiled += 1

print(fresh)

