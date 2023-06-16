import pandas as pd


fighters_df = pd.read_csv("fighters.csv", index_col=0)

print(fighters_df)

print(fighters_df.isnull().sum())

df = fighters_df
df.replace({"- -": None})

print(df)
print(df.isnull().sum())
