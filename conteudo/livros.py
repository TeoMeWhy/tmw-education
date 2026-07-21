import streamlit as st
import pandas as pd


from books.books import BookClient, Book

import os
import dotenv
dotenv.load_dotenv()

BOOK_CLIENT_URI = os.getenv("BOOK_CLIENT_URI")

# @st.cache_data(ttl=60)  # 10 minutes in seconds
def get_livros():
    book_client = BookClient(base_url=BOOK_CLIENT_URI)
    books = book_client.get_books()
    df = pd.DataFrame([book.to_dict() for book in books])
    return df

def livros():
    df = get_livros()
    
    themes = df['theme'].unique()
    themes.sort()
    for t in themes:
        st.markdown(f"#### {t}")
        theme_books = df[df['theme'] == t]
        for _, book in theme_books.iterrows():
            text = f"- [{book['title']}]({book['link']}) - {book['author']}"
            
            if 1-book['price_with_discount']/book['price'] > 0.2:  # More than 10% discount
                text += f" :star2: **{int((1-book['price_with_discount']/book['price'])*100)}% OFF**"
            
            st.markdown(text)
