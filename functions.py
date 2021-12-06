#importing packages
import pandas as pd
import scipy as sp
from scipy import stats
import matplotlib.pyplot as plt

#rank all columns in the dataframe
#adapted from https://stackoverflow.com/questions/28218698/how-to-iterate-over-columns-of-pandas-dataframe-to-run-regression
#rank code adapted from https://www.dataindependent.com/pandas/pandas-rank/
def rank_data (dataset, ranked_dataset): 
    """Rank data from highest to lowest for each 
    column of dataset
    
    Parameters
    -------------------------------
    dataset: pd.DataFrame
        The dataframe that is looped through and 
        rows are ranked from lowest to highest
    ranked_dataset: pd.DataFrame
        The dataframe that has countries as index
        and the ranked values are added to
        
    Retruns
    --------------------------------
    ranked_dataset: pd.DataFrame
        The complete ranked dataset for each column
    """
    
    for columns in dataset:
        ranked_dataset[columns] = dataset[columns].rank()
    return ranked_dataset

#stats of data
#stats code adapted from module 16
def stats_covid_data (data): 
    """Take basic statistics of a dataset
    
    Parameters
    -----------------------------------
    data: pd.DataFrame
        The dataframe in which basic statstics
        are taken for each column
    
    Returns
    -----------------------------------
    stats_data: pd.DataFrame
        The dataframe of basic statistics
        for each column.
    """
    
    stats_data = data.describe()
    return stats_data

#Ttest of data
#ttest code adapted from module 16 
def ttest (variable_1, variable_2, data):
    """Peforms a ttest on two columns from a dataset
    
    Parameters
    -------------------------------------
    variable_1: panda.Series
        The column name that'll be compared
        in the ttest.
    variable_2: panda.Series
        The column name that'll be compared
        in the ttest. 
    data: pd.DataFrame
        The dataframe that variable_1 and
        variable_2 are in
        
    Returns
    --------------------------------------
    p_value: sp.stats.stats.Ttest_indResult
        p value of the ttest
    """
    
    p_value = stats.ttest_ind(data[variable_1], data[variable_2])
    return p_value

#Create scatterplot of data
#adapted from create scatter matrix https://pandas.pydata.org/docs/reference/api/pandas.plotting.scatter_matrix.html, 
#adapted from https://stackoverflow.com/questions/50590900/how-to-make-plot-bigger
def scatter_matrix (size_x, size_y, data):
    """Create a scatterplot of the dataset
    
    Parameters
    ---------------------------------------
    size_x: int or float
        The size of the x axis
    size_y: int or float
        The size of the y axis
    data: pd.DataFrame
        The dataframe that is being plotted.
        
    Returns
    --------------------------------------
    scatterplot: None
        The scatterplot of the dataframe.
    """
    
    pd.plotting.scatter_matrix(data.rank(), figsize = (size_x,size_y))
    
#Create histogram of data
#adapted from module 16
def histogram (variable_1, data):
    """Create a histogram of one column of the
    dataset
    
    Parameters
    -------------------------------------------
    variable_1: panda.Series
        The column the histogram is made from
    data: pd.DataFrame
        The dataframe the histogram is made from
    
    Returns
    -------------------------------------------
    histogram: None
        The histogram of the column of the dataset.
    """
    
    plt.hist(data[variable_1], 25, alpha = 0.6)

#create pie chart of data
#adapted from https://www.w3schools.com/python/matplotlib_pie_charts.asp
#adapted from https://stackoverflow.com/questions/29786807/how-to-make-a-pie-chart-smaller-with-matplotlib
def pie_chart (values, size, labels):
    """Create a pie chart of one column of the
    dataset
    
    Parameters
    ---------------------------------------------
    values: panda.Series
        The values being evaluated as proportions
        in the pie chart.
    size: int or float
        the size of the pie chart
    labels: panda.Series
        The labels of each portion of the pie chart.
        
    Returns
    ---------------------------------------------
    pie chart: None
        The pie chart of the column of the dataset.
    """
    
    plt.pie(values, labels = labels, radius = size)
    plt.show()

#create bar graph of data
#adapted from https://datatofish.com/bar-chart-python-matplotlib/
#adapted from https://www.pythonpool.com/matplotlib-figsize/
def bar_graph (xAxis, yAxis):
    """Create a bar graph of one column of the 
    dataset
    
    Parameters
    -----------------------------------------------
    xAxis: panda.Series
        The x axis of the bar chart.
    yAxis: panda.Series
        The y axis of the bar chart.
        
    Returns
    ---------------------------------------------
    bar chart: None
        The bar chart of the x and y axis.
    """
    
    plt.bar(xAxis, yAxis)
    plt.xticks(rotation = 90)
    plt.figure(figsize = (15,6))
    plt.show()
    

