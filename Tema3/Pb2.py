def chr_count(s):
    ct_dist = {}

    for i in s:
        if(i in ct_dist):
            ct_dist[i] += 1
        else:
            ct_dist[i] = 1
    return ct_dist

s = "Ana has apples."
print(chr_count(s))