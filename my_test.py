from my_code import pay_calculator


def test_pay_calculator():
    assert 660 == pay_calculator(40)
    assert 907.50 == pay_calculator(50)
    assert 330 == pay_calculator(20)
