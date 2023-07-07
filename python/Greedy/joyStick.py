def solution(name):
    count = 0

    # 좌에서 우로 이동
    cursor = len(name) - 1

    for i, char in enumerate(name):
        # 해당 알파벳 최소값
        count += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

        # 해당 알파벳 다음부터 연속된 A 문자열 찾기
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1

        # '왼쪽에서 오른쪽으로 이동', '연속된 A의 왼쪽 시작', '연속된 A의 오른쪽 시작'
        # 중에서 최솟값이 가장 효율적인 이동 횟수
        cursor = min([cursor, i * 2 + (len(name) - next), i + 2 * (len(name) - next)])

    return count + cursor

str = 'JAN'
print(solution(str))

# https://aiday.tistory.com/120#%ED%95%B4%EA%B2%B0%20%EA%B3%BC%EC%A0%95-1