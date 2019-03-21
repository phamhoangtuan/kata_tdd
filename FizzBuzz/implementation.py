def _is_divisible(number, dividen):
    return number % dividen == 0


def get_fizz_buzz(number):
    result = str(number)
    if _is_divisible(number, 3) or '3' in str(number):
        result = 'Fizz'
    if _is_divisible(number, 5) or '5' in str(number):
        result = 'Buzz'
    if _is_divisible(number, 3) and _is_divisible(number, 5):
        result = 'FizzBuzz'
    return result


if __name__ == '__main__':
    for num in range(1, 101):
        print(get_fizz_buzz(num))
