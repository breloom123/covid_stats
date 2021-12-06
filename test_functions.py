#importing packages
import pandas as pd
import scipy as sp
from scipy import stats
import matplotlib.pyplot as plt

#defining parameters to functions
df = pd.read_csv("WHO_COVID_19.csv")
dropped_na_df = df.dropna()
dropped_na_df_index_country = dropped_na_df.set_index('country')
rank_df = pd.DataFrame(index = dropped_na_df['country'])

#importing functions that are being tested
from functions import rank_data
from functions import stats_covid_data
from functions import ttest

def test_rank_data():
    assert callable (rank_data)
    assert isinstance(rank_data(dropped_na_df_index_country,
                               rank_df), pd.DataFrame)
    assert rank_data(dropped_na_df_index_country,
                     rank_df)['cases_total'].max() == 21.0

def test_stats_covid_data():
    assert callable (stats_covid_data)
    assert isinstance(stats_covid_data(dropped_na_df), pd.DataFrame)
    assert stats_covid_data(dropped_na_df).shape == (8,11)
    
def test_ttest():
    assert callable (ttest)
    assert isinstance(ttest (variable_1 = 'cases_7_days_per_100000_pop', 
                             variable_2 = 'cases_total_per_100000_pop', 
                             data = dropped_na_df), sp.stats.stats.Ttest_indResult)



