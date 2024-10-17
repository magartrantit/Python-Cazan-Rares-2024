def char_freq(r_file,w_file):
    with open(r_file, 'r') as f:
        content = f.read()
    paragraphs = content.split()
    char_freq = dict()
    for par in paragraphs:
        for char in par:
            if char.lower() not in char_freq:
                char_freq[char.lower()] = 0
            char_freq[char.lower()] += 1
    print(char_freq)
    write_file = open(w_file,'w')
    histogram = []
    height_of_hist = max(char_freq.values())
    for i in range(height_of_hist):
        line = []
        for value in char_freq.values():
            if value <= i:
                line.append('o')
            else:
                line.append(' ')
        histogram.append(line)
    histogram.append(char_freq.keys())
    open(w_file,'w').write('\n'.join(''.join(line) for line in histogram))

char_freq('input.txt','output.txt')