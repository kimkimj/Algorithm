from collections import defaultdict
import re
def solution(files):
    dict = {}

    for i in range(len(files)):
        f = files[i]
        parts = re.split("(\d+)", f)
        head = parts[0].lower()
        num = int(parts[1])

        dict[f] = [head, num, i]

    files.sort()
    for i in range(1, len(files)):
        current = files[i]
        head = dict[current][0]

        current_index = i
        for j in range(1, i + 1):
            prev = files[i - j]
            prev_head = dict[prev][0]
            if prev_head != head:
                break

            num = dict[current][1]
            prev_num = dict[prev][1]
            if num > prev_num:
                break

           ## source of error. how to switch the two
            if num < prev_num:
                files[i - j] = current
                files[current_index] = prev

            elif num == prev_num:
                current_org_index = dict[current][2]
                prev_org_index = dict[prev][2]
                if current_org_index < prev_org_index:
                    files[i - j] = current
                    files[current_index] = prev
            current_index -= 1
    return files

files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
print(solution(files))




