import pandas as pd
from nba_api.stats.endpoints import leaguedashteamstats, leaguehustlestatsteam, leaguedashplayerstats, \
    leaguehustlestatsplayer, leaguedashptdefend

# Initialize DataFrames for each data source
df_team_stats = pd.DataFrame()
df_team_hustle_stats = pd.DataFrame()
df_player_stats = pd.DataFrame()
df_hustle_stats = pd.DataFrame()
df_defend_stats = pd.DataFrame()

# Fetching data for the 2022-2023 season

try:
    # Team Stats
    team_stats = leaguedashteamstats.LeagueDashTeamStats(season='2021-22')
    df_team_stats = team_stats.get_data_frames()[0]

    team_hustle = leaguehustlestatsteam.LeagueHustleStatsTeam(season='2021-22')
    df_team_hustle_stats = team_hustle.get_data_frames()[0]

    # Player Stats
    player_stats = leaguedashplayerstats.LeagueDashPlayerStats(season='2021-22')
    df_player_stats = player_stats.get_data_frames()[0]

    hustle_stats = leaguehustlestatsplayer.LeagueHustleStatsPlayer(season='2021-22')
    df_hustle_stats = hustle_stats.get_data_frames()[0]

    defend_stats = leaguedashptdefend.LeagueDashPtDefend(season='2021-22')
    df_defend_stats = defend_stats.get_data_frames()[0]


    df_team_stats = df_team_stats[['TEAM_ID', 'GP', 'BLK', 'BLKA', 'DREB', 'STL']]
    df_team_hustle_stats = df_team_hustle_stats[['TEAM_ID', 'CONTESTED_SHOTS', 'CONTESTED_SHOTS_2PT', 'CONTESTED_SHOTS_3PT',
                                            'DEFLECTIONS', 'CHARGES_DRAWN', 'LOOSE_BALLS_RECOVERED', 'BOX_OUTS']]
    df_player_stats = df_player_stats[['PLAYER_ID', 'PLAYER_NAME', 'TEAM_ID', 'GP', 'MIN', 'BLK', 'BLKA', 'STL', 'DREB']]
    df_hustle_stats = df_hustle_stats[['PLAYER_ID', 'BOX_OUTS', 'CONTESTED_SHOTS_2PT', 'CONTESTED_SHOTS_3PT',
                                       'CONTESTED_SHOTS', 'DEFLECTIONS', 'LOOSE_BALLS_RECOVERED', 'CHARGES_DRAWN']]
    df_defend_stats = df_defend_stats[['CLOSE_DEF_PERSON_ID', 'D_FG_PCT', 'NORMAL_FG_PCT', 'PCT_PLUSMINUS']]
    df_defend_stats = df_defend_stats.rename(columns={'CLOSE_DEF_PERSON_ID': 'PLAYER_ID'})

except Exception as e:
    print(f"An error occurred: {e}")

# Display the first few rows of each DataFrame for demonstration
#print("Team Stats:")
#print(df_team_stats.head())

#print("\nPlayer Stats:")
#print(df_player_stats.head())

#print("\nHustle Stats:")
#print(df_hustle_stats.head())

#print("\nDefend Stats:")
#print(df_defend_stats.head())


df_team_stats.to_csv('team_stats22', index=False)
df_team_hustle_stats.to_csv('team_hustle_stats22.csv', index=False)
df_player_stats.to_csv('player_stats22.csv', index=False)
df_hustle_stats.to_csv('hustle_stats22.csv', index=False)
df_defend_stats.to_csv('defend_stats22.csv', index=False)
