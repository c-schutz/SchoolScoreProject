import matplotlib.pyplot as plt
import csv
import school_scores
import pandas as pd
import numpy
def make_numeric(column):
    column = pd.to_numeric(column, errors='coerce')
    return column

data_points = school_scores.get_record()
if __name__ == '__main__':
    scores_file = 'school_scores.csv'
    df = pd.read_csv(scores_file) # shorthand for using file


    #Indexes within csv file
    math_2to3 = 65
    verb_2to3 = 68
    math_3to4 = 71
    verb_3to4 = 74
    math_4to5 = 77
    verb_4to5 = 80
    math_5to6 = 83
    verb_5to6 = 86
    math_6to7 = 89
    verb_6to7 = 92
    math_7to8 = 95
    verb_7to8 = 98
    the_arts_GPA = 6



    people_in_SAT_4to6 = (df.iloc[:54, math_2to3].sum())//53 + (df.iloc[:54, verb_2to3].sum())//53
    people_in_SAT_6to8 = (df.iloc[:54, math_3to4].sum())//53 + (df.iloc[:54, verb_3to4].sum())//53
    people_in_SAT_8to10 = (df.iloc[:54, math_4to5].sum())//53 + (df.iloc[:54, verb_4to5].sum())//53
    people_in_SAT_10to12 = (df.iloc[:54, math_5to6].sum())//53 + (df.iloc[:54, verb_5to6].sum())//53
    people_in_SAT_12to14 = (df.iloc[:54, math_6to7].sum())//53 + (df.iloc[:54, verb_6to7].sum())//53
    people_in_SAT_14to16 = (df.iloc[:54, math_7to8].sum())//53 + (df.iloc[:54, verb_7to8].sum())//53

    arts = df['Academic Subjects.Arts/Music.Average GPA'].tolist()
    arts = arts[1:54:9]
    People_in_SAT_Ranges = [people_in_SAT_4to6, people_in_SAT_6to8, people_in_SAT_8to10, people_in_SAT_10to12,
                            people_in_SAT_12to14, people_in_SAT_14to16]
    SAT_ranges = ['4-6', '6-8', '8-10', '10-12', '12-14', '14-16']

    fig, ax1 =plt.subplots()
    ax1.bar(SAT_ranges, People_in_SAT_Ranges, color ='b', alpha =0.7, label ='People in SAT Range')
    ax1.set_xlabel('SAT Scoring Ranges')
    ax1.set_ylabel('People in SAT Range', color = 'b')
    ax1.tick_params('y', colors = 'b')
    ax2 = ax1.twinx()
    ax2.plot(SAT_ranges, arts, color='r', marker='o', label='GPA in the Arts')
    ax2.set_ylabel('Arts GPA', color='r')
    ax2.tick_params('y',colors='r')



    plt.title('The Relationship between GPA in the Arts and SAT Score Ranges in 2005')
    plt.show()


























