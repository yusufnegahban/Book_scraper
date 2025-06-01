📚 Book Scraper Flask App
This app scrapes book info from Books to Scrape, saves it in a PostgreSQL database, and shows it in a simple Flask web app.

🚀 Features
Scrapes book title, author, ISBN, price, availability, publish date

-Handles multiple pages (pagination)

-Stores data using SQLAlchemy with PostgreSQL

-Web interface with search and pagination

-REST API to get book data in JSON

-Basic unit tests for scraping and web routes

🛠 How to Run
پ
pip install -r requirements.txt
python scraper.py    # Scrape and save books
python app.py        # Run the web app
Then open: http://localhost:5000 to explore the books!

🧠 What We Learned
-Web scraping with requests & BeautifulSoup

Database modeling with SQLAlchemy

Building web apps with Flask

Implementing search, pagination, and REST API

Writing tests and using Git for version control

Ready to explore or improve? Enjoy the code! 
