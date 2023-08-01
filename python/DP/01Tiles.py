# https://sungmin-joo.tistory.com/21
# fibonacci sequence

n = int(input())
# dp = [0] * (n + 1) 이렇게 하면 n = 1일때 Index Out of Bounds exception @dp[2] =2
dp = [0] * 1000001
dp[1] = 1
dp[2] = 2

for i in range(3, n + 1):
    # 반복문 안에서도 수시로 나머지 연산을 해 주어야 메모리 초과가 발생하지 않는다.
    # (값이 int값을 초과하기 때문에 n = 1000000 일 경우 엄청나게 많은 메모리를 차지하게 된다.)
    dp[i] = (dp[i - 2] + dp[i - 1]) % 15746
print(dp[n])





