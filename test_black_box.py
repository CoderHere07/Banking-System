import pytest
from bank_app import deposit, withdraw, transfer, calculate_interest

@pytest.mark.parametrize("balance, amount, expected", [
    (1000, 500, 1500),
    (0, 100, 100)
])
def test_deposit_positive_amount(balance, amount, expected):
    assert deposit(balance, amount) == expected


@pytest.mark.parametrize("balance, amount", [
    (1000, 0),
    (1000, -200)
])
def test_deposit_invalid_amount(balance, amount):
    with pytest.raises(ValueError):
        deposit(balance, amount)

def test_withdraw_more_than_balance():
    with pytest.raises(ValueError):
        withdraw(500, 600)

def test_transfer_success():
    from_balance, to_balance = transfer(1000, 500, 300)
    assert from_balance == 700
    assert to_balance == 800


def test_transfer_failure_insufficient_balance():
    with pytest.raises(ValueError):
        transfer(200, 500, 400)

@pytest.mark.parametrize("balance, rate, years, expected", [
    (1000, 10, 1, 1100.0),
    (2000, 5, 2, 2205.0)
])
def test_calculate_interest(balance, rate, years, expected):
    assert calculate_interest(balance, rate, years) == expected
