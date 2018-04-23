def isPrime(n):
    if n < 2: return False
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

count, result, list = 0, 1, []
while count < 10001:
    result += 1
    if isPrime(result):
        list.append(result)
        count += 1
print(list)
print('The 10 001st prime number is:', result)