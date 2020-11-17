from pandas_datareader import data as pdr
try:
    ptt = pdr.get_data_yahoo("PTT.BK", start="2020-07-01", end="2020-07-08")
    print(ptt.tail())
    print()
except:
    print("Error:", sys.exc_info()[0])
    print("Description:", sys.exc_info()[1])
