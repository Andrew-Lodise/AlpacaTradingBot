import pandas as pd
import matplotlib.pyplot as plt
#from config.config import API_SECRET as secret

# Assuming df is your DataFrame
# Resetting index to bring 'symbol' and 'timestamp' back as columns

class Grapher:

    def __init__(self, stock_df):
        self.df = stock_df
        self.add_ma_col()

    
    def add_ma_col(self):
        self.df['MA'] = self.df['close'].rolling(window=5).mean()


    def graph(self):

        data = self.df.reset_index()

        # Plotting the DataFrame
        plt.figure(figsize=(10, 6))  

        plt.plot(data['timestamp'], data['close'], color="blue", label="Closing Price", linewidth=5)
        plt.plot(data['timestamp'], data['MA'], color = "red", label= "5-day Moving Average", linewidth=2)

        #labels and title
        plt.xlabel('Timestamp')
        plt.ylabel('price')
        plt.title('Stock Prices Over Time')

        # Adding legend
        plt.legend()

        # Rotating x-axis labels for better readability
        plt.xticks(rotation=70)

        # Display the plot
        plt.tight_layout()  # Adjust layout to prevent clipping of labels
        plt.show()

