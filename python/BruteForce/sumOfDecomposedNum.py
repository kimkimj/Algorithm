#n = 216
n = int(input())

# n + 1을 해야 for loop에 n이 포함이 된다
for i in range(n + 1):
    #get every digit
    sum = i
    for digit in str(i):
        sum += int(digit)
    if sum == n:
        print(i)
        break

    #생성자가 없는 경우도 생각해야 한다
    # i와 입력값이 같으면 생성자가 없다는 뜻
    if i == n:
        print(0)
