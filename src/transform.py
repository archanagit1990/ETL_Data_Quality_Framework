import pandas as pd

def transform_data(df):
    print("Starting data transformation")
    #work on copy of the data to avoid modifying the original DataFrame
    df = df.copy()
    #convert order_date to datetime format
    df["order_date"] = pd.to_datetime(df["order_date"], errors='coerce')

    #identify duplicates
    duplicate_mask = df.duplicated(subset=["order_id"],keep=False)

    #create a new column rejected reason based on certain conditions
    df["rejected_reason"] = ""
    df.loc[df["customer_id"].isna(),"rejected_reason"]+="Missing Customerid; "
    df.loc[df["customer_name"].isna(),"rejected_reason"]+="Missing Customername; "
    df.loc[df["unit_price"].isna(),"rejected_reason"] += "Missing unit_price; "
    df.loc[df["quantity"]<=0,"rejected_reason"]+="Invalid quantiy; "
    df.loc[df["order_date"].isna(),"rejected_reason"]+= "Invalid order_date; "
    df.loc[duplicate_mask,"rejected_reason"] += "Duplicate order_id; "

    #seperate rejected and valid records

    valid_records=df[df["rejected_reason"]==""].copy()
    rejected_records=df[df["rejected_reason"]!=""].copy()

    #calculate total price for valid records only
    valid_records["total_amount"]=(valid_records["unit_price"]*valid_records["quantity"])

    #drop rejected_reason column
    valid_records.drop(columns=["rejected_reason"],inplace=True)

    print("Transformation completed.")
    print("Valid records:", len(valid_records))
    print("Rejected records:", len(rejected_records))

    return valid_records, rejected_records

if __name__ == "__main__":

    from extract import extract_data
    source_df = extract_data(
        "data/raw/sales_data.csv"
    )

    valid_records, rejected_records = transform_data(source_df)

    print("\nVALID RECORDS")
    print(valid_records)

    print("\nREJECTED RECORDS")
    print(
        rejected_records[
            ["order_id", "rejected_reason"]
        ]
    )