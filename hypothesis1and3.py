import matplotlib.pyplot as plt
import pandas as pd
import csv
import seaborn as sns
from statistic_tests import calc_t_test

#Hypothesis 1
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

#hypothesis 3
# testing hypotheses about gender and satscores
# need: Gender.Male.Verbal, Gender.Male.Test-takers,Gender.Male.Math,
# Gender.Female.Verbal, Gender.Female.Test-takers, Gender.Female.Math, Year, Total.Test-takers



data_set = pd.read_csv("school_scores.csv")


# merging data_set so that all the states are added/averaged together for each year
# creating new data set with only needed values (year, people count(gender), people(gender), total people)

merged_data = pd.DataFrame(columns=["year", "total_count",
                                    "total_male_count", "avg_male_math_score", "avg_male_verbal_score",
                                    "total_female_count", "avg_female_math_score", "avg_female_verbal_score"])

for year in data_set["Year"].unique():
    year_data = data_set[data_set["Year"] == year]
    total_count = year_data["Total.Test-takers"].sum()
    total_male_count = year_data["Gender.Male.Test-takers"].sum()
    avg_male_math_score = round(year_data["Gender.Male.Math"].mean(),2)
    avg_male_verbal_score = round(year_data["Gender.Male.Verbal"].mean(),2)
    total_female_count = year_data["Gender.Female.Test-takers"].sum()
    avg_female_math_score = round(year_data["Gender.Female.Math"].mean(),2)
    avg_female_verbal_score = round(year_data["Gender.Female.Verbal"].mean(),2)

    add_row = pd.DataFrame({"year": year,
                            "total_count": total_count,
                            "total_male_count": total_male_count,
                            "avg_male_math_score": avg_male_math_score,
                            "avg_male_verbal_score": avg_male_verbal_score,
                            "total_female_count": total_female_count,
                            "avg_female_math_score": avg_female_math_score,
                            "avg_female_verbal_score": avg_female_verbal_score}, index=[0])

    merged_data = pd.concat([merged_data, add_row], ignore_index=True)


years = merged_data["year"]
female_math = merged_data["avg_female_math_score"]
male_math = merged_data["avg_male_math_score"]
min_score = min(female_math.min(), male_math.min())
max_score = max(female_math.max(), male_math.max())


# creating violin graph, takes test score of gender
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(6, 6.5))


# plotting female graph
axs[0].violinplot(female_math)
axs[0].set_title('Females')
axs[0].set_xlabel("Distribution of scores")
axs[0].set_ylabel('test scores')
axs[0].set_ylim(min_score-5, max_score+5)
#axs[0].violinplot(female_math)

axs[1].violinplot(male_math)
axs[1].set_xlabel("Distribution of scores")
axs[1].set_ylabel("Test Score")
axs[1].set_title("Males")
axs[1].set_ylim(min_score-5, max_score+5)

fig.suptitle("Violin plot of Female and Male Math Test Scores", y=.95)

#creating scatterplot with linear regression line

#this might fix error idk:
merged_data["year"] = merged_data["year"].astype(float)


# create the figure and axes
fig, ax = plt.subplots(figsize=(7, 7))

# add the plots for each dataframe
sns.regplot(x="year", y="avg_female_math_score", data=merged_data, fit_reg=True, ci=None, label='Female Math Score')
sns.regplot(x="year", y="avg_male_math_score", data=merged_data, fit_reg=True, ci=None, ax=ax, label='Male Math Score')
ax.set(ylabel='Mean Math Score ', xlabel='Years')
ax.legend()

plt.show()
pd.options.display.width= None
pd.options.display.max_columns= None
pd.set_option('display.max_rows', 575)
pd.set_option('display.max_columns', 1000)

print(calc_t_test(data_set, "Gender.Male.Math","Gender.Female.Math",
                  "male math scores", "female math scores",
                  "Gender.Male.Test-takers", "Gender.Female.Test-takers"))
