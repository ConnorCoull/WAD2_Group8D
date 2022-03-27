import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','jot_project.settings')
import django
django.setup()
from jot.models import Book, Review, Category
from django.contrib.auth.models import User

def populate():
       

    # The population script takes the information in the form of a list of dictionaries.
    # This allows us to easily loop through and get the values we need and pass them to our add model functions.

    # We had our own user and admin classes at one point but this was scrapped because it is much more useful
    # to use the built in user model

    
    User.objects.all().delete
    Review.objects.all().delete
    Book.objects.all().delete




    test_users = [
       
        {'username': 'OnionGuy34672', 'password':'password','email' : 'OnionGuy34672@gmail.com'},
        {'username': 'coolAsACucumber', 'password':'password', 'email' : 'coolAsACucumber@gmail.com'},
        {'username': 'DrPepperLover', 'password':'password', 'email' : 'DrPepperLover@gmail.com'},
        {'username': 'pomeranianWriter', 'password': 'password','email' : 'pomeranian86345writer@gmail.com'},   
        {'username': 'Geezer5623', 'password': 'password','email' : 'geezerinnit@gmail.com'} ,
        {'username': 'readTheMostBooksEver', 'password': 'password','email' : 'bookEnthusiast@gmail.com'}, 
        {'username': 'crewEarly', 'password':'password', 'email': 'crewmate@gmail.com'},
        {'username': 'rastaaaangel94837', 'password':'password', 'email': 'rasta@gmail.com'},
        {'username': 'RachelJohnson', 'password':'password', 'email': 'RachelJohnson838737@gmail.com'},
        {'username': 'winstonSmith', 'password':'password', 'email': 'Winston46356Smith@gmail.com'},
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
        Camus suggests, in perceiving that an eternity of futile labor is a hideous punishment.''', 'uploaded_by':'crewEarly',
         'book_date_published':'1945-01-01', 'book_average_rating' : 4, 'book_file_path': 'jot/media', 'book_category': 'Philosophy', 'book_views': 12},

        {'book_title':'Cthulhu loses his Ipad', 'author':'pomeranianWriter', 'book_description':'''Cthulhu - dreaded, 
        colossal beast of the sea, takes a break from terrorising lone fishermeno look for his ipad, which he swears he put 
        somewhere near the indian ocean.''', 'uploaded_by':'pomeranianWriter','book_date_published':'2009-01-01', 
        'book_average_rating' : 2, 'book_file_path': 'jot/media', 'book_category': 'Fiction', 'book_views': 82},

        {'book_title': 'No Mean City', 'author':'Kingsley Long & Alexander McArthur', 'book_description' : 
        '''It is an account of life in the Gorbals, a run-down slum district of Glasgow with the hard men and the razor gangs.''',
        'uploaded_by': 'RachelJohnson','book_date_published' : '1935-01-01', 'book_average_rating' : 4,'book_file_path' : 'jot/media', 
        'book_category':'Fiction','book_views' : 9 },

        {'book_title': '''Jamie's 30-Minute Meals''', 'author':'Jamie Oliver', 'book_description' : '''Recipes you can make in 30 minutes!''',
        'uploaded_by': 'winstonSmith','book_date_published' : '2010-08-29', 'book_average_rating' : 3,'book_file_path' : 'jot/media', 
        'book_category':'Lifestyle','book_views' : 24 },

        {'book_title': '''Harry Potter and the Philosopher's Stone''', 'author':'J. K. Rowling', 'book_description' : 
        '''The first book in the critically acclaimed Harry Potter book series!''',
        'uploaded_by': 'DrPepperLover','book_date_published' : '1472-01-01', 'book_average_rating' : 5,'book_file_path' : 'jot/media', 
        'book_category':'Kids','book_views' : 1683 },

        {'book_title': 'In Defence of Witches', 'author':'Mona Chollet', 'book_description' : ''''What remains of the witch hunts? A stubborn misogyny,
         which still tints the way our societies look at single women, childless women, aging women, or quite simply, free women . . .''',
        'uploaded_by': 'coolAsACucumber','book_date_published' : '2022-06-01', 'book_average_rating' : 3,'book_file_path' : 'jot/media', 
        'book_category':'Non-fiction','book_views' : 396 },

        {'book_title': 'Das Kapital', 'author':'Karl Marx', 'book_description' : '''Foundational theoretical text in politics''',
        'uploaded_by': 'winstonSmith','book_date_published' : '1867-01-01', 'book_average_rating' : 3,'book_file_path' : 'jot/media', 
        'book_category':'Political','book_views' : 805 },
        ]   


    test_reviews = [
        {'review_book': 'The Adventures of Bill and Dandy', 'reviewer':'coolAsACucumber', 'review_rating' : 3
        , 'review_date_written': '2021-12-21', 'review_content': 'Decently written but rather bland at points'},

        {'review_book': 'Inferno', 'reviewer':'OnionGuy34672', 'review_rating' : 5
        , 'review_date_written': '2022-12-22', 'review_content': 'An absolute classic'},

        {'review_book':'The Myth Of Sisyphus', 'reviewer':'DrPepperLover', 'review_rating':4,
        'review_date_written': '2021-12-21', 'review_content': '''I found this quite obscure and difficult to read but after a few attempts,
        I now believe this is the greatest book ever written and everyone must read this as soon as they can.'''},

        {'review_book': 'The Adventures of Bill and Dandy', 'reviewer':'pomeranianWriter', 'review_rating' : 1
        , 'review_date_written': '2021-12-21', 'review_content': 'Terrible! Bill and Dandy!! what silly names!'},

        {'review_book': 'The Myth Of Sisyphus', 'reviewer':'OnionGuy34672', 'review_rating' : 2
        , 'review_date_written': '2022-12-22', 'review_content': 'Depressing, this guy needs to brighten up.'},

        {'review_book': 'Cthulhu loses his Ipad', 'reviewer':'readTheMostBooksEver', 'review_rating' : 1
        , 'review_date_written': '2022-12-22', 'review_content': '''This story is a disgrace to the amazing beast cthulhu, in what world would 
        Cthulhu ever own an Ipad? Never mind lose it!! As lovecraft's biggest fan EVER I think this book is just plain dumb.'''},
        
        {'review_book': '''Jamie's 30-Minute Meals''', 'reviewer':'crewEarly', 'review_rating' : 5
        , 'review_date_written': '2021-12-21', 'review_content': 'My family love the meals I make with this. Thank you Jamie!'},

        {'review_book': '''Harry Potter and the Philosopher's Stone''', 'reviewer':'coolAsACucumber', 'review_rating' : 3
        , 'review_date_written': '2021-12-21', 'review_content': 'My youngest read this and loved it!'},

        {'review_book': 'No Mean City', 'reviewer':'Geezer5623', 'review_rating' : 4
        , 'review_date_written': '2021-12-21', 'review_content': '''As a Glaswegian myself I found this book a great read!
        A must read if you're from Glasgow.'''},

        {'review_book': 'Das Kapital', 'reviewer':'rastaaaangel94837', 'review_rating' : 3
        , 'review_date_written': '2021-12-21', 'review_content': 'An eye-opening read, however verbose'},



        ]


    # The for loops loop through the dictionaires and pass the values as arguments to the
    # appropriate functions

    for u in test_users:
        add_user(u['username'], u['password'],u['email'])


    # This might look a bit odd so I'll give an explanation.
    # The counter is set to zero at the beginning, this variable tells us which index (dictionary)
    # we are at in the loop.
    # We first loop through the dictionaires in the list.
    # Then we loop through the key value pairs in a given dictionary.
    # This is when our counter comes into use.
    # This allows us to access each dictionary seperately.
    # We use a if statement to find the category of the dictionary and add the category.
    # We then fill in the values and increment the counter so that next time it loops 
    # round it will take the next dictionary.
    counter = 0
    for i in test_books:
        for key,value in test_books[counter].items():
            if key == 'book_category':
                c = add_category(value)
                add_book(c, i['book_title'], i['author'], i['book_description'], i['uploaded_by'], i['book_date_published'], 
                i['book_average_rating'], i['book_file_path'], i['book_category'], i['book_views'])
        counter +=1

    for c in Category.objects.all():
        for b in Book.objects.filter(book_category=c):
            print(f'-{c}: {b}')

    for r in test_reviews:
        add_review( r['review_book'], r['reviewer'], r['review_rating'], r['review_date_written'], r['review_content'])

    # Here are the functions used to add the information to the database.
    # Note that when other objects are creating within one of these functions
    # This is for the foreign keys.

def add_user(username, password, email):
    u = User.objects.get_or_create(username=username)[0]
    u.password=password
    u.email=email
    u.save()
    return u

def add_book(cat, book_title, author, book_description, uploaded_by, book_date_published, book_average_rating, book_file_path, book_category, book_views=0):
    b = Book.objects.get_or_create(book_title=book_title)[0]
    c = Category.objects.get_or_create(category_name=cat)[0]
    c2 = Category.objects.get_or_create(category_name=book_category)[0]
    u = User.objects.get_or_create(username=uploaded_by)[0]
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
    b = Book.objects.get_or_create(book_title=review_book)[0]
    r = Review.objects.create(review_book=b)
    u = User.objects.get_or_create(username=reviewer)[0]
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
    
    print(User.objects.all())
    print(Book.objects.all())
    print(Review.objects.all())