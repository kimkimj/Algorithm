n = int(input())
arr = list(map(int, input().split()))

# list를 set으로 바꿔 중복을 제거한 후 sorted()를 이용해 정렬된 list로 바꾼다
sorted = sorted(set(arr))

# dictionary에 list의 원소와 그 인덱스 값을 저장한다
# 인덱스 값이 원소보다 작은 원소의 수이다
dict = {}
for i in range(len(sorted)):
    dict[sorted[i]] = i

# dictionary안에서 원소의 value를 찾는다
for i in range(n):
    print(dict[arr[i]])


