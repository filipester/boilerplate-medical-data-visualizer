import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['height'] = df['height'] / 100
df['overweight'] = ((df['weight'] / (df['height'] ** 2)) > 25).astype(int)

# 3
df['cholesterol'] = df.apply(lambda x : 0 if x['cholesterol'] == 1 else 1, axis=1).astype(int)
df['gluc'] = df.apply(lambda x : 0 if x['gluc'] == 1 else 1, axis=1).astype(int)

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars='cardio', value_vars = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])


    # 6
    df_cat = df_cat['cardio'].value_counts()
    

    # 7



    # 8
    fig = None


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = None

    # 12
    corr = None

    # 13
    mask = None



    # 14
    fig, ax = None

    # 15



    # 16
    fig.savefig('heatmap.png')
    return fig
