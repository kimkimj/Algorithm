def solution(s):
    arr = s.split(' ')
    for i in range(len(arr)):
        if arr[i] != '':
            upperCase = arr[i][0].upper()
            arr[i] = upperCase + arr[i][1:].lower()
    return ' '.join(arr)

print(solution("a  aa"))

# space가 여러 개 consecutive 하게 있을 때 문제가 났다
# s.split을 하게되면 ''로 저장되기 때문에 이 string을 처리하려 하면 index out of range가 나는 것