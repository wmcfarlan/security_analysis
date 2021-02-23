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


if __name__ == "__main__":
    df = pd.read_csv('data/terror_db.csv')

    post_df = df[
        (df.eventid >= 200109110004) & 
        (df.doubtterr == 0) &
        (df.attacktype1 != 9) &
        (df.weaptype1 != 13)
        ]

    top_df = post_df[
        (post_df.country_txt == 'Iraq') | 
        (post_df.country_txt == 'Pakistan') | 
        (post_df.country_txt == 'Afghanistan') | 
        (post_df.country_txt == 'India') | 
        (post_df.country_txt == 'Colombia')
        ]
