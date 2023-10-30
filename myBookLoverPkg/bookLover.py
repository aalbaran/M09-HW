import pandas as pd
import numpy as np

class BookLover:
    #attributes
    name = None #The name of the person (type:string)
    email = None #The person’s email, serving as a unique identifier (type:string)
    fav_genre = None #The person’s favorite book genre (type:string)
    num_books = 0 #Keeps track of the number of books the person has read (type:int)
    book_list = pd.DataFrame({'book_name': [], 'book_rating': []}) #a dataframe 
    
    # constructor
    def __init__(self, name, email, fav_genre):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        #self.num_books = num_books
        #self.book_list = book_list
        
    # enroll in a course
    def add_book(self, book_name, book_rating): 
        #if(any(self.book_list[book_name] != book_name)):
        if book_name not in self.book_list['book_name'].values:
           new_book = pd.DataFrame({
               'book_name': [book_name],
               'book_rating': [book_rating]
            })
        self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
        
    def num_books_read(self):
        self.num_books = self.book_list.shape[0]
        return self.num_books
    
    def has_read(self, book_name):
        return book_name in self.book_list['book_name'].values
    
    def fav_books(self):
        return self.book_list[self.book_list['book_rating']>3]

if __name__ == '__main__':
    test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
    test_object.add_book("War of the Worlds", 4)
    test_object.add_book("The Divine Comedy", 5)
    test_object.add_book("Fight Club", 3)
    test_object.num_books_read()
    test_object.fav_books()
 
