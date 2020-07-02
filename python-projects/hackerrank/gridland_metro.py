from collections import defaultdict

def count_set_bits(bits):
    # brian kernighans algorithm
    count = 0
    while bits:
        bits &= (bits-1)
        count += 1
    return count

#print(count_set_bits(25))
#print(bin(25))

def gridlandMetro(n, m, k, tracks):
    #grid_map = [2**m-1 for _ in range(n)]
    partial_grid_map = defaultdict(lambda: 2**m-1)
    #print([bin(x) for x in grid_map])
    for track in tracks:
        map_index = track[0] - 1
        from_m = track[1]
        to_m = track[2]
        if from_m > to_m:
            from_m, to_m = to_m, from_m
        #print(map_index, from_m, to_m)
        covered_area = (2**(to_m-from_m+1)-1) << (m-to_m)
        #print(bin(covered_area))
        partial_grid_map[map_index] = partial_grid_map[map_index] & (~covered_area)
        #print([(x,bin(y)) for x, y in partial_grid_map.items()])
        #print("#"*2)
    count = 0
    for k, v in partial_grid_map.items():
        count += count_set_bits(v)
    #print(count)
    count = count + m*(n-len(partial_grid_map))
    return count

print(gridlandMetro(4, 4, 3, [[2, 2, 3], [3, 1, 4], [4, 4, 4]]))
