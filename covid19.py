import seaborn as sns
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

#TITLE
st.title('COVID-19 Di Indonesia')

#HEADER
st.header("Ini adalah Data Sebaran Covid-19 di Indonesia")

#WRITE
st.write("Membuat Tabel dari Data")
data = pd.read_csv('covid19_indonesia_time_series_all.csv')

# CHECKBOX
show_data = st.checkbox("Show Dataframe")
if show_data:
    st.write(data)

# BUTTON
info = data.shape
if st.button("Lihat Total Data"):
    st.write(info)

# RADIO BUTTON

Location = st.radio("Select Dataframe of Location", data.Location.unique())

# SELECT
Location_Level = st.selectbox("Select Dataframe of Location Level", data.Location_Level.unique())

#HEADER
st.header("VISUALISASI DATA")

# Membuat PLOT PAKE MATPLOTLIB

arr = np.random.normal(1, 1, 100)
st.write(arr)
fig, ax = plt.subplots()
plt.hist(arr, bins=20)
st.pyplot(fig)

#VISUALISASI DATASET
df_covid_19 = st.selectbox("Select column", ['New Cases', 'New Deaths', 
    'New Recovered', 'Total Cases', 'Total Deaths', 'Total Recovered'])
fig = px.line(data,  x='Population', y=df_covid_19)
st.plotly_chart(fig)

plot = sns.relplot(x="Total Cases", y="Total Recovered", hue='Country', data=data)
st.pyplot(plot)

df = sns.relplot(x='Location', y='Total Cases', kind='line', data=data)
st.pyplot(df)