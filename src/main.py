from classes.stock_data_retriever import StockDataRetriever
from config.config import API_KEY as key
from config.config import API_SECRET as secret
from classes.grapher import Grapher

def main():

    sdr = StockDataRetriever(api_key=key, api_secret=secret)
    g = Grapher(sdr.get_dataframe("AAPL"))
    #g.graph()
    
    #StockDataRetrieverTests
    #print(sdr.get_dataframe("AAPL")) #✔
    #print(sdr.get_latest_price("AAPL")) #✔


if __name__ == "__main__":
    main()