import requests
import pprint


# Prompt use for country and save as string variable named "country"
country_search_pattern = input("What country would like to search for? ")

# Make the GET request to the API endpoint and store response to variable named "response"
response = requests.get(f'https://restcountries.com/v3.1/name/{country_search_pattern}')

# Extract the JSON (dictionaries OR list of dictionaries) from the response and store as variable named "countries_data"
countries_data = response.json()

# Now that we know our response is a list, lets see how many countries matched our search
print(f"Found {len(countries_data)} countries")
# A search for "china" returns 4 matches
# This means we have a list with 4 elements
# Each element in the list is a dictionary containing info about the country

# Because our response is a list, we should iterate through the list with a loop
for country in countries_data:
  # Lets print something about each country, how about the common name
  print(country['name']['common'])