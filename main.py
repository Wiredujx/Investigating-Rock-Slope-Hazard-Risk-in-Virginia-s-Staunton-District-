import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency, random_table

alpha = 0.05

def importData():
    rock_slopes = pd.read_csv('Rock_Slopes_Table-Rock_Slope_Data.csv', encoding='cp1252')
    #print(rock_slopes.to_string())
    #print(rock_slopes.head(5).to_string())
    return rock_slopes

def chiSquared(rock_slopes):

    risk_summary = (
    rock_slopes.groupby("County")["Risk"] #groupby: groups dataframe by unique values in specified column. risk will be selected as the working column
    .value_counts() #value_counts: counts each unique risk amount
    .unstack(fill_value=0) #unstack: converts one level of a multi-level index and converts to columns
    .reindex(columns=["Low", "Medium", "High"], fill_value=0) #reindex: specifies column order
    )

    risk_summary.columns.name = None #fixes from formatting


    #for printing to console
    risk_summary = risk_summary.rename(columns={
    "County": "County",
    "Low": "Low",
    "Medium": "Medium",
    "High": "High"
    })
    print(risk_summary)


    #chi2 test of independence 
    chi2, p, dof, expected = chi2_contingency(risk_summary)
    print("Chi-square statistic:", chi2)
    print("P-value:", p)
    print("Degrees of freedom:", dof)

    #examine expected frequencies
    expected_df = pd.DataFrame(expected,
        index=risk_summary.index,
        columns=risk_summary.columns
        )

    print(expected_df.round(2))

    #bins with count less than 5
    bins_five = (expected < 5).sum()
    print("Bins with expected count < 5:",bins_five)

    bins_five_percent = (expected < 5).mean() * 100
    print("Percentage of bins with expected count < 5:",bins_five_percent)

    if(bins_five_percent > 30):
        print("The number of bins that contain a number less then 5 is more than 30%, interpret results with caution.")
        print("Use another statistical tool to reenforce results.")

    
    #hypothesis
    print("Null hypothesis: There is not an association between county and risk classification.")
    print("Alternative hypothesis: There is an association between county and risk classification.")
    if (p < alpha):
        print("\nChi2 result: the p-value is less than alpha, reject the null hypothosis.")
    else:
        print("\nChi2 result: the p-value is greater than alpha, fail to reject the null hypothesis.\n")

    

    return risk_summary

def monteCarlo(risk_summary):
    n_simulations = 100000
    rng = np.random.default_rng(42)

    chi2_observed,_,_,expected = chi2_contingency(risk_summary, correction=False)

    rows_totals = risk_summary.sum(axis=1)
    columns_totals = risk_summary.sum(axis=0)

    simulated_tables = random_table.rvs(rows_totals, columns_totals, size=n_simulations, random_state=rng)
    
    expected = np.outer(rows_totals, columns_totals)/risk_summary.values.sum()

    simulated_chi2=np.sum((simulated_tables - expected)**2/expected, axis=(1,2))

    p = (1+np.sum(simulated_chi2 >= chi2_observed))/(n_simulations+1)

    print("\n\n\n Monte Carlo test. \n\n")
    print("Observed chi2: ", chi2_observed)
    print("number of simulations: ", n_simulations)
    print("monte carlo p-vaule: ", p)

    #hypothesis
    print("Null hypothesis: There is not an association between county and risk classification.")
    print("Alternative hypothesis: There is an association between county and risk classification.")
    if (p < alpha):
        print("\nChi2 result: the p-value is less than alpha, reject the null hypothosis.")
    else:
        print("\nChi2 result: the p-value is greater than alpha, fail to reject the null hypothesis.\n")
    
    
    return

def main():
    rock_slopes = importData()
    risk_summary = chiSquared(rock_slopes)
    monteCarlo(risk_summary)

if __name__ == "__main__":
    main()