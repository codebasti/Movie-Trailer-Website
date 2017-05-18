import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=3PsUJFEBC74")

#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://s3.foxmovies.com/foxmovies/production/films/18/images/posters/251-asset-page.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print(storyline)
#avatar.show_trailer()

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


movies = [rambo1, starwars, silence]
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)
