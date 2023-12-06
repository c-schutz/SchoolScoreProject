from scipy.stats import ttest_ind


# function that will perform t test and print out a statistical analysis like p-val and t-stat
# this test is used to tell whether there is a statistically significant difference, and will be using pandas
def calc_t_test(dataframe, sample1_col, sample2_col, sample1_name, sample2_name, sample1_count, sample2_count,
                alpha=0.05):
    """
    Parameters:
        dataframe - the pandas dataframe
        sample1_col - the name of the column in that dataframe that you want as the first sample
        sample2_col - the name of the column in given dataframe that you will compare with sample1
        sample1_name - the name of the sample data1, e.g. Gender.Male.Math can be "male math scores"
        sample2_name -
        sample1_count - the count who are in sample1
        sample2_count - the count who are in sample2
        alpha - the significance level, preset as 0.05, lowering alpha means lower chance of committing type1 error     
    """
    # will be rounding everthing to the 4th decimal point if needed
    # sample size
    size_sample1 = dataframe[sample1_col].sum()
    size_sample2 = dataframe[sample2_col].sum()

    # mean of sample
    mean_sample1 = round(dataframe[sample1_col].mean(),4)
    mean_sample2 = round(dataframe[sample2_col].mean(),4)

    # standard deviations
    stan_dev_sample1 = round(dataframe[sample1_col].std(),4)
    stan_dev_sample2 = round(dataframe[sample2_col].std(),4)

    # performing t-test, p-val is used to compare with alpha
    t_test, p_val = ttest_ind(dataframe[sample1_col], dataframe[sample2_col], equal_var=False)
    t_test = round(t_test,4)



    # reject or fail to reject null hypoth

    if p_val < alpha:
        hypothesis_result = ("Successfully rejected the null hypothesis, "
                             "there is a statistically significant difference between the 2 samples ")
    else:
        hypothesis_result = ("Failed to reject the null hypothesis, "
                             "there is not a statistically significant difference between the 2 samples")


    #print all of results
    print(f'Sample 1 = {sample1_name}\nSample 2 = {sample2_name}')
    print(f'{sample1_name}(sample1) sample size: {size_sample1}')
    print(f'{sample2_name}(sample2) sample size: {size_sample2}')
    print(f'{sample1_name}(sample1) mean: {mean_sample1}')
    print(f'{sample2_name}(sample2) mean: {mean_sample2}')
    print(f'{sample1_name}(sample1) standard deviation: {stan_dev_sample1}')
    print(f'{sample2_name}(sample2) standard deviation: {stan_dev_sample2}')
    print(f'T-stat: {t_test}')
    print(f'P-val: {p_val}')
    print(f'Alpha level: {alpha}')
    print(f'Conclusion: {hypothesis_result}')


