import pandas as pd

# Recommender function to filter and sort restaurants based on user input and return top recommendations
def recommend_restaurants(df_new, df, city, cuisine, price, top_n=5):
    # Input cleaning
    city = city.lower()
    cuisine = cuisine.lower()

    # Ensure lowercase matching
    df_new['City'] = df_new['City'].str.lower()
    df_new['Cuisines'] = df_new['Cuisines'].str.lower()

    # Filtering
    filtered = df_new[
        (df_new['City'] == city) &
        (df_new['Cuisines'].str.contains(cuisine, na=False)) &
        (df_new['Price range'] == price)
    ]

    # Sort by rating and votes
    filtered = filtered.sort_values(
        by=['Aggregate rating', 'Votes'],
        ascending=False
    ).head(top_n)

    # Get full details from original dataset
    result = df[df['Restaurant Name'].isin(filtered['Restaurant Name'])]

    return result[['Restaurant Name', 'City', 'Cuisines',
                   'Average Cost for two', 'Price range',
                   'Aggregate rating', 'Votes', 'Address']]