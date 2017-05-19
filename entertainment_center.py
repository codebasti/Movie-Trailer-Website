import media
import fresh_tomatoes

#the following instances each store 1 concrete movie + its details and gives it the Movie class from media.py
rambo1 = media.Movie("Rambo 1",
                     "A man killing pigs bare-handed",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BODBmOWU2YWMtZGUzZi00YzRhLWJjNDAtYTUwNWVkNDcyZmU5XkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UY1200_CR85,0,630,1200_AL_.jpg",
                     "https://www.youtube.com/watch?v=9Txo84-yx44")

starwars = media.Movie("StarWars",
                       "Galaxy Wars",
                       "https://i.kinja-img.com/gawker-media/image/upload/s--S24cks6n--/c_scale,f_auto,fl_progressive,q_80,w_800/19fk32sw3nt1wjpg.jpg",
                       "https://www.youtube.com/watch?v=2P_kaYqH8qk")

silence = media.Movie("the silence of the lambs",
                       "Dr. Lecter",
                       "https://i.stack.imgur.com/KYuPU.jpg",
                       "https://www.youtube.com/watch?v=JismZR7zp4U")

#the movies array contains all movies, that we want to see on the webpage
movies = [rambo1, starwars, silence]

#calls the open_movies_page function in fresh_tomatoes.py and gives it the movies-array
fresh_tomatoes.open_movies_page(movies)
