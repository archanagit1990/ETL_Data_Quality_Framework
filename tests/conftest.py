import sys
import os
import pytest
import pandas as pd

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            "src"
        )
    )
)

from extract import extract_data
from transform import transform_data
from database import get_connection


@pytest.fixture(scope="session")
def source_data():

    return extract_data(
        "data/raw/sales_data.csv"
    )


@pytest.fixture(scope="session")
def transformed_data(source_data):

    valid_records, rejected_records = transform_data(source_data)

    return valid_records, rejected_records


@pytest.fixture
def valid_data(transformed_data):

    return transformed_data[0]


@pytest.fixture
def rejected_data(transformed_data):

    return transformed_data[1]


@pytest.fixture
def target_data():

    conn = get_connection()

    df = pd.read_sql(
        "SELECT * FROM fact_sales ORDER BY order_id",
        conn
    )

    conn.close()

    return df


@pytest.fixture
def rejected_target_data():

    conn = get_connection()

    df = pd.read_sql(
        "SELECT * FROM rejected_sales",
        conn
    )

    conn.close()

    return df