#importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model  import LogisticRegression
import streamlit as st
import os



st.header("Alhamdulilah")
#https://github.com/mdrhmn48/JUMPlus/blob/main/week2/charcters_stats.csv
#file = "charcters_stats.csv"
# file = open(file)
# file.read()
# DATE_COLUMN = 'date/time'
# DATA_URL = (file)
# @st.cache_data
# def read_data(file):
#     data = pd.read_csv(file) #path folder of the data file
#     return data
# # st.write(data)

st.title("Hello world! hi how are you")

uploaded_file = st.file_uploader("charcters_stats.csv")
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.write("dataframe")
# data = read_data(file)
# st.title('Super Heroes Vs Super Villians')


# def load_data(nrows):
#     data = pd.read_csv(DATA_URL, nrows=nrows)
#     #lowercase = lambda x: str(x).lower()
#     #data.rename(lowercase, axis='columns', inplace=True)
#     #data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
#     return data


# # Create a text element and let the reader know the data is loading.

# # Load 10,000 rows of data into the dataframe.
# # @st.cache_data
# data = load_data(100)
# # Notify the reader that the data was successfully loaded.
