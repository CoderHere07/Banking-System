import pytest
from bank_app import deposit, withdraw, transfer, calculate_interest, check_loan_eligibility

def test_deposit_error_branch():
    with pytest.raises(ValueError):
        deposit(1000, -50)

def test_withdraw_negative_amount():
    with pytest.raises(ValueError):
        withdraw(1000, -100)


def test_withdraw_insufficient_balance():
    with pytest.raises(ValueError):
        withdraw(300, 500)

def test_transfer_negative_amount():
    with pytest.raises(ValueError):
        transfer(1000, 500, -100)


def test_transfer_insufficient_balance():
    with pytest.raises(ValueError):
        transfer(200, 500, 300)


def test_transfer_success_path():
    result = transfer(1000, 200, 400)
    assert result == (600, 600)

def test_interest_negative_balance():
    with pytest.raises(ValueError):
        calculate_interest(-100, 5, 2)


def test_interest_negative_rate():
    with pytest.raises(ValueError):
        calculate_interest(1000, -5, 2)


def test_interest_success():
    assert calculate_interest(1000, 10, 1) == 1100.0

def test_loan_eligible():
    assert check_loan_eligibility(6000, 750) is True


def test_loan_not_eligible_low_balance():
    assert check_loan_eligibility(3000, 750) is False


def test_loan_not_eligible_low_credit():
    assert check_loan_eligibility(6000, 650) is False
