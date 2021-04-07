import pandas as pd

columns = ['City_ID', 'City', 'Cloudiness', 'Country', 'Data', 'Humidity', 'Lat', 'Lng', 'Max Temp', 'Wind Speed']
cities_df = pd.read_csv('Resources/cities.csv', names=columns,index_col='City_ID' )

# Use the .to_html() to get your table in html
print(cities_df.to_html())

