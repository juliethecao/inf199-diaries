import csv
import pandas as pd
import pymongo

df=pd.read_csv("d-p1.csv", header=[0,1])

# print(df)

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

table_ranges = [
    (0, 18),  # table 1: monday
    (21, 39),  # table 2: tuesday
    (42, 60),  # table 3: wednesday
    (63, 81),  # table 4: thursday
    (84, 102),  # table 5: friday
    (105, 123)  # table 6: saturday
]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# create dict to store dfs for each table
table_data = []

# create dfs for each table
for idx, (start, end) in enumerate(table_ranges, start=0):
    # table_name = days[idx]
    table_df = create_table(df, start, end)
    # print(f"Table Name: {table_name}")

    table_dict = table_df.to_dict(orient='records')
    # table_data.append({days[idx]: table_dict})
    table_data.append(table_dict)

    # for data in table_data:
    #     print(data)
    #     print("\n")

client = pymongo.MongoClient("mongodb+srv://<username>:<password>@<projectname>.8db8is9.mongodb.net/?retryWrites=true&w=majority&appName=INF199Diaries")
print(client.test)
print(client.list_database_names())

def checkExistence_DB(DB_NAME, client):
    DBlist = client.list_database_names()
    if DB_NAME in DBlist:
        print(f"DB: '{DB_NAME}' exists")
        return True
    print(f"DB: '{DB_NAME}' not yet present present in the DB")
    return False


_ = checkExistence_DB(DB_NAME="practiceDiaries", client=client)

db=client["practiceDiaries"]
print(db)
print(client.list_database_names())

COLLECTION_NAME = "practiceDiariesDetails"
collection = db[COLLECTION_NAME]

def checkExistence_COL(COLLECTION_NAME, DB_NAME, db):
    collection_list = db.list_collection_names()

    if COLLECTION_NAME in collection_list:
        print(f"Collection:'{COLLECTION_NAME}' in Database:'{DB_NAME}' exists")
        return True

    print(f"Collection:'{COLLECTION_NAME}' in Database:'{DB_NAME}' does not exists OR \n\
    no documents are present in the collection")
    return False


_ = checkExistence_COL(COLLECTION_NAME="practiceDiariesDetails", DB_NAME="practiceDiaries", db=db)

for data in table_data:
    collection.insert_many(data)

# for i in collection.find():
#     print(i)

