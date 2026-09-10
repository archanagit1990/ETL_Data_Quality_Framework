from extract import extract_data
from transform import transform_data
from load import create_tables, load_data


def run_pipeline():

    print("\nStarting ETL Pipeline")

    source_df = extract_data(
        "data/raw/sales_data.csv"
    )

    valid_records, rejected_records = transform_data(source_df)

    create_tables()

    load_data(valid_records, rejected_records)

    print("\nETL Pipeline completed successfully")


if __name__ == "__main__":
    run_pipeline()