import pytest


@pytest.mark.dq
def test_valid_quantity(valid_data):

    assert (
        valid_data["quantity"] > 0
    ).all()


@pytest.mark.dq
def test_total_amount(valid_data):

    expected = (
        valid_data["quantity"]
        * valid_data["unit_price"]
    )

    assert (
        valid_data["total_amount"] == expected
    ).all()


@pytest.mark.dq
def test_valid_customer_id(valid_data):

    assert (
        valid_data["customer_id"]
        .isnull()
        .sum()
        == 0
    )


@pytest.mark.dq
def test_valid_customer_name(valid_data):

    assert (
        valid_data["customer_name"]
        .isnull()
        .sum()
        == 0
    )