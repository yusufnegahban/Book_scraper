import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Import Flask app, db and model
from app import app, db, Book

def scrape_books():
    base_url = "http://books.toscrape.com/catalogue/"
    page_url = "page-1.html"

    while True:
        response = requests.get(base_url + page_url)
        soup = BeautifulSoup(response.text, "html.parser")

        books = soup.select("article.product_pod")

        for book in books:
            title = book.h3.a["title"]

            # Fix price encoding issue
            price_raw = book.select_one("p.price_color").text.strip()
            price_fixed = price_raw.encode('latin1').decode('utf-8')
            price = price_fixed  # Now price is clean

            availability = book.select_one("p.instock.availability").text.strip()

            # Detail page
            detail_link = urljoin(base_url, book.h3.a['href'])
            detail_res = requests.get(detail_link)
            detail_soup = BeautifulSoup(detail_res.text, "html.parser")

            table = detail_soup.select_one("table.table.table-striped")
            rows = table.find_all("tr")
            data = {row.th.text.strip(): row.td.text.strip() for row in rows}

            isbn = data.get("UPC", "")
            publish_date = data.get("Availability", "")
            author = "Unknown"  # You can improve this later

            existing = Book.query.filter_by(title=title, isbn=isbn).first()
            if not existing:
                new_book = Book(
                    title=title,
                    author=author,
                    price=price,
                    availability=availability,
                    isbn=isbn,
                    publish_date=publish_date
                )
                db.session.add(new_book)

        db.session.commit()
        print(f"✅ Page {page_url} done")

        next_button = soup.select_one("li.next > a")
        if next_button:
            page_url = next_button["href"]
        else:
            break

if __name__ == "__main__":
    with app.app_context():
        scrape_books()
