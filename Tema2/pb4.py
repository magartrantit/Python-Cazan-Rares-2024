def compose(notes, moves, start):
    song = [notes[start]]
    cur = start
    for i in moves:
        cur = (cur + i) % len(notes)
        song.append(notes[cur])
    return song


notes = ["do", "re", "mi", "fa", "sol"]
moves = [1, -3, 4, 2]
start = 2
print(compose(notes, moves, start))