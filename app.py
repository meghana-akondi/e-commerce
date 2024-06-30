from flask import Flask, render_template, request, redirect
from scrapers.flipkart_scraper import scrape_flipkart
from scrapers.ebay_scraper import scrape_ebay  # Import the eBay scraper function

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form['query']
        flipkart_results = scrape_flipkart(query)
        ebay_results = scrape_ebay(query)  # Get eBay results
        return render_template('index.html', flipkart_results=flipkart_results, ebay_results=ebay_results)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
