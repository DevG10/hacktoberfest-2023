# first of all install all the necessary libraries.
#Example:
#pip install requests beautifulsoup4

#CODE:

import requests
from bs4 import BeautifulSoup

# Function to scrape quotes from http://quotes.toscrape.com
def scrape_quotes():
    # Send a GET request to the website
    response = requests.get("http://quotes.toscrape.com")
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Extract and print quotes and authors
    for quote in soup.find_all("span", class_="text"):
        text = quote.text
        author = quote.find_next("small", class_="author").text
        print(f'"{text}" - {author}')

# Call the function to scrape quotes
if __name__ == "__main__":
    scrape_quotes()
