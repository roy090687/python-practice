def solution(number):
    result = []
    place = 1
    while number > 0:
        digit = number % 10
        result.insert(0, digit * place)
        number //= 10
        place *= 10

    return result

number = 58697
print(solution(number))

