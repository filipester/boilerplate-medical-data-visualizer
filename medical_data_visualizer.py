import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['overweight'] = ((df['weight'] / ((df['height']/100) ** 2)) > 25).astype(int)

# 3
df['cholesterol'] = df.apply(lambda x : 0 if x['cholesterol'] == 1 else 1, axis=1).astype(int)
df['gluc'] = df.apply(lambda x : 0 if x['gluc'] == 1 else 1, axis=1).astype(int)

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars='cardio', value_vars = ['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])

    # 8
    fig = sns.catplot(x="variable", hue="value", col="cardio", data=df_cat, kind='count')
    fig.set_axis_labels("variable", "total")

    fig=fig.fig
    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df.loc[df['ap_lo'] <= df['ap_hi']]
    df_heat = df_heat.loc[df_heat['height'] >= df['height'].quantile(0.025)]
    df_heat = df_heat.loc[df_heat['height'] <= df['height'].quantile(0.975)]
    df_heat = df_heat.loc[df_heat['weight'] >= df['weight'].quantile(0.025)]
    df_heat = df_heat.loc[df_heat['weight'] <= df['weight'].quantile(0.975)]
    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(corr)



    # 14
    fig, ax = plt.subplots(figsize=(10,10))

    # 15


    ax = sns.heatmap(corr, linewidths=.5, annot=True, fmt='.1f', mask=mask, square=True, center=0, vmin=-0.1, vmax=0.25, cbar_kws={'shrink':.45, 'format':'%.2f'})
    # 16
    fig.savefig('heatmap.png')
    return fig
