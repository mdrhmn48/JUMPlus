#importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model  import LogisticRegression
import streamlit as st
import os



st.header("Welcome to Marvel Dataset")
#file = "charcters_stats.csv"
# file = open(file)
# file.read()
# DATE_COLUMN = 'date/time'
# DATA_URL = (file)
# @st.cache_data
def read_data(file):
    data = pd.read_csv(file) #path folder of the data file
    return data



st.title("Hello world! hi how are you")

uploaded_file = st.file_uploader("charcters_stats.csv")
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.write("dataframe")
# data = read_data(file)
# st.title('Super Heroes Vs Super Villians')

