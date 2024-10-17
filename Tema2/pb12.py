def rhyme(words):
    ret_list = []
    used_words = set()
    
    for i, word in enumerate(words):
        if word in used_words:
            continue
        current_group = [word]
        used_words.add(word)
        for j in range(i + 1, len(words)):
            if words[j] not in used_words and word[-2:] == words[j][-2:]:
                current_group.append(words[j])
                used_words.add(words[j])
        ret_list.append(current_group)
    
    return ret_list

print(rhyme(['ana', 'banana', 'carte', 'arme', 'parte']))
            