import media
import fresh_tomatoes

#Store information for the 6 chosen movies

trumbo = media.Movie("Trumbo",
               "https://upload.wikimedia.org/wikipedia/en/9/96/Trumbo_%282015_film%29_poster.jpg",
               "https://www.youtube.com/watch?v=n0dZ_2ICpJE"
               )

megamind = media.Movie("Megamind",
                 "https://upload.wikimedia.org/wikipedia/en/thumb/8/89/Megamind2010Poster.jpg/220px-Megamind2010Poster.jpg",
                 "https://www.youtube.com/watch?v=Xu42-p6_5RE"
                 )

invention = media.Movie("The Invention of Lying",
                  "https://upload.wikimedia.org/wikipedia/en/thumb/2/2b/Invention_of_lying_ver2.jpg/220px-Invention_of_lying_ver2.jpg",
                  "https://www.youtube.com/watch?v=vn71hYvyqCA"
                  )

vendetta = media.Movie("V for Vendetta",
                 "https://upload.wikimedia.org/wikipedia/en/thumb/9/9f/Vforvendettamov.jpg/220px-Vforvendettamov.jpg",
                 "https://www.youtube.com/watch?v=qxyUl9M_7vc"
                 )

win = media.Movie("Win Win",
            "https://upload.wikimedia.org/wikipedia/en/5/5e/Win_Win_Poster.jpg",
            "https://www.youtube.com/watch?v=ci_I6n2j5Uw"
            )

hector = media.Movie("Hector and the Search for Happiness",
               "https://upload.wikimedia.org/wikipedia/en/7/7d/Hector_and_the_Search_for_Happiness_poster.jpg",
               "https://www.youtube.com/watch?v=iWFVAIbIkS4"
               )

#Store all the movies in an array
LIST_OF_MOVIES = [trumbo, megamind, invention, vendetta, win, hector]

#Create page with movies
fresh_tomatoes.open_movies_page(LIST_OF_MOVIES)             
               
