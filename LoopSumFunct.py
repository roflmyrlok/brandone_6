def numbers_sum(*numbers):
    result = 0

    for number in numbers:
        result += int(number)
    return result
answer = numbers_sum( 32, 123, 1234, 632)
print(answer)
