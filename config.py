import pandas as pd
import os



######## Load the data ########
cwd = 'Fantasy-Premier-League/data/2022-23/'
all_players_raw = pd.read_csv(os.path.join(cwd, 'players_raw.csv'))
# for position
element_type_dict = {1:"GK", 2:"DEF", 3:"MID", 4:"FWD"}
all_players_raw["Position"] = all_players_raw['element_type'].apply(lambda x: element_type_dict[x])

output_file = 'latest_gw.csv'

