def sum(numbers):
    result = 0
    for i in range(len(numbers)):
        result += int(numbers[i])
    return result
numbers_to_use = [32,23,2]
answer = sum(numbers_to_use)
print(answer)
