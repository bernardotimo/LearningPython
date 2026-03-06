import pandas as pd

sales = {"user_id": ["KM37", "PR19", "YU88"],
         "order_value": [197.75, 208.21, 134.99]}

sales_df = pd.DataFrame(sales) # Converts to DataFrame
print(sales_df)

# Reading in a CSV file in current directory
# sales_df = pd.read_csv("sales_df.csv")
print(type(sales_df))

print(sales_df.head()) # Preview the first five rows
print(sales_df.info()) # Checking file info