def _is_divisible(number, divided):
    if number % divided == 0:
        return True
    return False


def is_leap_year(year_number):
    if _is_divisible(year_number, 4):
        if _is_divisible(year_number, 100):
            if _is_divisible(year_number, 400):
                return True
            else:
                return False
        else:
            return True
    return False
