from django.db import models 
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

# This is unfinished, I'll come back to it and finish it later
# Note that the rest of my comments are things I've put here so I can come and fix them later

class Users(models.Model):
    #Not sure if user gets its own model but I've made it here anyway, can always remove it
    #user_admin_deletes = models.ForeignKey(Admin, on_delete=models.CASCADE)
    username = models.CharField(max_length=32, unique=True)
    user_password = models.CharField(max_length=32)
    user_type = models.BooleanField(default=False)
    user_email = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'Users'
        verbose_name_plural = 'Users'
    

class Book(models.Model):
    #There is an uploaded_by and author. This is because a user might want to upload a book they themselves did not write
    #book_admin_deletes = models.ForeignKey(Admin, on_delete=models.CASCADE)
    book_title = models.CharField(max_length=30)
    author = models.CharField(max_length=32)
    book_description = models.CharField(max_length=250)
    book_date_published = models.DateField(auto_now=False, auto_now_add=True)
    #book_id = models.IntegerField(unique=True)
    book_average_rating = models.PositiveIntegerField(
        default = 1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    ) # The book can only be rated between 1-5, so the rating will be between these numbers
    book_file_path = models.CharField(max_length=128)
    book_views = models.IntegerField(default=0)
    uploaded_by = models.ForeignKey(Users, on_delete=models.CASCADE, null = True)

    def __str__(self):
        return self.book_title
    
    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

class Review(models.Model):
    #review_admin_deletes = models.ForeignKey(Admin, on_delete=models.CASCADE)
    review_book = models.ForeignKey(Book, on_delete=models.CASCADE, null = True)
    reviewer = models.ForeignKey(Users, on_delete=models.CASCADE, null = True)
    #review_id = models.IntegerField(unique=True)
    review_rating = models.IntegerField( 
        #Since the reviews are rated 1-5 this makes it so
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]


    )
    review_date_written = models.DateField(auto_now=False, auto_now_add=True)
    review_content = models.CharField(max_length=250)

    def __str__(self):
        return self.review_rating #maybe change this and make another variable to be the unique identifier

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

class Admin(models.Model):
    admin_username = models.CharField(max_length=32, unique=True)
    admin_password = models.CharField(max_length=32)
    admin_email= models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.admin_username
    
    class Meta:
        verbose_name = 'Admin'
        verbose_name_plural = 'Admins'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_picture = models.ImageField()  #change upload to file when its set up
    bio = models.TextField()

    def __str__(self):
        return self.Users.username

    class Meta:
        verbose_name = 'UserProfile'
        verbose_name_plural = 'UserProfiles'


