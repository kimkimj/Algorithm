n = int(input())
count = 0
num = 666
#for i in range(666, 10001):
while True:
    #if str(i).find('666') != -1:
    if "666" in str(num):
        count += 1
        if count == n:
            print(num)
            break
    num += 1
# for i in range(666, 10001):
# for loop 으로 10000을 limit으로 설정해 놓으니 20번째 666부터는 아무것도 출력이 되지 않았다
# 20번째 666은 10666 으로 10000을 넘는다
# 문제에서는 10000 안의 666을 구하라는 것이 아니라 n이 10000 보다 작을 것이라고 명시한다
# 따라서 for loop 대신 infinite while loop을 사용해야한다