""" 
open the csv file called "nfl_offensive_stats.csv" in this workspace and read in
the csv data from the file
"""
# read in the csv file
import csv


with open("nfl_offensive_stats.csv", "r") as nflfile:
    data = list(csv.reader(nflfile))

""" 
In the data we just read in, the 4th column is the player name, the 3rd column is the position,
and the 8th column is the passing yards. 
For each player whose position is "QB",
determine the sum of yards from column 8. Save player name and total yards in new dictionary.
"""
# create a dictionary to store the player name and total yards
total_yards = {}

# loop through the data and add up the total yards for each player
for row in data:
    if row[2] == "QB":
        if row[3] in total_yards:
            total_yards[row[3]] += int(row[7])
        else:
            total_yards[row[3]] = int(row[7])

# print the total yards for each player sorted by total yards in descending order
for player in sorted(total_yards, key=total_yards.get, reverse=True):
    print(player, total_yards[player])

"""
plot the players by their number of passing yards only for 
players with more than 4000 passing yards.
The horizontal axis should be the player name and the vertical axis should be the total yards.
"""
# import the matplotlib library

import matplotlib.pyplot as plt

# create a list of players with more than 4000 passing yards

players = []
yards = []

for player in sorted(total_yards, key=total_yards.get, reverse=True):
    if total_yards[player] > 4000:
        players.append(player)
        yards.append(total_yards[player])

# plot the players by their number of passing yards
        
plt.bar(players, yards)
plt.xlabel("Players")
plt.ylabel("Total Yards")
plt.xticks(rotation=90)
plt.title("Players with more than 4000 Passing Yards")
plt.show()
