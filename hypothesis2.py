import matplotlib.pyplot as plt
import school_scores

data = school_scores.get_record()

math20To40 = 0
verbal20To40 = 0
math40To60 = 0
verbal40To60 = 0
math60To80 = 0
verbal60To80 = 0
math80To100 = 0
verbal80To100 = 0
mathLess20 = 0
verbalLess20 = 0
mathMore100 = 0
verbalMore100 = 0

for x in data:
    if x['Year'] != 2015:
        continue
    incomeData = x['Family Income']
    for y in x['Family Income']:
        if y == "Between 20-40k":
            math20To40 = math20To40 + x['Family Income']['Between 20-40k']['Math']
            verbal20To40 = verbal20To40 + x['Family Income']['Between 20-40k']['Verbal']
        if y == "Between 40-60k":
            math40To60 = math40To60 + x['Family Income']['Between 40-60k']['Math']
            verbal40To60 = verbal40To60 + x['Family Income']['Between 40-60k']['Verbal']
        if y == "Between 60-80k":
            math60To80 = math60To80 + x['Family Income']['Between 60-80k']['Math']
            verbal60To80 = verbal60To80 + x['Family Income']['Between 60-80k']['Verbal']
        if y == "Between 80-100k":
            math80To100 = math80To100 + x['Family Income']['Between 80-100k']['Math']
            verbal80To100 = verbal80To100 + x['Family Income']['Between 80-100k']['Verbal']
        if y == "Less than 20k":
            mathLess20 = mathLess20 + x['Family Income']['Less than 20k']['Math']
            verbalLess20 = verbalLess20 + x['Family Income']['Less than 20k']['Verbal']
        if y == "More than 100k":
            mathMore100 = mathMore100 + x['Family Income']['More than 100k']['Math']
            verbalMore100 = verbalMore100 + x['Family Income']['More than 100k']['Verbal']

avgLess20 = ((mathLess20/53)+(verbalLess20/53))
avg20To40 = ((math20To40/53)+(verbal20To40/53))
avg40To60 = ((math40To60/53)+(verbal40To60/53))
avg60To80 = ((math60To80/53)+(verbal60To80/53))
avg80To100 = ((math80To100/53)+(verbal80To100/53))
avgMore100 = ((mathMore100/53)+(verbalMore100/53))

satScores = [avgLess20, avg20To40, avg40To60, avg60To80, avg80To100, avgMore100]
income = ["Less than 20k", "20-40k", "40-60k", "60-80", "80-100k", "More than 100"]

x_values = income
y_values = satScores
plt.plot(x_values, y_values)
plt.title('Relationship between Household Income and SAT Scores')
plt.xlabel('Household Income')
plt.ylabel('SAT Scores')

plt.show()