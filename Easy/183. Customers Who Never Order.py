import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    pd1 = customers.merge(orders,left_on="id",right_on="customerId",how="left")
    pd1 = pd1[pd1['id_y'].isna()]

    pd1 = pd1.rename(columns={"name":"Customers"})
    return pd1[["Customers"]]
