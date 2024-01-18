import pandas as pd
import matplotlib.pyplot as plt
#from config.config import API_SECRET as secret

# Assuming df is your DataFrame
# Resetting index to bring 'symbol' and 'timestamp' back as columns

class Grapher:

    def __init__(self, stock_df):
        self.df = stock_df

    def graph(self):

        df_reset = self.df.reset_index()

        # Plotting the DataFrame
        plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
        for symbol, data in df_reset.groupby('symbol'):
            plt.plot(data['timestamp'], data['close'], label=symbol)

        # Adding labels and title
        plt.xlabel('Timestamp')
        plt.ylabel('Close Price')
        plt.title('Stock Prices Over Time')

        # Adding legend
        plt.legend()

        # Rotating x-axis labels for better readability
        plt.xticks(rotation=70)

        # Display the plot
        plt.tight_layout()  # Adjust layout to prevent clipping of labels
        plt.show()

