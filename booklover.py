#Task 1

import pandas as pd

class BookLover:
    def __init__(self, name, email, fav_genre, num_books=0, book_list=None):
        self.name = name                  # Name of the person
        self.email = email                # Unique email identifier
        self.fav_genre = fav_genre        # Favorite book genre
        self.num_books = num_books        # Number of books read
        self.book_list = book_list if book_list is not None else pd.DataFrame({'book_name': [], 'book_rating': []})

    # Method 1: Add a book if it doesn't already exist in book_list
    def add_book(self, book_name, rating):
        if self.book_list['book_name'].eq(book_name).any():
            print(f"{book_name} is already in the book list.")
        else:
            new_book = pd.DataFrame({'book_name': [book_name], 'book_rating': [rating]})
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books += 1

    # Method 2: Check if the person has read a particular book
    def has_read(self, book_name):
        return (self.book_list['book_name'] == book_name).any()

    # Method 3: Return the total number of books read
    def num_books_read(self):
        return self.num_books

    # Method 4: Return a filtered list of favorite books with ratings > 3
    def fav_books(self):
        return self.book_list[self.book_list['book_rating'] > 3]

# Testing the class
if __name__ == '__main__':
    test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
    test_object.add_book("War of the Worlds", 4)
    test_object.add_book("1984", 5)
    test_object.add_book("War of the Worlds", 4)  # Should not add again
    print("Books read:", test_object.num_books_read())
    print("Has read '1984':", test_object.has_read("1984"))
    print("Favorite books:\n", test_object.fav_books())


    
