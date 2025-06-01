# Book_scraper
Book scraping and display app with Flask

# Book Scraper Flask App 📚

This app scrapes book data from [Books to Scrape](http://books.toscrape.com/), stores it in a PostgreSQL database, and displays it via a Flask web app.

## 🚀 Features

- Scrape title, author, ISBN, price, availability
- Store in PostgreSQL using SQLAlchemy
- Web interface with search + pagination
- REST API to get book data (JSON)
- Unit tests with pytest

## 🛠 How to Run

```bash
git clone <your-repo-url>
cd project-folder
pip install -r requirements.txt
python scraper.py  # Scrapes the books
python app.py      # Starts the Flask web app

