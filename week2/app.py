#importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model  import LogisticRegression
import streamlit as st
import pandas_bokeh
from bokeh.plotting import figure, show
file = "https://raw.githubusercontent.com/mdrhmn48/JUMPlus/main/week2/charcters_stats.csv"
def load_data():
   df = pd.read_csv(file)

   return df
  
df = load_data()
st.title(":red[Welcome to] :green[Marvel Data Analysis] 🤖👿🦸‍♂️⚒️:bar_chart:")
st.markdown("Marvel Data Analysis Dashboard, let's you explore the relationship between each super powers and villians")
# st.set_page_config(layout="wide")
scatter_fig = df.plot_bokeh.scatter(x="Intelligence", y="Strength", category = None,
                            xlabel = "Intelligence", ylabel="Strength", title = "Superheroes Superpowers",
                            fontsize_title = 25, fontsize_label=12,
                            figsize=(750,500), show_figure=False
                            )
st.bokeh_chart(scatter_fig)

# def create_bar(col):
#     plt.figure(figsize = (10,6))
#     temp_df = df.groupby("Alignment")[col].mean().round(decimals=2).reset_index()
#     ax = sns.barplot(
#         data = temp_df,
#         x = "Alignment",
#         y = col,
#         palette = ["#941A00", "#439429", "#1E38AD"]
#     )
#     plt.title(f"{col} with respect to Alignment", fontsize =  15, weight = "bold");
#     for i in ax.containers:
#         ax.bar_label(i,)
#     plt.show()

# cols = ['Intelligence', 'Strength', 'Speed', 'Durability', 'Power', 'Combat']
# for col in cols:
#     bar_plot = create_bar(col)
#     st.bar_chart(bar_plot)


# p = figure(x_range="Intelligence", height=350, title="Fruit Counts",
#            toolbar_location=None, tools="")

# p.vbar(x="Strength", top=counts, width=0.9)

# p.xgrid.grid_line_color = None
# p.y_range.start = 0

bar_plot = df.plot_bokeh(
    kind='bar',
    x='Total',
    y=['Intelligence', 'Strength', 'Durability'],
    xlabel='Category',
    ylabel='Annual Sales',
    title='Annual Sales by Category'
  )
st.bar_chart(bar_plot)