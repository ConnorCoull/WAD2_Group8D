#Use the django.test.TestCase class for tests that rely on the back-end database
#Otherwise use the unittest.TestCase class   
from django.test import TestCase
import unittest

from jot.GoogleBookSearchAPI import getRatings

# Create your tests here.
class ApiSearchTestCase(unittest.TestCase):

    def test_api_search(self):
        #gibberish search should return the default array 
        self.assertEqual(getRatings("sdjbksfgbjqlswdgf2432ssdf"),[0,0])
        #Book has no reviews and so should return the default array - might change should consider mocking
        self.assertEqual(getRatings("the blue book of grammar and punctuation"),[0,0])
        #GetRatings should be able to take numeric titles no problem 
        self.assertNotEqual(getRatings(1984), [0,0])
        #Normal search should renturn a non-deafult result 
        self.assertNotEqual(getRatings("Lord of the Rings"),[0,0])
