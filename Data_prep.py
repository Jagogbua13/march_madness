import pandas as pd
import numpy as np


df = pd.read_csv('combined_stats.csv')
#df.head()


def school_list():
    list_schools = df['TEAM'].values.tolist()
    return(list_schools)


def get_team(team):
    
    team_stat= df.loc[df['TEAM'] == team]
    new_df = team_stat[['FGA-game','assist_per_game','turnover_per_game']].values.tolist()
    stats = new_df[0]
    #print(stats)
    return(stats)



def model_prep(home,away):
    home_stats = get_team(home)
    away_stats = get_team(away)
    model_list = []
    
    for x in range(0,3):
        model_list.append(home_stats[x])
        model_list.append(away_stats[x])
    model_stats= {'h_field_goals_att':model_list[0],'a_field_goals_att':model_list[1], 'h_assists':model_list[2],'a_assists':model_list[3],
                  'h_turnovers':model_list[4],'a_turnovers':model_list[5]}
    model_df = pd.DataFrame(model_stats, index=[0])
    return(model_df)