import pandas as pd
import numpy as np
from config import indices_name
from document_CURD import *
from indices_CURD import *
from main import createTrade

# it will help to fix and fill mock data into "MOCK.csv"
def UpdateDataFile():
	df = pd.read_csv("MOCK_DATA.csv")

	df["trade_date_time"] = pd.to_datetime(df['trade_date_time'] + ' ' + df['trade_date_time_2'])

	df.drop(['trade_date_time'], axis = 1)

	df["buySellIndicator"] = df["buySellIndicator"].map({True:"BUY",False:"SELL"})
	df['quantity'] = np.random.randint(1, 6000, df.shape[0])
	df['trade_id'] = df[['trade_date_time', 'buySellIndicator','quantity',"counterparty","instrument_name"]].sum(axis=1).map(hash)
	
	df = df.sort_values(by = 'trade_date_time')
	df.to_csv("MOCK_DATA_2.csv")

# convert csv to dict
def CSV_to_dict(name):
	df = pd.read_csv(name)
	ans = df.to_dict(orient='records')
	return ans


def stringToJSON(s):
    return json.loads(s)

# it will itrate to every row and that will push all valid rows into database
def updateDB():
	UpdateDataFile()
	data = CSV_to_dict("MOCK_DATA_2.csv")
	resp = stringToJSON(GetAllDocument(indices_name))	

	if "error" not in resp:
		DeleteIndices(indices_name)
	CreateIndices(indices_name)

	for i in data:
		print(InsertIntoIndices(indices_name,i))

# function used to reset database
def resetDatabase():
	try:
		UpdateDataFile()
		updateDB()
		return True
	except:
		return False




