def get_duration(start, end):
    start_hour, start_min = map(int, start.split(":"))
    end_hour, end_min = map(int, end.split(":"))
    if start_hour == end_hour:
        return end_min - start_min
    else:
        return (60 - start_min) + (end_hour - start_hour) * 60 + end_min

def get_music_by_duration(min_played, music):
    length = len(music)
    if length < min_played: # if the music is shorter than the min played
        whole = ((min_played - length) // length) + 1
        part = (min_played - length) % length

        return music * whole + music[:part]

    # if the music is longer than the min played on radio
    return music[:min_played]

def detect_sharp(notes):
    notes = list(notes)
    dict = {'C':'0', 'D':'1', 'F':'2', 'G':'3', 'A':'4'}
    for i in range(len(notes) - 1):
        a = notes[i + 1]
        if notes[i + 1] == '#':
            notes[i] = dict[notes[i]]
    notes = ''.join(notes)
    return notes.replace('#', '')

def solution(m, musicinfos):
    tune = detect_sharp(m)
    longest_min_played = 0
    longest = []

    for i in range(len(musicinfos)):
        song = musicinfos[i]
        start, end, name, music = song.split(",")
        min_played = get_duration(start, end)
        notes_played = get_music_by_duration(min_played, music)
        notes_played = detect_sharp(notes_played)

        if tune in notes_played:
            if min_played > longest_min_played:
                longest = [name]
            elif min_played == longest_min_played:
                longest.append(name)
    if len(longest) > 0:
        return longest[0]
    return "(None)"

musicinfo = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]
m = "ABC"
print(solution(m, musicinfo))