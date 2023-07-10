def solution(number, k):
    answer = []
    for num in number:
        while k > 0 and answer and answer[-1] < num:
            answer.pop()
            k -= 1
        answer.append(num)
    return ''.join(answer)[:len(answer) - k]

#9999, 1을 넣으면 9999가 나온다
number = "9999"
k = 1
print(solution(number, k))




            
            
        


