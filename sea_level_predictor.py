import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df =  pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', s=10)

    # Create first line of best fit
    slope_all, intercept_all, _, _, _ = linregress(
        df['Year'], df['CSIRO Adjusted Sea Level']
    )
    years_all = pd.Series(range(df['Year'].min(), 2051))
    sea_pred_all = intercept_all + slope_all * years_all
    plt.plot(years_all, sea_pred_all, color='red', label='Tendance 1880–2050')

    # Create second line of best fit
    df_2000 = df[df['Year'] >= 2000]
    slope_2000, intercept_2000, _, _, _ = linregress(
        df_2000['Year'], df_2000['CSIRO Adjusted Sea Level']
    )
    years_2000 = pd.Series(range(2000, 2051))
    sea_pred_2000 = intercept_2000 + slope_2000 * years_2000
    plt.plot(years_2000, sea_pred_2000, color='green', label='Tendance 2000–2050')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend(loc='upper left')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()