import requests
import http

class Book:
    
    def __init__(self,id, title, author, description, genre, theme, link, price=None, price_with_discount=None):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.genre = genre
        self.theme = theme
        self.link = link
        self.price = float(price) if price is not None else 0.0
        self.price_with_discount = float(price_with_discount) if price_with_discount is not None else 0.0

    def __repr__(self):
        return f"Book(id={self.id}, title={self.title}, author={self.author}, description={self.description}, genre={self.genre}, theme={self.theme}, link={self.link}, price={self.price}, price_with_discount={self.price_with_discount})"
        
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "description": self.description,
            "genre": self.genre,
            "theme": self.theme,
            "link": self.link,
            "price": self.price,
            "price_with_discount": self.price_with_discount
        }


class BookClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_books(self):
        response = requests.get(f"{self.base_url}/books")
        if response.status_code == http.HTTPStatus.OK:
            
            data = response.json()
            
            books = []
            for book_data in data["books"]:
                book = Book(
                    id=book_data.get("id"),
                    title=book_data.get("title"),
                    author=book_data.get("author"),
                    description=book_data.get("description"),
                    genre=book_data.get("genre"),
                    theme=book_data.get("theme"),
                    link=book_data.get("link"),
                    price=book_data.get("price"),
                    price_with_discount=book_data.get("price_with_discount"),
                )
                books.append(book)
            return books
        else:
            return {"error": f"Failed to get books. Status code: {response.status_code}"}

    def get_book_by_id(self, book_id):
        response = requests.get(f"{self.base_url}/books/{book_id}")
        if response.status_code == http.HTTPStatus.OK:
            data = response.json()
            return Book(
                id=data.get("id"),
                title=data.get("title"),
                author=data.get("author"),
                description=data.get("description"),
                genre=data.get("genre"),
                theme=data.get("theme"),
                link=data.get("link"),
                price=data.get("price"),
                price_with_discount=data.get("price_with_discount"),
            )
        else:
            return {"error": f"Book with ID {book_id} not found. Status code: {response.status_code}"}

    def search_books(self, query_params):
        response = requests.get(f"{self.base_url}/books/search", params=query_params)
        if response.status_code == http.HTTPStatus.OK:
            data = response.json()
            books = []
        
            for book_data in data['books']:
                book = Book(
                    id=book_data.get("id"),
                    title=book_data.get("title"),
                    author=book_data.get("author"),
                    description=book_data.get("description"),
                    genre=book_data.get("genre"),
                    theme=book_data.get("theme"),
                    link=book_data.get("link"),
                    price=book_data.get("price"),
                    price_with_discount=book_data.get("price_with_discount"),
                )
                books.append(book)
            return books
        
        else:
            return {"error": f"Failed to search books. Status code: {response.status_code}"}

    def create_book(self, book):
        
        book_data = {
            "title": book.title,
            "author": book.author,
            "description": book.description,
            "genre": book.genre,
            "theme": book.theme,
            "link": book.link,
            "price_with_discount": book.price_with_discount,
            "price": book.price,
        }
        
        response = requests.post(f"{self.base_url}/books", json=book_data)
        if response.status_code == http.HTTPStatus.CREATED:
            return response.json()
        else:
            return {"error": f"Failed to create book. Status code: {response.status_code}"}
        
    def update_book(self, book):
        
        book_data = {
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "description": book.description,
            "genre": book.genre,
            "theme": book.theme,
            "link": book.link,
            "price_with_discount": book.price_with_discount,
            "price": book.price,
        }
        
        response = requests.put(f"{self.base_url}/books/{book.id}", json=book_data)
        
        if response.status_code == http.HTTPStatus.OK:
            return response.json()
        
        else:
            return {"error": f"Failed to update book. Status code: {response.status_code}"}