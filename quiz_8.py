import random
def random_number():
    result = []
    while len(result) < 6:
        number = random.randint(1, 45)
        if number not in result:
            result.append(number)
    result.sort()
    return result
x=random_number()
print('생성된 숫자는 ' + str(x) + '입니다.')
