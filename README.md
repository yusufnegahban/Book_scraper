📚 Book Scraper & Flask Web App
Hey there!we built a cool app that scrapes book info from a website, stores it in a database, and shows it on a simple web page.
It’s like a mini online bookstore! 😍

🚀 What We Did
1️⃣ Data Scraping
Used Python with requests and BeautifulSoup to grab book info from books.toscrape.com:

Book title
Author (improved later)
Price
Availability
Publish date
ISBN
Handled pagination to scrape all pages one by one 📄➡️📄➡️📄


2️⃣ Data Storage
Used PostgreSQL to keep the data safe and organized

Created a Book model with SQLAlchemy to store book details in tables


3️⃣ Flask Web App
Built a simple web app to display books in a neat table

Added search to find books by title or author 🔎

Added pagination so only 10 books show per page

Made a detail page to show full info of each book 📖


4️⃣ REST API
Created a REST API that serves book data in JSON format

You can use the API to get data for other apps or future projects


5️⃣ Testing & Code Quality
Wrote simple tests to make sure main page and API work fine ✅

Kept code clean, organized, and easy to maintain


6️⃣ Git & Version Control
Used Git to track project changes
Made clear and descriptive commits for every step
Created branches and pull requests like pros


🛠️ How to Run
Install packages:

```pip install -r requirements.txt```


Setup PostgreSQL database books_db

Run model script to create tables

Run scraper to fill database:

nginx
Copy
Edit
python scraper.py
Run Flask app:

nginx
Copy
Edit
python app.py
Open your browser:

arduino
Copy
Edit
http://localhost:5000
Enjoy browsing books! 📚✨

🧠 What We Learned
How to scrape data from websites like a boss

Use ORM (SQLAlchemy) for smooth database handling

Build dynamic web pages with Flask

Add search and pagination for better user experience

Create a REST API for flexible data access

Write tests and manage projects professionally with Git


