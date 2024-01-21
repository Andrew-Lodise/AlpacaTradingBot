import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#from config.config import API_SECRET as secret

# Assuming df is your DataFrame
# Resetting index to bring 'symbol' and 'timestamp' back as columns

class Grapher:

    def __init__(self, stock_df):
        self.df = stock_df

    def graph(self):

        data = self.df.reset_index()

        # Plotting the DataFrame
        plt.figure(figsize=(10, 6))  

        plt.plot(data['timestamp'], data['close'], color="blue", label="Closing Price", linewidth=5)
        plt.plot(data['timestamp'], data['MA'], color = "red", label= "5-day Moving Average", linewidth=2)

        #labels and title
        plt.xlabel('Timestamp')
        plt.ylabel('Price (USD$)')
        plt.title(f'({self.df.index[0][0]}) Stock Prices Over Time')

        # Adding legend
        plt.legend()

        # Adding grid
        plt.grid()

        # Rotating x-axis labels for better readability
        plt.xticks(rotation=90)

        # Display the plot
        plt.tight_layout()  # Adjust layout to prevent clipping of labels
        plt.show()

