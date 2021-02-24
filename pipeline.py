import pandas as pd
import numpy as np

# plotting imports
import matplotlib.pyplot as plt
import seaborn as sns
import chart_studio.plotly as py
import plotly.express as px
import plotly.graph_objects as go

import warnings
warnings.filterwarnings('ignore')


def find_ratios(df, dum_col):
    dum_df = pd.get_dummies(df[dum_col])
    dum_df['success'] = df['success']

    feat_lst = dum_df.columns.tolist()[:-1]

    success_dct = {}
    fail_dct = {}

    for feat in feat_lst:
        ratio = dum_df[dum_df[feat] == 1]['success'].sum() / len(dum_df)
        success_dct[feat] = ratio
    
    for feat in feat_lst:
        ratio = dum_df[dum_df[feat] == 0]['success'].sum() / len(dum_df)
        fail_dct[feat] = ratio
    
    success_keys = [k for k, v in sorted(success_dct.items(), key=lambda x: x[1], reverse=True)]
    success_vals = [v for k, v in sorted(success_dct.items(), key=lambda x: x[1], reverse=True)]
    fail_keys = [k for k, v in sorted(fail_dct.items(), key=lambda x: x[1], reverse=True)]
    fail_vals = [v for k, v in sorted(fail_dct.items(), key=lambda x: x[1], reverse=True)]

    return (success_keys, success_vals, fail_keys, fail_vals)

# def year_counts(year_lst, df):
#     df_lst = []
#     for num, year in enumerate(year_lst):
#         attack_count = df[(df.iyear >= year) & (df.iyear <= (year + 4))].country_txt.value_counts()
#         year_df = pd.DataFrame(data = [attack_count.values], columns = attack_count.index)
#         df + str(num) = year_df.T.rename(columns={0: f'{year} events'})
#         df_lst.append(df + str(num))
    
#     merged_df = pd.concat(df_lst)
#     return merged_df

def create_combined_frame(primary_df, secondary_df):
    year_lst = [num for num in range(1970, 2011, 5)]
    df_lst = []
    for num, year in enumerate(year_lst):
        attack_count = primary_df[(primary_df.iyear >= year) & (primary_df.iyear <= (year + 4))].country_txt.value_counts()
        year_df = pd.DataFrame(data = [attack_count.values], columns = attack_count.index)
        num = year_df.T.rename(columns={0: f'{year}_events'})
        df_lst.append(num)
    
    merged_df = pd.concat(df_lst, axis=1)
    merged_df = merged_df.apply(lambda row: row.fillna(row.mean()), axis=1)
    merged_df['country'] = merged_df.index
    merged_df.reset_index(drop=True)
    
    final_merge = pd.merge(merged_df, secondary_df, left_on='country', right_on='Country Name')

    final_merge['total_attacks'] = round(final_merge['1970_events'] +
                               final_merge['1975_events'] +
                               final_merge['1980_events'] +
                               final_merge['1985_events'] +
                               final_merge['1990_events'] +
                               final_merge['1995_events'] +
                               final_merge['2000_events'] +
                               final_merge['2005_events'] +
                               final_merge['2010_events'])
    return final_merge

def event_count(merged_df):

    merged_df.reset_index(drop=True, inplace=True)
    
    event_lst = ['1970_events', '1975_events', '1980_events',
             '1985_events', '1990_events', '1995_events', '2000_events',
             '2005_events', '2010_events']
    
    edu_lst = ['1970', '1975', '1980', '1985', '1990',
           '1995', '2000', '2005', '2010']
    
    country_lst = merged_df['country'].tolist()
    
    data_dct = {'education': [], 'nattacks': []}
    for idx, _ in enumerate(country_lst):
        for atk in merged_df.loc[idx, event_lst]:
            data_dct['nattacks'].append(atk)
        for edu in merged_df.loc[idx, edu_lst]:
            data_dct['education'].append(edu)
    
    atk_vs_edu = pd.DataFrame.from_dict(data_dct)
    return atk_vs_edu

if __name__ == "__main__":
    print('main')