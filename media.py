import webbrowser

#create the Movie class - it contains all details of a movie
class Movie():

    #init function initializes space in memory for our movie instances located in entertainment.py
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    #show_trailer function opens the youtube-trailer in our webbrowser
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
