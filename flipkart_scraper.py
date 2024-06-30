import requests
from bs4 import BeautifulSoup


def scrape_flipkart(query):
    url = f"https://www.flipkart.com/search?q={query}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    products = []
    for item in soup.find_all('a', {'class': 'CGtC98'}):
        name = item.find('div', {'class': 'KzDlHZ'})
        price = item.find('div', {'class': 'Nx9bqj _4b5DiR'})
        rating = item.find('div', {'class': 'XQDdHH'})

        if name and price:
            product_info = {
                'name': name.text,
                'price': price.text,
                'rating': rating.text if rating else 'No rating',
                'url': "https://www.flipkart.com" + item['href']
            }
            products.append(product_info)

    return products
