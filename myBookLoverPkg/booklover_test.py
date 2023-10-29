from bookLover import BookLover
import unittest

class BookLoverTestSuite(unittest.TestCase):
    
    
    def test_1_add_book(self):
        print('test')
        # add a book and test if it is in `book_list`.
        test_1 = BookLover("angela", "me@uva.com", "romance")
        test_1.add_book("Jane Eyre", 4)
        self.assertTrue('Jane Eyre' in test_1.book_list['book_name'].values)

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        test_2 =  BookLover("angela", "me@uva.com", "romance")
        test_2.add_book("Jane Eyre", 4)
        test_2.add_book("Jane Eyre", 4)
        count = test_2.book_list['book_name'].value_counts()['Jane Eyre']
        self.assertEqual(count, 1)

    def test_3_has_read(self):
        # pass a book in the list and test if the answer is `True`.
        test_3 =  BookLover("angela", "me@uva.com", "romance")
        test_3.add_book("Jane Eyre", 4)
        is_in_list = test_3.has_read('Jane Eyre')
        self.assertTrue(is_in_list)

    def test_4_has_read(self):
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        test_4 =  BookLover("angela", "me@uva.com", "romance")
        test_4.add_book("Jane Eyre", 4)
        is_in_list = test_4.has_read('Fight Club')
        self.assertFalse(is_in_list)
        
    def test_5_num_books_read(self):
        # add some books to the list, and test num_books matches expected.
        test_5 =  BookLover("angela", "me@uva.com", "romance")
        test_5.add_book("Jane Eyre", 4)
        test_5.add_book("Fight club", 2)
        self.assertEqual(self.test_5.num_books_read(), 2)
        
    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating > 3
        test_6 =  BookLover("angela", "me@uva.com", "romance")
        test_6.add_book("Jane Eyre", 4)
        test_6.add_book("Fight club", 2)
        test_6.add_book("The Divine Comedy", 5)
        new = test_6.fav_books()
        self.assertTrue(is_greater_than_3 = (new['book_rating'] > 3).all())
    
if __name__ == '__main__':
    unittest.main(verbosity=3)
