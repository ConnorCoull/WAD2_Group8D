import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','jot_project.settings')
import django
django.setup()
from jot.models import Users, Book, Review, Admin, UserProfile, Category
import uuid

def populate():
        #if usertype is true the user in an author
        #if usertype if false the user is a reader

    test_users = [
       
        {'username': 'OnionGuy34672', 'user_password':'password', 'user_type' : True, 'user_email' : 'OnionGuy34672@gmail.com'},
        {'username': 'coolAsACucumber', 'user_password':'password', 'user_type' : True, 'user_email' : 'coolAsACucumber@gmail.com'},
        {'username': 'DrPepperLover', 'user_password':'password', 'user_type': False, 'user_email' : 'DrPepperLover@gmail.com'},
        {'username': 'Hamaguchi', 'user_password': 'password', 'user_type': True, 'user_email' : 'RHamaguchi@gmail.com'}        
        ]

    test_books = [
        {'book_title': 'The Adventures of Bill and Dandy', 'author':'OnionGuy34672', 'book_description' : 'A book I wrote about 2 guys, bill and dandy',
        'uploaded_by': 'OnionGuy34672' ,'book_date_published' : '2022-12-03', 'book_average_rating' : 1.2, 'book_file_path' : 'jot/media', 
        'book_category':'Fiction', 'book_views' : 5,
        },
    
        {'book_title': 'Inferno', 'author':'Dante Alighieri', 'book_description' : '''The first part of Dante's poem Divine comedy''',
        'uploaded_by': 'coolAsACucumber','book_date_published' : '1472-01-01', 'book_average_rating' : 5,'book_file_path' : 'jot/media', 
        'book_category':'Historical','book_views' : 81 },
        
        #The third book below was added for one of Tianhao's unit tests
        {'book_title': 'Inferno2', 'author':'Dante Alighieri', 'book_description' : '''The first part of Dante's poem Divine comedy''',
        'uploaded_by': 'coolAsACucumber','book_date_published' : '1472-01-01', 'book_average_rating' : 5,'book_file_path' : 'jot/media', 
        'book_category':'Historical','book_views' : 81 },

        {'book_title':'The Myth Of Sisyphus', 'author':'Albert Camus', 'book_description':'''According to the Greek myth, Sisyphus is condemned to roll 
        a rock up to the top of a mountain, only to have the rock roll back down to the bottom every time he reaches the top. The gods were wise, 
        Camus suggests, in perceiving that an eternity of futile labor is a hideous punishment.''', 'uploaded_by':'Hamaguchi',
         'book_date_published':'1945-01-01', 'book_average_rating' : 4, 'book_file_path': 'jot/media', 'book_category': 'Philosophy', 'book_views': 12}
        ]   


    test_reviews = [
        {'review_book': 'The Adventues of Bill and Dandy', 'reviewer':'coolAsACucumber', 'review_rating' : 3
        , 'review_date_written': '2021-12-21', 'review_content': 'Decently written but rather bland at points'},

        {'review_book': 'Inferno', 'reviewer':'OnionGuy34672', 'review_rating' : 5
        , 'review_date_written': '2022-12-22', 'review_content': 'An absolute classic'},

        {'review_book':'The Myth of Sysphus', 'reviewer':'DrPepperLover', 'review_rating':4,
        'review_date_written': '2021-12-21', 'review_content': '''I found this quite obscure and difficult to read but after a few attempts,
        I now believe this is the greatest book ever written and everyone must read this as soon as they can.'''}
        ]



    
    
    
    
    #for d in test_books:
    #    for key, value in d.items():
    #        if key == 'book_category':
    #            c = add_category(value)

    for u in test_users:
        add_user(u['username'], u['user_password'], u['user_type'], u['user_email'])

   # for b in test_books:
    #    add_book(b['book_title'], b['author'], b['book_description'], b['uploaded_by'], b['book_date_published'], 
     #   b['book_average_rating'], b['book_file_path'], b['book_category'], b['book_views'])

    counter = 0
    for i in test_books:
        for key,value in test_books[counter].items():
            if key == 'book_category':
                c = add_category(value)
                add_book(c, i['book_title'], i['author'], i['book_description'], i['uploaded_by'], i['book_date_published'], 
                i['book_average_rating'], i['book_file_path'], i['book_category'], i['book_views'])
        counter +=1
        print("This is the counter number", counter)

    for c in Category.objects.all():
        for b in Book.objects.filter(book_category=c):
            print(f'-{c}: {b}')

    #for r in test_reviews:
        #for r in d.values():
      #  add_review(r['review_id'], r['review_book'], r['reviewer'], r['review_rating'], r['review_date_written'], r['review_content'])
    


def add_user(username, user_password, user_type, user_email):
    u = Users.objects.get_or_create(username=username)[0]
    u.user_password=user_password
    u.user_type=user_type
    u.user_email=user_email
    u.save()
    return u

def add_book(cat, book_title, author, book_description, uploaded_by, book_date_published, book_average_rating, book_file_path, book_category, book_views=0):
    test = uuid.uuid4()
    b = Book.objects.get_or_create(bookID = test)
    b = Book.objects.get_or_create(book_title=book_title)[0]
    c = Category.objects.get_or_create(category_name=cat)[0]
    c2 = Category.objects.get_or_create(category_name=book_category)[0]
    u = Users.objects.get_or_create(username=uploaded_by)[0]
    b.cat = c

    b.author=author
    b.book_description=book_description
    b.uploaded_by = u 
    b.book_date_published=book_date_published
    b.book_average_rating=book_average_rating
    b.book_file_path=book_file_path
    b.book_category=c2
    b.book_views=book_views

    b.save()
    return b

def add_review(review_book, reviewer, review_rating, review_date_written, review_content):
    r = Review.objects.get_or_create(review_book=review_book)[0]
    b = Book.objects.get_or_create(book_title=review_book)
    u = Users.objects.get_or_create(username=reviewer)
    print(r)
    print(b)
    print(u)
    r.review_book = b
    r.reviewer = u
    r.review_rating=review_rating
    r.review_date_written=review_date_written
    r.review_content=review_content
    r.save()
    return r

def add_category(category_name):
    c = Category.objects.get_or_create(category_name=category_name)[0]
    c.save()
    return c




if __name__ == "__main__":
    print("Populating script...")
    populate()