import pandas as pd
import numpy as np
from config import indices_name
from document_CURD import *
from indices_CURD import *
from main import createTrade

def UpdateDataFile():
	df = pd.read_csv("MOCK_DATA.csv")

	df["trade_date_time"] = pd.to_datetime(df['trade_date_time'] + ' ' + df['trade_date_time_2'])

	df.drop(['trade_date_time'], axis = 1)

	df["buySellIndicator"] = df["buySellIndicator"].map({True:"BUY",False:"SELL"})
	df['quantity'] = np.random.randint(1, 6000, df.shape[0])
	df['trade_id'] = df[['trade_date_time', 'buySellIndicator','quantity',"counterparty","instrument_name"]].sum(axis=1).map(hash)
	
	df = df.sort_values(by = 'trade_date_time')
	df.to_csv("MOCK_DATA_2.csv")

def CSV_to_dict(name):
	df = pd.read_csv(name)
	ans = df.to_dict(orient='records')
	return ans

def stringToJSON(s):
    return json.loads(s)

def updateDB():
	UpdateDataFile()
	data = CSV_to_dict("MOCK_DATA_2.csv")
	resp = stringToJSON(GetAllDocument(indices_name))	

	if "error" not in resp:
		DeleteIndices(indices_name)
	CreateIndices(indices_name)

	for i in data:
		print(InsertIntoIndices(indices_name,i))

def resetDatabase():
	try:
		UpdateDataFile()
		updateDB()
		return True
	except:
		return False

if __name__ == '__main__':
	print("!!!!!!!!!!!!!!!!!!!!!!!!!!")
	x = int(input("Do You Really want to update Yes(1) or  No(0) : "))
	if x==1:
		UpdateDataFile()
		updateDB()
		print("Your work is done")
	else:
		print("Not Changed")




