import pandas as pd
import matplotlib.pyplot as plt
import csv
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


