import json
from urllib.request import urlopen

#given a books title this function returns an arrray of the form [Average Rating,Number of reviews]
def getRatings(title):
    #Setting up the basic api call 
    api = "https://www.googleapis.com/books/v1/volumes?q=:"

    #Swap the spaces in the tile with +
    title = str(title).replace(" ", "+")

    # send a request and get a JSON response
    resp = urlopen(api + title)
    # parse JSON into Python as a dictionary
    results = json.load(resp)
    
    #Return a default value if there are no results 
    if results["totalItems"] == 0:
        return [0,0]

    #Get the info for the first book from the query 
    bookInfo = results["items"][0]["volumeInfo"]

    #check if the book has been reviewed
    if 'ratingsCount' in bookInfo:
        return [bookInfo['averageRating'],bookInfo['ratingsCount']]
    else:
        return [0,0]
