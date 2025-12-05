raw_ranges = []
raw_ids = []


with open("day5/day5.txt") as f:
    raw_ranges, raw_ids = f.read().strip().split("\n\n")

ranges = sorted(tuple(map(int, r.split("-"))) for r in raw_ranges.splitlines())
ids = list(map(int, raw_ids.splitlines()))

merged = []
for s, e in ranges:
    if not merged or s > merged[-1][1] + 1:
        merged.append([s, e])
    else:
        merged[-1][1] = max(merged[-1][1], e)

fresh = 0
for x in ids:
    lo, hi, ans = 0, len(merged) - 1, -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if merged[mid][0] <= x:
            ans = mid
            lo = mid + 1
        else:
            hi = mid - 1
        if ans != -1:
            s, e = merged[ans]
            if s <= x <= e:
                fresh += 1

total = sum(e - s + 1 for s, e in merged)
print(f"Part 1: {fresh}, Part 2: {total}")

# spoiled = 0
# fresh = 0
# for id in ids:
#     lo = 0
#     hi = len(merged) - 1
#     ans = -1

#     while lo <= hi:
#         mid = (hi + lo) // 2
#         if merged[mid][0] <= id:
#             lo = mid + 1
#             ans = mid
#         else:
#             hi = mid - 1

#     if ans == -1:
#         # print(f"{id} is spoiled")
#         spoiled +=1
#     else:
#         s, e = merged[ans]
#         if s <= id <= e:
#             # print(f"{id} is fresh")
#             fresh += 1
#         else:
#             # print(f"{id} is spoiled")
#             spoiled += 1
# print(fresh)

# total = 0
# for s, e in merged:
#     total += (e - s) + 1

# print(total)
