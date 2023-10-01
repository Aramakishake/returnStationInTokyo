import pandas as pd
import numpy.random as ran

# CSV読み込み
station = pd.read_csv('station20230907free.csv')
# 東京の駅リストを取得
station_tokyo = station[(station["pref_cd"] == 13)]
# 東京の駅リストから駅数を取得
num_station_tokyo = len(station_tokyo.index)
# ランダムなindexを取得
idx1_station_tokyo = ran.randint(num_station_tokyo)
idx2_station_tokyo = ran.randint(num_station_tokyo)
# ランダムなindexから東京の駅を抽出しprint
print("お前が行く駅は")
print("・" + station_tokyo.iloc[idx1_station_tokyo, 2])
print("もしくは")
print("・" + station_tokyo.iloc[idx2_station_tokyo, 2])
print("だ")
