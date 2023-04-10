#importing libraries 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import streamlit as st

path_to_file = 'C:/Users/MD_Rahman/Desktop/Cognixia/JUMPlus/JUMPlus/week1/players_20.csv'

if os.path.isfile(path_to_file):
    print("File exists")
else:
    print("File not found")

file1 = "players_20.csv"

#1.Load the csv file and show top 5 records from it
#@st.cache_data
def load_data(path_to_file):
    df = pd.read_csv(path_to_file)
    return df
df = load_data(path_to_file)


st.set_page_config(page_title="FIFA2020 Game Dashboad Analytics", page_icon=":tada:",layout="wide")

#header section

st.title(":red[FIFA 2020] :orange[Dateset] :green[Analysis]:soccer::chart::bar_chart:")
st.markdown("This is Fifa Dashboard by MD Rahman")
st.write("[GitHub link](https://github.com/mdrhmn48/JUMPlus/tree/main/week1)")


# def usa_player():
#     df["value_usd"] = df["value_eur"]*1.09
#     df[["value_usd", "value_eur"]].head(3)
#     usa_top5 = df[df.nationality == "United States"].nlargest(5,["value_usd"])
#     usa_top5[['short_name',"value_usd"]]
#     return usa_top5

# st.pyplot(usa_player())

def create_plot():
    st.subheader("USA Players Salary :soccer:")
    df["value_usd"] = df["value_eur"]*1.09
    df[["value_usd", "value_eur"]].head(3)
    usa_top5 = df[df.nationality == "United States"].nlargest(5,["value_usd"])
    usa_top5[['short_name',"value_usd"]]
    plt.figure(figsize= (10,8))
    temp_df = df.groupby("age")["value_usd"].mean().reset_index()
    sns.barplot(
        data = temp_df,
        x = "age",
        y = "value_usd"
    );
    plt.title("Age vs Value USD", fontsize = 15, weight = "bold")
    plt.ticklabel_format(style='plain', axis='y')
    return plt

st.pyplot(create_plot())
st.set_option('deprecation.showPyplotGlobalUse', False)

def create_piechart():
    plt.figure(figsize= (10,8))
    temp_df = df.groupby("club")["value_usd"].sum().sort_values(ascending = False)[:10].reset_index()

    colors = sns.color_palette('pastel')

    plt.pie(temp_df["value_usd"], labels = temp_df["club"], colors = colors, autopct='%.2f%%')
    plt.title("Top 10 Clubs Spent", fontsize = 15, weight = "bold");
st.pyplot(create_piechart())


#2. How you would be able to see each column's name.
print(df.columns.tolist())



#3. Need to show number of rows and columns of this dataset
print("number of rows: ", len(df))
print("number of columns: ", len(df.columns))
df.shape
