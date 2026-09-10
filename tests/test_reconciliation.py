import pytest


@pytest.mark.reconciliation
def test_source_target_reconciliation(
    source_data,
    target_data,
    rejected_target_data
):

    source_count = len(source_data)
    target_count = len(target_data)
    rejected_count = len(rejected_target_data)

    assert source_count == (
        target_count + rejected_count
    )


@pytest.mark.reconciliation
def test_valid_target_count(
    valid_data,
    target_data
):

    assert len(valid_data) == len(target_data)