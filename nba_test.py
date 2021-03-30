from nba_api.stats.endpoints import leaguegamelog
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.markdown("""
This app retrieves a list of nba teams along with game statistics from a specific season. The stats are then used to compare the number of Field Goal Attempts(FGA) and whether the team with the most FGA won more often than not.
* **Python libraries:** nba_api, pandas, streamlit, numpy, matplotlib
* **Data source:** [NBA](https://www.nba.com/stats/).
""")

stuff = leaguegamelog.LeagueGameLog(season='2019-20')
abcd = stuff.league_game_log.get_dict()
teams = pd.DataFrame(abcd["data"], columns=abcd["headers"])
winning_teams = teams[(teams.WL) == "W"]
losing_teams = teams[(teams.WL) == "L"]


winning_teams["Opposing FGA"] = losing_teams['FGA'].to_numpy()
winning_teams['More FGA than Opposing Team'] = np.where(winning_teams['FGA'] > winning_teams['Opposing FGA'], 'YES', 'NO')
FGA_data = winning_teams['More FGA than Opposing Team'].value_counts()
new_labels = 'NO', 'Yes'
plt.pie(FGA_data, labels=new_labels)

st.dataframe(winning_teams)
st.pyplot(plt)

