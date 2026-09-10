import pytest


@pytest.mark.smoke
def test_source_not_empty(source_data):

    assert len(source_data) > 0


@pytest.mark.dq
def test_source_columns(source_data):

    expected_columns = {
        "order_id",
        "customer_id",
        "customer_name",
        "product",
        "quantity",
        "unit_price",
        "order_date",
        "status"
    }

    assert expected_columns.issubset(
        source_data.columns
    )