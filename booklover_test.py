#Task 2

import unittest
from booklover import BookLover
import pandas as pd

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # Create a BookLover instance and add a book
        book_lover = BookLover("Tom", "tom@gmail.com", "fiction")
        book_lover.add_book("Hunger Games", 5)
        
        # Test if the book was added to book_list
        self.assertTrue("Hunger Games" in book_lover.book_list['book_name'].values)
    
    def test_2_add_book_twice(self):
        # Create a BookLover instance and add the same book twice
        book_lover = BookLover("Tom", "tom@gmail.com", "fiction")
        book_lover.add_book("Hunger Games", 5)
        book_lover.add_book("Hunger Games", 5)  # Attempt to add the same book again
        
        # Test that the book is only in book_list once
        self.assertEqual(book_lover.book_list['book_name'].value_counts().get("Hunger Games", 0), 1)
                
    def test_3_has_read(self): 
        # Create a BookLover instance and add a book
        book_lover = BookLover("Tom", "tom@gmail.com", "fiction")
        book_lover.add_book("Hunger Games", 5)
        
        # Test if has_read returns True for the book
        self.assertTrue(book_lover.has_read("Hunger Games"))
        
    def test_4_has_not_read(self): 
        # Create a BookLover instance without adding any books
        book_lover = BookLover("Tom", "tom@gmail.com", "fiction")
        
        # Test if has_read returns False for a book not in the list
        self.assertFalse(book_lover.has_read("The Great Gatsby"))
        
    def test_5_num_books_read(self): 
        # Create a BookLover instance and add books
        book_lover = BookLover("Tom", "tom@gmail.com", "fiction")
        book_lover.add_book("Hunger Games", 5)
        book_lover.add_book("To Kill a Mockingbird", 4)
        book_lover.add_book("The Catcher in the Rye", 3)
        
        # Test if num_books matches the expected count
        self.assertEqual(book_lover.num_books_read(), 3)

    def test_6_fav_books(self):
        # Create a BookLover instance and add books with various ratings
        book_lover = BookLover("Tom", "tom@gmail.com", "fiction")
        book_lover.add_book("Hunger Games", 5)
        book_lover.add_book("To Kill a Mockingbird", 4)
        book_lover.add_book("The Catcher in the Rye", 3)
        book_lover.add_book("The Great Gatsby", 2)
        
        # Get favorite books with rating > 3
        fav_books = book_lover.fav_books()
        
        # Test if the favorite books have rating > 3
        self.assertTrue(all(fav_books['book_rating'] > 3))
                
if __name__ == '__main__':
    unittest.main(verbosity=3)


#Task 3

