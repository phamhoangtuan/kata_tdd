from LeapYears.solution import is_leap_year


def test_leap_year_divisible_by_4():
    assert not is_leap_year(1990)
    assert is_leap_year(1992)


def test_leap_year_divisible_by_4_but_not_100():
    assert not is_leap_year(2100)
    assert is_leap_year(2008)


def test_not_leap_year_divisible_by_100_but_not_400():
    assert not is_leap_year(1700)
    assert is_leap_year(1600)


def test_leap_year_divisible_by_400():
    assert not is_leap_year(1700)
    assert is_leap_year(2000)
