# 📚 Book Scraper & Flask Web App

cool app that scrapes book info from a website, stores it in a database, and shows it on a simple web page.  
It’s like a mini online bookstore! 😍

---

## 🚀 What We Did

### 1️⃣ Data Scraping
- Used Python with `requests` and `BeautifulSoup` to grab book info from [books.toscrape.com](http://books.toscrape.com)
- Scraped:
  - Book title
  - Author *(improved later)*
  - Price
  - Availability
  - Publish date
  - ISBN
- Handled pagination to scrape all pages one by one 📄➡️📄➡️📄

---

### 2️⃣ Data Storage
- Used **PostgreSQL** to keep the data safe and organized
- Created a `Book` model with **SQLAlchemy** to store book details in tables

---

### 3️⃣ Flask Web App
- Built a simple web app to display books in a neat table
- Added **search** to find books by title or author 🔎
- Added **pagination** (10 books per page)
- Made a **detail page** to show full info of each book 📖

---

### 4️⃣ REST API
- Created a REST API that serves book data in **JSON format**
- Now you can use the API for other apps or future projects

---

### 5️⃣ Testing & Code Quality
- Wrote simple tests using `pytest` to ensure the main page and API work ✅
- Kept code clean, organized, and easy to maintain

---

### 6️⃣ Git & Version Control
- Used **Git** to track project changes
- Made clear and descriptive commits for every step
- Created branches and pull requests like pros ✨

---

## 🛠️ How to Run

### 🔧 Install dependencies

```bash
pip install -r requirements.txt



## 🗃️ Setup PostgreSQL

Before running the scraper or the app, make sure PostgreSQL is installed and a database is created.

### 🧱 Step 1 – Install PostgreSQL
If you haven’t already installed PostgreSQL:

- [Download PostgreSQL](https://www.postgresql.org/download/)
- During setup, remember your **username**, **password**, and **port** (default is 5432)

---

### 🛠️ Step 2 – Create a database

Open a terminal or PostgreSQL shell and run:

```sql
CREATE DATABASE books_db;

