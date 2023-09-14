from collections import defaultdict
import re
def solution(files):
    dict = {}

    for i in range(len(files)):
        f = files[i]
        parts = re.split("(\d+)", f)
        head = parts[0]
        num = int(parts[1])
        tail = ""
        for k in range(2, len(parts)):
            tail += parts[k]

        dict[f] = [head, num, tail, i]

    files.sort()
    for i in range(1, len(files)):
        current = files[i]
        head = dict[current][0]
        for j in range(1, i):
            prev = files[i - j]
            prev_head = dict[prev][0]
            if prev_head != head:
                break

            num = dict[current][1]
            prev_num = dict[prev][1]
            if num > prev_num:
                break

            tail = dict[current][2]
            prev_tail = dict[prev][2]
            if num < prev_num or (num == prev_num and tail < prev_tail):
                files[i - 1] = f
                files[i] = prev

            elif num == prev_num and tail == prev_tail:
                current_org_index = dict[current][3]
                prev_org_index = dict[prev][3]
                if current_org_index < prev_org_index:
                    files[i - 1] = f
                    files[i] = prev
    return files

files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
print(solution(files))






