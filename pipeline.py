import pandas as pd
print(pd.__version__)
# 1. Load the CSV
df = pd.read_csv("employees.csv")

# 2. Explore — print shape, columns, and first 5 rows
# your code here
print(df.shape);
print(df.columns);
print(df.head(5));
# 3. Clean:
#    - Fill missing salary with mean salary
#    - Fill missing name with "Unknown" 
# Q1 — How many employees per department?
print(df["department"].value_counts())

# Q2 — Average salary per country?
print(df.groupby("country")["salary"].mean())

# Q3 — Top 3 highest paid (name and salary)?
print(df.sort_values("salary", ascending=False)[["name","salary"]].head(3))

# Q4 — Engineering employees with experience > 4?
print(df[(df["department"] == "Engineering") & (df["experience"] > 4)])