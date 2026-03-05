from recommender import recommend_restaurants
import pandas as pd

df = pd.read_csv("Dataset.csv")

pd.set_option('display.max_columns', None)

df_new = df[['Restaurant Name', 'City', 'Cuisines',
                  'Average Cost for two', 'Price range',
                  'Aggregate rating', 'Votes']].copy()

# User input
city = input("Enter city: ").lower()
cuisine = input("Enter cuisine: ").lower()
price = int(input("Enter price range (1-4): "))

result = recommend_restaurants(df_new, df, city, cuisine, price)
print(result)