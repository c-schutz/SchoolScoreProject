import matplotlib.pyplot as plt
import pandas as pd
import csv

if __name__ == "__main__":
    #Hypotheses 1
    #open the csv file and collect the header
    file = open("school_scores.csv", "r")
    csv_file = csv.reader(file)
    header = next(csv_file)



    #Get all the rows of data
    rows = []
    for row in csv_file:
        rows.append(row)

    #Get one data set from each year
    rows_diff_years = []
    for i in range(1, len(rows)):
        if rows[i][0] != rows[i-1][0]:
            rows_diff_years.append(rows[i])

    #Data points
    years = []
    fam_income_20to40 = []
    fam_income_60to80 = []
    fam_income_over100 = []
    score_range_300to400_math = []
    score_range_300to400_verbal = []
    score_range_500to600_math = []
    score_range_500to600_verbal = []
    score_range_700to800_math = []
    score_range_700to800_verbal = []



    #Collect data from the years
    for val in rows_diff_years:
        years.append(val[0])
        fam_income_20to40.append(val[19])
        fam_income_60to80.append(val[29])
        fam_income_over100.append(val[24])
        score_range_300to400_math.append(val[71])
        score_range_300to400_verbal.append(val[74])
        score_range_500to600_math.append(val[83])
        score_range_500to600_verbal.append(val[86])
        score_range_700to800_math.append(val[95])
        score_range_700to800_verbal.append(val[98])

    #Graphing (in progress)
    x_values = fam_income_60to80
    y_values = years
    plt.plot(x_values, y_values)
    plt.xlabel('Income')
    plt.ylabel('Years')
    plt.show()

