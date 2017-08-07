import webbrowser

# Create class Movie to store title & box art information about movies, and tra
# iler function


class Movie():

    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_url)
