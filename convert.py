import pandas as pd
from pymongo import MongoClient
import argparse
from dotenv import load_dotenv
import os

load_dotenv()

def create_table(df, start_index, end_index):
    """
    create a dataframe for a table using the specified start and end indices
    
    Args:
    - df: dataframe containing the data
    - start_index: Starting index of the table
    - end_index: Ending index of the table
    
    Returns:
    - dataframe for the specified table
    """
    table = df.iloc[start_index:end_index]
    table.columns = [f"{col[1]}" for col in table.columns]
    return table

def extract_table_data(df, table_ranges):
    table_data = []
    for start, end in table_ranges:
        table_df = create_table(df, start, end)
        table_dict = table_df.to_dict(orient='records')
        table_data.append(table_dict)
    return table_data

def checkExistence_DB(DB_NAME, client):
    DBlist = client.list_database_names()
    if DB_NAME in DBlist:
        print(f"DB: '{DB_NAME}' exists")
        return True
    print(f"DB: '{DB_NAME}' not yet present in the DB")
    return False

def checkExistence_COL(COLLECTION_NAME, DB_NAME, db):
    collection_list = db.list_collection_names()
    if COLLECTION_NAME in collection_list:
        print(f"Collection:'{COLLECTION_NAME}' in Database:'{DB_NAME}' exists")
        return True
    print(f"Collection:'{COLLECTION_NAME}' in Database:'{DB_NAME}' does not exist OR no documents are present in the collection")
    return False

def main():
    parser = argparse.ArgumentParser(description='Convert CSV to MongoDB.')
    parser.add_argument('filename', type=str, help='The CSV file to convert')
    args = parser.parse_args()

    df = pd.read_csv(args.filename, header=[0, 1])

    table_ranges = [
        (0, 18),  # table 1: monday
        (21, 39),  # table 2: tuesday
        (42, 60),  # table 3: wednesday
        (63, 81),  # table 4: thursday
        (84, 102),  # table 5: friday
        (105, 123)  # table 6: saturday
    ]

    table_data = extract_table_data(df, table_ranges)

    client = MongoClient(os.environ.get('URI'))
    print(client.test)
    print(client.list_database_names())

    _ = checkExistence_DB(DB_NAME=os.environ.get('DB'), client=client)

    db = client[os.environ.get('DB')]
    print(db)
    print(client.list_database_names())

    collection = db[os.environ.get('COLLECTION')]

    _ = checkExistence_COL(COLLECTION_NAME=os.environ.get('COLLECTION'), DB_NAME=os.environ.get('DB'), db=db)

    for data in table_data:
        collection.insert_many(data)
    
    print(f"CSV file '{args.filename}' has been converted to MongoDB.")

if __name__ == "__main__":
    main()
