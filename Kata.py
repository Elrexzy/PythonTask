def isEven(number):
    if number % 2 == 0:
        return True
    else:
        return False


def isPrimeNumber(number):
    isPrime = True

    for index in range(2, number):
        if number % index == 0:
            isPrime = False
            break

    if isPrime:
        return True
    else:
        return False


def subtract(number, numberOne):
    if number > numberOne:
        return number - numberOne
    else:
        return numberOne - number


def divide(number, numberOne):
    if numberOne == 0:
        return 0
    else:
        return number / numberOne


def factorOf(number):
    counter = 0

    for index in range(1, number + 1):
        if number % index == 0:
            counter += 1

    return counter


def isSquare(number):
    if math.sqrt(number) % 1 == 0:
        return True
    else:
        return False


def isPalindrome(number):
    original = number
    reverse = 0

    while number != 0:
        digit = number % 10
        reverse = reverse * 10 + digit
        number = number // 10

    if original == reverse:
        return True
    else:
        return False


def factorialOf(number):
    factorial = 1

    for index in range(1, number + 1):
        factorial = factorial * index

    return factorial


def squareOf(number):
    result = number * number
    return result


print("Enter a number:", end= ' ')
number = int(input())

print(squareOf(number))
