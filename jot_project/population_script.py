import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','jot_project.settings')
import django
django.setup()
from jot.models import Users, Book, Review, Admin, UserProfile


def populate():

    test_users = [
       
        {'username': 'OnionGuy34672', 'user_password':'password', 'user_type' : True, 'user_email' : 'OnionGuy34672@gmail.com'},
        {'username': 'coolAsACucumber', 'user_password':'password', 'user_type' : True, 'user_email' : 'coolAsACucumber@gmail.com'}
        
    ]

    test_books = [
        {'book_title': 'The Adventures of Bill and Dandy', 'author':'OnionGuy34672', 'book_description' : 'A book I wrote about 2 guys, bill and dandy'
        ,'uploaded_by': 'OnionGuy34672','book_date_published' : '12/12/2021', 'book_average_rating' : 1.2, 'book_file_path' : 'jot/media', 'book_views' : 5},
    
        {'book_title': 'Inferno', 'author':'Dante Alighieri', 'book_description' : '''The first part of Dante's poem Divine comedy''',
        'uploaded_by': 'coolAsACucumber', 'book_date_published' : '01/01/1472', 'book_average_rating' : 5, 'book_file_path' : 'jot/media', 'book_views' : 81, }
    ]

    test_reviews = [
        {'review_book': 'The Adventues of Bill and Dandy', 'reviewer':'coolAsACucumber', 'review_rating' : 3
        , 'review_date_written': '12/03/2022', 'review_content': 'Decently written but rather bland at points'},

        {'review_book': 'Inferno', 'reviewer':'Users.OnionGuy34672', 'review_rating' : 5
        , 'review_date_written': '10/03/2022', 'review_content': 'An absolute classic'}
    ]

    admin_test = {'admin_username': 'adminguy23', 'admin_password': 'password', 'admin_email':'adminguy24@gmail.com'}

    for u in test_users:
        add_user(u['username'], u['user_password'], u['user_type'], u['user_email'])

    for b in test_books:
        add_book(b['book_title'], b['author'], b['book_description'], b['uploaded_by'], b['book_date_published'], 
        ['book_average_rating'], b['book_file_path'], b['book_views'])

    for r in test_reviews:
        #for r in d.values():
        add_review(r['review_book'], r['reviewer'], r['review_rating'], r['review_date_written'], r['review_content'])
    


def add_user(username, user_password, user_type, user_email):
    u = Users.objects.get_or_create(username=username)[0]
    u.user_password=user_password
    u.user_type=user_type
    u.user_email=user_email
    u.save()
    return u

def add_book(book_title, author, book_description, book_date_published, book_average_rating, book_file_path, uploaded_by=Users, book_views=0):
    b = Book.objects.get_or_create(book_title=book_title)[0]
    b.author=author
    b.book_description=book_description
    b.uploaded_by=uploaded_by
    b.book_date_published=book_date_published
    b.book_average_rating=book_average_rating
    b.book_file_path=book_file_path
    b.book_views=book_views
    b.save()
    return b

def add_review(review_book, reviewer, review_rating, review_date_written, review_content):
    r = Review.objects.get_or_create(review_book=review_book)[0]
    r.reviewer=reviewer
    r.review_rating=review_rating
    r.review_date_written=review_date_written
    r.review_content=review_content
    r.save()
    return r





if __name__ == "__main__":
    print("Populating script...")
    populate()