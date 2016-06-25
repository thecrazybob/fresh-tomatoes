# Importing the necessary modules
import webbrowser

# The class for the movie's data to go in
class Movie():
    """
	Class for Inputs of each movie instance
    """
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, imdb):
    	"""
            The constructor for creating variables for each movie instance
    	"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.imdb_url = imdb

    def show_trailer(self):
    	"""
	    Method for opening the trailer in user's browser using the 'webbrowser' module.
    	"""
        webbrowser.open(self.trailer_youtube_url)
