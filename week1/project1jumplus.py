#importing libraries 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

path_to_file = 'C:/Users/MD_Rahman/Desktop/Cognixia/JUMPlus/JUMPlus/week1/players_20.csv'

if os.path.isfile(path_to_file):
    print("File exists")
else:
    print("File not found")

file1 = "players_20.csv"

#1.Load the csv file and show top 5 records from it
df = pd.read_csv(path_to_file)
df.head()

#2. How you would be able to see each column's name.
print(df.columns.tolist())

# for col in df.columns:
#   print(col)
# df["body_type"].unique()

#3. Need to show number of rows and columns of this dataset
print("number of rows: ", len(df))
print("number of columns: ", len(df.columns))
df.shape

#4. Show number of players and their countries.
# Groupby multiple columns
result = df.groupby(['nationality']).agg(numOfPlayers=('short_name', 'count'))
result

# 5. If you find many records in point 4 then show only top 10 countries and their number of players.
top10 = result['numOfPlayers'].nlargest(n=10)
top10 = top10.to_frame().reset_index()
top10

#6. Now you have to create a bar plot of top 5 countries and their number of players, try to fill green color in bars.
#create bar plot with custom aesthetics
top5 = top10.sort_values(by="numOfPlayers", ascending=0)[:5]
top5.plot.bar(x='nationality', y='numOfPlayers', color="green")

plt.title("Countries with Most Players")
plt.xlabel("Countries")
plt.ylabel("Number Of Players")

#7. Show top 5 players short name and wages.
top5_wages = df.nlargest(5, 'wage_eur')
top5_wages = top5_wages[["short_name","wage_eur"]]
top5_wages.reset_index(drop=True)

#8. Show top 5 players short name and wages that are getting highest salaries.

top5_salary = df.nlargest(5, 'value_eur')
top5_salary = top5_salary[["short_name","wage_eur", 'value_eur']]
top5_salary.reset_index(drop=True, inplace=True)

top5_salary

#9.Create a bar plot of point number 8
top5_salary.plot.bar(x='short_name', y='value_eur')
plt.title("Players with Highest Salary")
plt.xlabel("Player's Name")
plt.ylabel("Euro Pound")

"""#Germany(10-12)"""

#filtering the country name
def germany(col, other_cols):
  germany = df[df.nationality == "Germany"]
  germany_top10 = germany.nlargest(10,[f"{col}"])
  
  germany_top10 = germany_top10.reset_index(drop=True)
  other_cols.insert(0,"short_name")
  return germany_top10[other_cols]

#10.Show top 10 records of Germany. #overall
germany("overall",["overall", "nationality"])

germany("height_cm",["height_cm", "nationality"])

#11.Now show top 5 records of Germany players who have maximum height, weight and wages.
# germany("height_cm",["height_cm"])
# germany("weight_kg",["weight_kg"])
germany("wage_eur",["wage_eur"])

#12.Show short name and wages of top 5 Germany players.
germany("wage_eur",["wage_eur"]).head()

#13.Show top 5 players who have great shooting skills among all with short name.
top5_shooter = df.nlargest(5, 'shooting')
top5_shooter = top5_shooter[["short_name","shooting"]].reset_index(drop=True)

top5_shooter

# 14.Show top 5 players records (short name, defending, nationality, and club) that have awesome defending skills

defending_top5 = df.nlargest(5,["defending"])
defending_top5[['short_name',"defending","nationality", "club"]]

"""#Real Madrid(15-18)"""

#function for Real Madrid
def real_Madrid(col,*args):
  realMadrid = df[df.club == "Real Madrid"]
  realMadrid_top5 = realMadrid.nlargest(5,[f"{col}"])
  realMadrid_top5.reset_index(drop=True, inplace=True)
  return realMadrid_top5[['short_name',*args]]

# 15.Show wages records of top 5 players of 'Real Madrid' team.
real_Madrid("wage_eur","wage_eur", "club")

# 16.Show shooting records of top 5 players of 'Real Madrid' team.
real_Madrid("shooting")

# 17.Show defending records of top 5 players of 'Real Madrid' team.
real_Madrid("defending")

# 18.Show nationality records of top 5 players of 'Real Madrid' team.
real_Madrid("overall","overall", "nationality")

"""##Extension"""

#Top 5 USA players and Wages. 
df["value_usd"] = df["value_eur"]*1.09
df[["value_usd", "value_eur"]].head(3)
usa_top5 = df[df.nationality == "United States"].nlargest(5,["value_usd"])
usa_top5[['short_name',"value_usd"]]

df.plot(kind = 'scatter', x = 'overall', y = 'wage_eur')

plt.figure(figsize= (10,8))
temp_df = df.groupby("age")["value_usd"].mean().reset_index()
sns.barplot(
    data = temp_df,
    x = "age",
    y = "value_usd"
    
);
plt.title("Age vs Value USD", fontsize = 15, weight = "bold");
plt.ticklabel_format(style='plain', axis='y');

df[["short_name", "age","wage_eur", "nationality"]][df["age"]==41]

plt.figure(figsize= (10,8))
temp_df = df.groupby("team_position")["wage_eur"].mean().reset_index()
sns.barplot(
    data = temp_df,
    x = "team_position",
    y = "wage_eur"    
)
plt.xticks(rotation= 90);
plt.title("Team Position vs Wage EUR", fontsize = 15, weight = "bold");

temp_df = df.groupby("team_position")["wage_eur"].count()
temp_df

df[["short_name", "team_position", "wage_eur", "value_usd"]][df["team_position"]=="CF"]

plt.figure(figsize= (10,8))
temp_df = df.groupby("club")["value_usd"].sum().sort_values(ascending = False)[:10].reset_index()

colors = sns.color_palette('pastel')

plt.pie(temp_df["value_usd"], labels = temp_df["club"], colors = colors, autopct='%.2f%%')
plt.title("Top 10 Clubs Spent", fontsize = 15, weight = "bold");

players20_updated = df.to_csv("players20_updated")
