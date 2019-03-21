from FizzBuzz.implementation import get_fizz_buzz


def _check_fizz_buzz_value(input, expected_output):
    output = get_fizz_buzz(input)
    assert output == expected_output


def test_return_one_when_call_fizz_buzz_one():
    _check_fizz_buzz_value(1, '1')


def test_return_two_when_call_fizz_buzz_two():
    _check_fizz_buzz_value(2, '2')


def test_return_fizz_when_call_fizz_buzz_three():
    _check_fizz_buzz_value(3, 'Fizz')


def test_return_buzz_when_call_fizz_buzz_five():
    _check_fizz_buzz_value(5, 'Buzz')


def test_return_fizz_when_call_fizz_buzz_six():
    _check_fizz_buzz_value(6, 'Fizz')


def test_return_buzz_when_call_fizz_buzz_ten():
    _check_fizz_buzz_value(10, 'Buzz')


def test_return_fizzbuzz_when_call_fizz_buzz_fifteen():
    _check_fizz_buzz_value(15, 'FizzBuzz')


def test_return_fizz_when_call_fizz_buzz_twenty_three():
    _check_fizz_buzz_value(23, 'Fizz')


def test_return_buzz_when_call_fizz_buzz_fifty_one():
    _check_fizz_buzz_value(51, 'Buzz')
