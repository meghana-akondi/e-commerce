# Web Scraping Marketplace Search

This repository contains a Flask web application for searching products across multiple marketplaces using web scraping techniques. The application allows users to enter a search query, retrieves results from Flipkart and eBay, and displays them on a single page for comparison.

## Features

- **Search**: Users can enter a query to search for products.
- **Flipkart Scraper**: Scrapes product data from Flipkart search results.
- **eBay Scraper**: Scrapes product data from eBay search results.
- **Comparison**: Displays results from both platforms for easy comparison.

## Technologies Used

- **Python**: Backend programming language.
- **Flask**: Web framework for building the application.
- **Beautiful Soup**: Python library for web scraping.
- **Requests**: HTTP library for making web requests.
- **HTML/CSS**: Frontend templates and styling.

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/Madhavv69/WebScraping-Marketplace-Search.git
    ```

2. Install dependencies:

    ```bash
    cd WebScraping-Marketplace-Search
    pip install -r requirements.txt
    ```

3. Run the application:

    ```bash
    python app.py
    ```

4. Open a web browser and go to `http://localhost:5000` to use the application.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Commit your changes (`git commit -am 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature-name`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
