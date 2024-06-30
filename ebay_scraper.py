import requests
from bs4 import BeautifulSoup


def scrape_ebay(query):
    url = f"https://www.ebay.com/sch/i.html?_nkw={query}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    products = []
    for item in soup.find_all('div', {'class': 's-item__info clearfix'}):
        name = item.find('div', {'class': 's-item__title'})
        price = item.find('span', {'class': 's-item__price'})
        rating = item.find('div', {'class': 'x-star-rating'})

        if name and price:
            product_info = {
                'name': name.text.strip(),
                'price': price.text.strip(),
                'url': item.find('a', {'class': 's-item__link'}).get('href', 'No URL')
            }
            if rating:
                product_info['rating'] = rating.find('span', {'class': 'clipped'}).text.strip()
            else:
                product_info['rating'] = 'No rating'
            products.append(product_info)

    return products
