import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

player_stats22 = pd.read_csv('/Users/zachcarlson/Documents/NBA Project/2021-22/player_filtered_stats22.csv')
player_stats23 = pd.read_csv('/Users/zachcarlson/Documents/NBA Project/2022-23/player_filtered_stats23.csv')

player_stats22 = player_stats22.drop(columns=['PLAYER_ID', 'PLAYER_NAME', 'TEAM_ID'])
player_stats23 = player_stats23.drop(columns=['PLAYER_ID', 'PLAYER_NAME', 'TEAM_ID'])

pd.set_option('display.max_columns', None)

corr_matrix22 = player_stats22.corr()
#corr_matrix23 = player_stats23.corr()

plt.figure(figsize=(12, 8))  # You can adjust the size as needed

sns.heatmap(corr_matrix22, annot=True, fmt=".2f", cmap='coolwarm', square=True, annot_kws={"size": 6})

plt.title('Correlation Matrix')
#plt.savefig('/Users/zachcarlson/Documents/NBA Project/2022-23/heatmap23.png', dpi=300, bbox_inches='tight')
plt.show()


#print(player_stats22.describe())
#print(player_stats23.describe())

