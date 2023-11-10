import random
result = []
while len(result) < 6:
    number = random.randint(1, 45)
    if number not in result:
        result.append(number)

result.sort()
print('생성된 숫자는 ' + str(result) + '입니다.')
