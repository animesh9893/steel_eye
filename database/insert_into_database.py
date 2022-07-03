import pandas as pd
import numpy as np


def UpdateDataFile():
	df = pd.read_csv("MOCK_DATA.csv")

	df["trade_date_time"] = pd.to_datetime(df['trade_date_time'] + ' ' + df['trade_date_time_2'])

	df.drop(['trade_date_time'], axis = 1)

	df["buySellIndicator"] = df["buySellIndicator"].map({True:"BUY",False:"SELL"})
	df['quantity'] = np.random.randint(1, 6000, df.shape[0])
	df.to_csv("MOCK_DATA_2.csv")

def CSV_to_dict(name):
	df = pd.read_csv(name)
	ans = df.to_dict(orient='records')
	return ans

# print(CSV_to_dict("MOCK_DATA_2.csv"))
# UpdateDataFile()