from classes.stock_data_retriever import StockDataRetriever
from config.config import API_KEY as key
from config.config import API_SECRET as secret
from classes.grapher import Grapher

def main():

    sdr = StockDataRetriever(api_key=key, api_secret=secret)
    

    #StockDataRetriever tests
    df = sdr.get_dataframe(symbol="AAPL", months_back=3)    
    #print(sdr.get_dataframe(symbol="SPY", months_back=6)) #✔
    #print(sdr.get_latest_price("AAPL")) #✔

    #Grapher tests
    g = Grapher(df)
    #g.graph_stock_close()
    g.graph() #✔
    

if __name__ == "__main__":
    main()