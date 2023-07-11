def my_solution_wrong(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(reverse=True)

    answer = ''
    for n in numbers:
        answer += n

    return answer

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x : str(x) * 3, reverse = True)
    return str(int(''.join(numbers)))

numbers = [3, 30, 34, 5, 9]
print(solution(numbers))
