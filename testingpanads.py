import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

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
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(7.5, 6.5))


# plotting female graph
axs[0].violinplot(female_math)
axs[0].set_title('Females')
axs[0].set_xlabel("Distribution of scores")
axs[0].set_ylabel('test scores')
axs[0].set_ylim(min_score-10, max_score+10)
#axs[0].violinplot(female_math)

axs[1].violinplot(male_math)
axs[1].set_xlabel("Distribution of scores")
axs[1].set_ylabel("Test Score")
axs[1].set_title("Males")
axs[1].set_ylim(min_score-10, max_score+10)

fig.suptitle("Violin plot of Female and Male Math Test Scores", y=.95)

#creating scatterplot with linear regression line

# create the figure and axes
fig, ax = plt.subplots(figsize=(10, 10))

# add the plots for each dataframe
sns.regplot(x="year", y="avg_female_math_score", data=merged_data, fit_reg=True, ci=None, label='df1')
sns.regplot(x="year", y="avg_male_math_score", data=merged_data, fit_reg=True, ci=None, ax=ax, label='df2')
ax.set(ylabel='y', xlabel='x')
ax.legend()

plt.show()