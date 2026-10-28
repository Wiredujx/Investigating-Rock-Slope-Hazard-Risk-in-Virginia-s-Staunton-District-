<div align="center">

# Investigating Rock Slope Hazard Risk in Virginia's Staunton District

Project Group 24—Computational Masters

Treshaun T., Jayden W., Nathan Y.

Department of Engineering, James Madison University

Computational Methods in Engineering (ENGR 315), SECTION 003

Dr. Mercy Adeyemi-Kayode

</div>

INTRODUCTION 

For Computational Methods in Engineering (ENGR 315) at James Madison University, a final culminating assignment towards the end of the semester was 
assigned to every section of the course. The objective of the assignment is to explore a dataset of a chosen field of interest amongst self-organized 
teams. Project Group 24 (Computational Masters) was organized to complete this task. The expected project deliverables are: (1) a final report, (2) 
functional Visual Studio Code using Python, and (3) a final presentation with a demonstration. This document serves as a proposal for the following assignment.  

The team has agreed to develop a program to analyze rock slope data. This area of interest could fall within Engineering Geology, Geotechnical Engineering, 
Transportation/Infrastructure, and Environmental Engineering. As for the objectives of this assignment, the team intends to computationally analyze and 
visualize existing rock slope risk data to identify patterns and relationships within the inventory. 

The selected dataset (Rock_Slopes_Table-Rock_Slope_Data.csv) is from the Virginia Department of Transportation (VDOT) Staunton District's maintenance and inventory 
records. The data was collected initially to inventory rock slopes within the VDOT's Staunton District. It was collected through means of field measurements and
on-site observations by VDOT staff.   

Relevant information from the dataset will be incorporated to analyze the qualitatively identified and classified rock slopes. The program will rank counties 
with the highest-risk slopes, identify any variance of the measured properties of slopes in the dataset, and show use of location identifiers to compare 
locations. The following table (Table 1) is a snippet of the following dataset. It contains location identifiers, observed characteristics, and qualitative 
identifiers of risk (Probability, impact, and total risk).
<div align="center">
Table 1 — Snippet of rock slope data

|   County  |  Latitude | Longitude  | Height (ft) | Length (ft) | Slope (°) | Clast Size (cy) | Clast Type | Probability | Impact |
|-----------|-----------|------------|-------------|-------------|-----------|-----------------|------------|-------------|--------|
| Alleghany | 37.867475 | -79.947153 |     70.2    |     415     |   61.5    |        12       | Spheroidal |     High    | Medium |
| Alleghany | 37.811385 | -79.798305 |     79.4    |     300     |   78.8    |        8        | Spheroidal |     High    | High   |
| Alleghany | 37.808559 | -79.797059 |     65.4    |     400     |   87.2    |        8        | Spheroidal |     High    | High   |
| Alleghany | 37.73331  | -80.22598  |     45.8    |     450     |   61.8    |        4        | Discoidal  |     High    | Medium |
</div>
CHOSEN QUESTIONS 

3. What clast types and sizes are most common in high-risk rock slope areas?  

Trends may be identified between Clast Type, Clast Size, and qualitative Risk classifications to determine whether certain rock characteristics are
more frequently associated with high-risk slopes. Variables of interest include Clast Type, Clast Size, and Risk. 

4. How can a qualitative risk matrix be used to evaluate the relationship between probability, impact, and overall risk classification? 

A qualitative risk matrix can be developed using probability, impact, and risk variables to show how overall risk is assigned throughout 
the dataset. Could help identify patterns in VDOT's risk classification process and provide additional context for the primary research questions. 

5. Is there a statistical association between county and rock slope risk classification? 

A chi-square test for independence can be performed using county and risk classifications to determine if the distribution of risk levels 
differs significantly among counties. This analysis may help determine if differences in county-level risk concentrations are statistically 
meaningful rather than random variation.  

 
IMPLEMENTATION DETAILS

Question 3: Clast Type Analysis 

Figure 1 is an example of how all the data on Risk and Clast types can be represented as a distribution of clast type to its risk factor. This will 
allow us to find the clast types that are common in high-risk areas. Spheroidal is the most common type in high-risk areas, followed by Discoidal.
There are no cylindrical type clasts in high-risk zones.  

Metrics: 
    Frequency of clast types 
    Frequency of clast sizes 
    Frequency of clast types among high-risk slopes 

Tools: 
    Pandas 
    NumPy 
    Matplotlib 

Methods: 

The dataset will be filtered to isolate high-risk rock slopes. Clast type and clast size frequencies will be calculated using Pandas and the max() 
function where appropriate to identify the most common categories. Frequency distributions and contingency tables will be generated to determine 
which rock characteristics occur most frequently in high-risk locations. 

Expected Visualizations: 

    Frequency of distribution bar charts 
    Crosstab tables 

 

Question 4: Qualitative Risk Matrix Analysis 

Figure 2 provides a visual representation of the relationship between Probability and Impact classifications within the rock slope inventory.
The matrix may help identify combinations that most frequently contribute to overall risk classifications and provide additional insight into
the qualitative risk assessment process used throughout the dataset. 

Metrics: 

    Frequency of probability classifications 
    Frequency of impact classifications 
    Frequency of probability-impact combinations 
    Overall risk classifications 

Tools: 

    Pandas 
    NumPy 
    Matplotlib 
    Seaborn 

Methods: 

A qualitative risk matrix will be developed using Probability, Impact, and Risk classifications from the dataset. Pandas will be used to
generate a crosstab table showing the frequency of each Probability-Impact combination. The resulting matrix will be used to examine how
combinations of probability and impact relate to overall risk classifications throughout the inventory. 

Expected Visualizations: 

    Risk matrix heatmap 
    Crosstab summary table 


Question 5: County-Risk Association Analysis 

To determine if there is an association between county and rock-slope risk classification, a chi-squared test of independence was performed
using Microsoft Excel. The null hypothesis (H₀) states that county and risk classification are independent while the alternative hypothesis
(Hₐ) states risk classification is associated with county. Table 3 presents the observed counts of high, medium, and low risk rock slopes for
each county. The table has 10 counties and 3 risk categories, resulting in 18 degrees of freedom, calculated from the formula, where r is the
number of rows and c is the number of columns. Table 4 presents the expected frequencies for each county and risk category using the formula:  
<div align="center">
$$
E = \frac{\text{County Total} \times \text{Risk Total}}{\text{Grand Total}}
$$
</div>
Table 5 summarizes the chi-squared test results. The calculated chi-square statistic is 34.46, with a corresponding p-value of 0.0110. At a
significance level of 0.05, the p-value is sufficiently small to reject the null hypothesis. This suggests that there is a significant
association between county and risk classification.  

 

However, a limitation of the analysis is that approximately 27% of cells have an expected frequency below 5. With the chi-squared test, it is
expected that at least 80% of the cells have a value of 5 or greater. With approximately 30% of the cells being below a count of 5, the results
should be interpreted with caution. 

 

A Monte Carlo simulation was also performed in excel. With 100,000 replicants, the Monte Carlo p-value was 0.010180. This was consistent with
the chi-squared test, suggesting that there is an association between county and risk level. 

<div align="center">
Table 4 –Count of Risk per County (Observed Frequency) 

| County     | High | Medium | Low | Total |
| ---------- | ---- | ------ | --- | ----- |
| Alleghany  | 6    | 22     | 28  | 56    |
| Augusta    | 7    | 11     | 7   | 25    |
| Bath       | 4    | 12     | 21  | 37    |
| Frederick  | 1    | 9      | 10  | 20    |
| Highland   | 0    | 14     | 28  | 42    |
| Page       | 0    | 5      | 6   | 11    |
| Rockbridge | 19   | 23     | 29  | 71    |
| Rockingham | 6    | 8      | 10  | 24    |
| Shenandoah | 4    | 14     | 7   | 25    |
| Warren     | 1    | 3      | 3   | 7     |
| Total      | 48   | 121    | 149 | 318   |
</div>

<div align="center">
Table 5 –Expected frequency 

| County     | High        | Medium      | Low         |
| ---------- | ----------- | ----------- | ----------- |
| Alleghany  | 8.452830189 | 21.3081761  | 26.23899371 |
| Augusta    | 3.773584906 | 9.512578616 | 11.71383648 |
| Bath       | 5.58490566  | 14.07861635 | 17.33647799 |
| Frederick  | 3.018867925 | 7.610062893 | 9.371069182 |
| Highland   | 6.339622642 | 15.98113208 | 19.67924528 |
| Page       | 1.660377358 | 4.185534591 | 5.15408805  |
| Rockbridge | 10.71698113 | 27.01572327 | 33.2672956  |
| Rockingham | 3.622641509 | 9.132075472 | 11.24528302 |
| Shenandoah | 3.773584906 | 9.512578616 | 11.71383648 |
| Warren     | 1.056603774 | 2.663522013 | 3.279874214 |
</div>
<div align="center">
Table 6 –χ2 and p-value (Chi-Square Results) 

| CHI-SQ statistic | P-value    |
| ---------------- | ---------- |
| 34.45993219      | 0.01104507 |
</div>

Metrics: 

    Observed frequencies 
    Expected frequencies 
    Chi-square statistic 
    Degrees of freedom 
    P-value 

Tools: 

    Pandas 
    NumPy 
    SciPy 

Methods: 

A chi-square test of independence will be performed to determine whether county and rock slope risk classification are statistically associated.
Observed frequencies will be calculated from the dataset and compared against expected frequencies. The chi-square statistic and p-value will
be used to determine whether differences among counties are statistically significant. A Monte Carlo simulation will be performed alongside the
chi-square test to confirm consistantcy as ~30% of the cells have values less than 5. 

Visualization: 

    Contingency tables 
    County-risk distribution charts 
    Chi-square summary table 



RESULTS 

(To be completed during PHASE II) 

CONCLUSIONS 

(To be completed during PHASE III) 