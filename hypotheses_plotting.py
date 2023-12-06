import matplotlib.pyplot as plt
import pandas as pd
import csv
import seaborn as sns

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv("school_scores.csv")

# Specify the states you want to include (FL and CA) and the columns you want to include
states_to_include = ["FL", "CA"]
columns_to_include = ["Year", "State.Code", "Total.Math", "Total.Test-takers"]

# Filter the DataFrame based on the specified states
filtered_df = df.loc[(df["State.Code"].isin(states_to_include)), columns_to_include]
filtered_df_fl = df.loc[(df["State.Code"] == "FL"), columns_to_include]
filtered_df_ca = df.loc[(df["State.Code"] == "CA"), columns_to_include]

# Print the filtered DataFrame
print(filtered_df)

# create the figure and axes
fig, ax = plt.subplots(figsize=(7, 7))

# add the plots for each dataframe
sns.regplot(x="Year", y="Total.Math", data=filtered_df_fl, fit_reg=True, ci=None, label='Florida Scores')
sns.regplot(x="Year", y="Total.Math", data=filtered_df_ca, fit_reg=True, ci=None, ax=ax, label='California Scores')
ax.set(ylabel='Total Math Scores', xlabel='Years')
ax.legend()

plt.show()