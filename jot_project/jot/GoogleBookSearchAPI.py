import json
from urllib.request import urlopen

#given a books title this function returns an arrray of the form [Average Rating,Number of reviews]
def getRatings(title):
    #Setting up the basic api call 
    api = "https://www.googleapis.com/books/v1/volumes?q=:"

    #Swap the spaces in the tile with +
    title = title.replace(" ", "+")

    # send a request and get a JSON response
    resp = urlopen(api + title)
    # parse JSON into Python as a dictionary
    book_data = json.load(resp)

    #Get the info for the first book from the query 
    volume_info = book_data["items"][0]["volumeInfo"]
    return [volume_info['averageRating'],volume_info['ratingsCount']]
