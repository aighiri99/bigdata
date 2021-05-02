import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    st.title('GNI per capita Vs. Life Expectancy')

    @st.cache
    def load_data():
        df1 = pd.read_csv("source_files/population_total.csv")
        df2 = pd.read_csv("source_files/life_expectancy_years.csv")
        df3 = pd.read_csv("source_files/ny_gnp_pcap_pp_cd.csv")
        df1 = df1.ffill()
        df2 = df2.ffill()
        df3 = df3.ffill()
        df1 = df1.melt(id_vars = ['country'], var_name='year', value_name='Population')
        df2 = df2.melt(id_vars = ['country'], var_name='year', value_name='Life_Expectancy')
        df3 = df3.melt(id_vars = ['country'], var_name='year', value_name='GNI_per_capita')
        df = df1.merge(df2, on = ['country', 'year'])
        df = df.merge(df3, on = ['country', 'year'])
        return df

    df = load_data()
    year = st.sidebar.slider('Year', min_value=min(df['year'].astype('int').unique().tolist()), max_value=max(df['year'].astype('int').unique().tolist()))
    x = df[(df['year'].astype('int') == year)]['GNI_per_capita'].values
    y = df[(df['year'].astype('int') == year)]['Life_Expectancy'].values
    sizes = df[(df['year'].astype('int') == year)]['Population'].values
    colors = df[(df['year'].astype('int') == year)]['country'].values
    g = sns.scatterplot(x=x, y=y, size = sizes, hue=colors)
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    g.set(xlim=(0, 100000))
    st.pyplot(plt)

if __name__ == '__main__':
	main()