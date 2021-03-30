# NBA Stats Project

### Purpose of Project

The initial purpose of this project is to gather and use statistics from NBA.com to determine whether the number of Field Goal Attempts (FGA) correlates with whether a team wins or loses.

And then I will deploy an application showing the result of the data gathered.

### Steps

1. Gather

2. Write app

3. Deploy app

### Gather

The first step was to figure out what data I would need to gather.
I wanted to compare the number of times teams had more Field Goal Attempts(FGA) and won the game to when they had more FGA and lost the game. 
I need to gather a list of teams in the NBA and then each team's list of gamelogs for the 2019-2020 season. 

First I gathered the appropriate modules. There is an NBA api library that I installed from https://pypi.org/project/nba-api/. 
This api provides easier access to the endpoints from https://www.nba.com/. 
I used https://github.com/swar/nba_api to figure out which endpoints that I would need.

This next bit of code was used to gather the data from the endpoint and then store it in a csv file. 
It was originally included in the nba_test.py with no csv and just interactng with the endpoint.
It was changed as the nba api blocks cloud platforms like heroku which will be used to deploy the app.

from nba_api.stats.endpoints import leaguegamelog  
import pandas as pd

stuff = leaguegamelog.LeagueGameLog(season='2019-20')  
abcd = stuff.league_game_log.get_dict()  
teams = pd.DataFrame(abcd["data"], columns=abcd["headers"])  
teams.to_csv("2019-20_stats.csv", index=False)  

### Write app

Next, a script was written utilizing the libraries from numpy, matplotlib, and pandas and then run using streamlit.  
The data was read in and filtered to create the table with data I needed.  

The visual representation I chose was a pie chart as there are only two variables.
The pie chart will be able to give an appropriate visualization to not just answer our question, but to show if there is a large enough disparity to show if FGA in a NBA game is relvant to the outcome.

### Deploy app
Finally, I utilized heroku to deploy the app.  
The link showing the data and pie chart is [here](https://nba-stats-comp.herokuapp.com/).

###What's next
The next steps or to-dos will be to add a sidebar that will allow other statistical comparisons.
