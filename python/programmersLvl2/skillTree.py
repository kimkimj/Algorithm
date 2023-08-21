from collections import deque
def solution(skill, skill_trees):
    skill = list(skill)
    count = 0
    for tree in skill_trees:
        req = deque(skill)
        for i in range(len(tree)):
            letter = tree[i]
            if letter in req:
                if req[0] == letter:
                    req.popleft()
                else:
                    break
            if i == len(tree) - 1:
                count += 1
    return count

skill = "CBD"
skill_tree = ["BACDE", "CBADF", "AECB", "BDA"]
solution(skill, skill_tree)
