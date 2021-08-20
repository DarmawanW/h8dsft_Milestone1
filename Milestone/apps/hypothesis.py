from dash_html_components.Br import Br
from numpy import median
import plotly.express as px
import pandas as pd
from scipy import stats
 
import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
 
from app import app #change this line

df = pd.read_csv('supermarket_sales.csv')

female = df[(df['Gender'] == 'Female')]
male = df[(df['Gender'] == 'Male')]

female_median = female['Total'].median()
female_mean = female['Total'].mean()
female_mode = female['Total'].mode().iloc[0]
male_median = male['Total'].median()
male_mean = male['Total'].mean()
male_mode = male['Total'].mode().iloc[0]

female_range = female['Total'].max() - female['Total'].min()
female_stdev = female['Total'].std()
female_var = female['Total'].var()
female_iqr = female['Total'].quantile(0.75) - female['Total'].quantile(0.25)
male_range = male['Total'].max() - male['Total'].min()
male_stdev = male['Total'].std()
male_var = male['Total'].var()
male_iqr = male['Total'].quantile(0.75) - male['Total'].quantile(0.25)

def welch_ttest(x, y): 
    ## Welch-Satterthwaite Degrees of Freedom ##
    dof = (x.var()/x.size + y.var()/y.size)**2 / ((x.var()/x.size)**2 / (x.size-1) + (y.var()/y.size)**2 / (y.size-1))
   
    t, p = stats.ttest_ind(x, y, equal_var = False)

welch_ttest(female['Total'], male['Total'])
tval, pval = stats.ttest_ind(female['Total'], male['Total'], equal_var = False)
dofval = (female['Total'].var()/female['Total'].size + male['Total'].var()/male['Total'].size)**2 / ((female['Total'].var()/female['Total'].size)**2 / (female['Total'].size-1) + (male['Total'].var()/male['Total'].size)**2 / (male['Total'].size-1))

layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(
                html.H1("Hypothesis Testing"),
                className="mb-2 mt-2"
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.H6(children='In this Hypothesis Testing, by using the supermarket sales data,' 
                'we will be testing to see if there is a significant difference in the total sales between the Female Gender and Male Gender.'
                ),
                className="mb-4"
            )    
        ]),
        dbc.Row([
            dbc.Col(
                html.H6(children=['We define the hypothesis as:', html.Br(),
                'Null hypothesis (H0): u1 = u2, which translates to the mean of sample 1 is equal to the mean of sample 2.',html.Br(),
                'And the alternative hypothesis (HA): u1 ≠ u2, which translates to the mean of sample 1 is not equal to the mean of sample 2']),
                className="mb-4"
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.H2(children='Data Loading'),
                className="mb-4"
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.H6(children=['The dataset that we use in this hypothesis testing is the historical sales of supermarket company,'
                'which has recorded in 3 different branches for 3 months data',html.Br(),
                'The dataset contains:',html.Br(),
                '1. Branch & City Data', html.Br(),
                '2. Customer Type', html.Br(),
                '3. Gender', html.Br(),
                '4. Product Line', html.Br(),
                '5. Unit Price & Quantity', html.Br(),
                '6. Total Sales', html.Br(),
                '7. Date & Time', html.Br(),
                '8. Payment Type', html.Br(),
                '9. Others', html.Br(),
                'This dataset can be found at https://www.kaggle.com/aungpyaeap/supermarket-sales'
                ]),
                className="mb-4"
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.H2(children='Data Preprocessing'),
                className="mb-4"
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.H6(children='The loaded dataset then preprocessed by grouping the dataset by gender and total sales.'
                'New datasets are also created which consists only of Female Gender and Male Gender'),
                className="mb-4"
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.H2(children='Measures of Central Tendency'),
                className="mb-4"
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.H6(children=['A measure of central tendency is a summary statistic that represents the center point or typical value of a dataset.', html.Br(), 
                'There are three main measures of central tendency:', html.Br(),
                '1. Mean : the sum of the value of each observation in a dataset divided by the number of observations', html.Br(),
                '2. Mode : the most commonly occurring value in a distribution', html.Br(),
                '3. Median : the middle value in distribution when the values are arranged in ascending or descending order'
                ]),
                className="mb-4"
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.H6(children=['The average median of total sales in the female gender is: ' + format(female_median, '.2f'),html.Br(),
                'The average mean of total sales in the female gender is: ' + format(female_mean, '.2f'),html.Br(),
                'The average mode of total sales in the female gender is: ' + format(female_mode, '.2f'),html.Br(),
                'The average median of total sales in the male gender is: ' + format(male_median, '.2f'),html.Br(),
                'The average mean of total sales in the male gender is: ' + format(male_mean, '.2f'),html.Br(),
                'The average mode of total sales in the male gender is: ' + format(male_mode, '.2f')
                ]),
                className="mb-4"
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.H2(children='Measures of Variability'),
                className="mb-4"
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.H6(children=['A measure of variability is a summary statistic that represents the amount of dispersion in a dataset.',html.Br(),
                'There are 4 most commonly used measurement of variability:', html.Br(),
                '1. Range: the difference between the highest and lowest values of a dataset', html.Br(),
                '2. Variance: the average squared difference of the values from the mean', html.Br(),
                '3. Standard Deviation :  the standard or typical difference between each data point and the mean', html.Br(),
                '4. Interquartile Range : the range of the middle half of a distribution'
                ]),
                className="mb-4"
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.H6(children=['The range of total sales in the female gender is: ' + format(female_range,'.2f'), html.Br(),
                'The variance of total sales in the female gender is: ' + format(female_var,'.2f'), html.Br(),
                'The standard deviation of total sales in the female gender is: ' + format(female_stdev,'.2f'), html.Br(),
                'The interquartile range of total sales in the female gender is: ' + format(female_iqr,'.2f'), html.Br(),
                'The range of total sales in the male gender is: ' + format(male_range,'.2f'), html.Br(),
                'The variance of total sales in the male gender is: ' + format(male_var,'.2f'), html.Br(),
                'The standard deviation of total sales in the male gender is: ' + format(male_stdev,'.2f'), html.Br(),
                'The interquartile range of total sales in the male gender is: ' + format(male_iqr,'.2f')
                ]),
                className="mb-4"
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.H2(children='T-TEST'),
                className="mb-4"
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.H6(children='A t-test is a statistical test that is used to compare the means of two groups'
                'In this hypothesis testing, we use the t-test because we want to compare the means of total sales between Female Gender and Male Gender'),
                className="mb-4"
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.H6(children=['From the Welch t-test, it is obtained that the t-value is :' + format(tval, '.3f'), html.Br(),
                'And the p-value is :' + format(pval, '.3f'), html.Br(), 
                'With the degree of freedom is: ' +format(dofval,'.3f')]),
                className="mb-4"
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.H2(children='Results'),
                className="mb-4"
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.H6(children=['The current study aimed to test if there was a significant difference in the total sales amount between the Female and Male Gender.', html.Br(), 
                'The difference in total sales amount between Female Gender (Mean = 335.095; SD = 249.324) and Male Gender (Mean = 310.789; SD = 242.021) was insignificant (t (1.564) =997.340; p > 0.118).', html.Br(),
                'Our p-value of 0.118 is much higher than 0.05, therefore we accept the null hypothesis of no difference in the total sales amount between the Female and Male Gender']),
                className="mb-4"
            )
        ]),
    ])
])