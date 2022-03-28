from django.db import models 
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
import os
from django.template.defaultfilters import slugify
 
from django.db.models.signals import post_save
from django.dispatch import receiver

# Models.py
#                       
# Category - We sort each book into a category.
# 
# Book - This stores all the information for the books.
# 
# Review - This is where the information for a review on a book is stored.
#


# Note the user_type is a boolean value that stores whether the user is a reader or a writer. 
# The user_type is simply just for display purposes on the users profile and has no other effect.


class Category(models.Model):
    category_name = models.CharField(max_length = 64, unique=True) 
    slug = models.SlugField()
    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name)
        super(Category, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

        
    def __str__(self):
        return self.category_name



class Book(models.Model):
 
    #There is an uploaded_by and author. This is because a user might want to upload a book they themselves did not write.
    #The bookID is what we can use to uniquely identify books, as we allow users to upload books of the same title.
    #The book model contains a FileField which allows the user to upload their book.
    #The book average rating can only between 1 and 5 as users can only rate it from 1 to 5.
    
    bookID = models.AutoField(primary_key=True)
    book_category = models.ForeignKey(Category, on_delete=models.CASCADE, null = True)
    book_title = models.CharField(max_length=128)
    pdf_location = (str(book_title)+'.pdf')
    author = models.CharField(max_length=64)
    book_description = models.CharField(max_length=1024)
    pdf_upload = models.FileField(upload_to = 'books/')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    book_date_published = models.DateField(auto_now=False, auto_now_add=True)
    book_average_rating = models.PositiveIntegerField(
        default = 1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    ) 
    book_file_path = models.CharField(max_length=128)
    book_views = models.IntegerField(default=0)
    slug = models.SlugField()
    def save(self, *args, **kwargs):
        self.slug = slugify(self.bookID)
        super(Book, self).save(*args, **kwargs)


    def __str__(self):
        return self.book_title
    
    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'


    #Like we have done in Book, review uses a reviewID which uniquely identifies any given review
    #When giving a review, the user can give it a score from 1 to 5

class Review(models.Model):
    
    reviewID = models.AutoField(primary_key=True)
    review_book = models.ForeignKey(Book, on_delete=models.CASCADE, null = True)
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    review_rating = models.IntegerField( 
        
        default = 1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]

    
    )
    review_date_written = models.DateField(auto_now=False, auto_now_add=True)
    review_content = models.CharField(max_length=1024)

    

    def __str__(self):
        return self.review_content

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_picture = models.ImageField(upload_to='userprofiles')  
    bio = models.CharField(blank=True, default="hello, i'm on JOT!", max_length=250)
    user_picture_file=str(user_picture)+'.pdf'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(UserProfile, self).save(*args, **kwargs)

  

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'UserProfile'
        verbose_name_plural = 'UserProfiles'




#This function just updates the related User Model when the UserProfile gets updated
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
