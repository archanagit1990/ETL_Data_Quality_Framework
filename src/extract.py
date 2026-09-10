import pandas as pd

def extract_data(file_path):
    print("Extracting data from file:", file_path)
    print("Starting data extraction")

    data = pd.read_csv(file_path)
    print("Data extraction completed successfully.")
    print("Number of records extracted: ",len(data))
    return data

if __name__ == "__main__":
    data = extract_data("data/raw/sales_data.csv")
    print(data)