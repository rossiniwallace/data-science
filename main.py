import pandas as pd
from connection import execute_query

vinhos = execute_query("SELECT * FROM vinhos");

df = pd.DataFrame(vinhos)

print(df)