# Importing Necessary Modules
import media
import fresh_tomatoes

# Data for Movie Trailers

# Captain America: Civil War (2016)
ca_civil_war = media.Movie(
    "Captain America",
    "Political interference in the Avengers' activities causes a rift between "
    "former allies Captain America and Iron Man.",
    "http://ia.media-imdb.com/images/M/MV5BMjQ0MTgyNjAxMV5BMl5BanBnXkFtZTgwNjUzMDkyODE@._V1_SY1000_CR0,0,674,1000_AL_.jpg", #noqa
    "https://www.youtube.com/watch?v=dKrVegVI0Us",
    "http://www.imdb.com/title/tt3498820/")

# Jason Bourne (2016)
jason_bourne = media.Movie(
    "Jason Bourne",
    "Jason Bourne, now remembering who he truly is, tries to uncover hidden "
    "truths about his past.",
    "http://ia.media-imdb.com/images/M/MV5BMTU1ODg2OTU1MV5BMl5BanBnXkFtZTgwMzA5OTg2ODE@._V1_SY1000_SX632_AL_.jpg", #noqa
    "https://www.youtube.com/watch?v=F4gJsKZvqE4",
    "http://www.imdb.com/title/tt4196776/")

# The Martian (2016)
the_martian = media.Movie(
    "The Martian",
    "An astronaut becomes stranded on Mars after his team assume him dead, "
    "and must rely on his ingenuity to find a way to signal to Earth that he "
    "is alive.",
    "http://ia.media-imdb.com/images/M/MV5BMTc2MTQ3MDA1Nl5BMl5BanBnXkFtZTgwODA3OTI4NjE@._V1_UX182_CR0,0,182,268_AL_.jpg", #noqa
    "https://www.youtube.com/watch?v=lQqhfq87FgY",
    "http://www.imdb.com/title/tt3659388/")

# The Revenant (2016)
the_revenant = media.Movie(
    "The Revenant",
    "A frontiersman on a fur trading expedition in the 1820s fights for "
    "survival after being mauled by a bear.",
    "http://ia.media-imdb.com/images/M/MV5BMjU4NDExNDM1NF5BMl5BanBnXkFtZTgwMDIyMTgxNzE@._V1_SY1000_CR0,0,674,1000_AL_.jpg", #noqa
    "https://www.youtube.com/watch?v=LoebZZ8K5N0",
    "http://www.imdb.com/title/tt1663202/")

# Kung Fu Panda (2016)
kung_fu_panda_3 = media.Movie(
    "Kung Fu Panda 3",
    "Continuing his \"legendary adventures of awesomeness\", Po must face "
    "two hugely epic, but different threats: one supernatural and the other "
    "a little closer to his home.",
    "http://ia.media-imdb.com/images/M/MV5BMTUyNzgxNjg2M15BMl5BanBnXkFtZTgwMTY1NDI1NjE@._V1_.jpg", #noqa
    "https://www.youtube.com/watch?v=fGPPfZIvtCw",
    "http://www.imdb.com/title/tt2267968/")

# The Jungle Book (2016)
the_jungle_book = media.Movie(
    "The Jungle Book",
    "After a threat from the tiger Shere Khan forces him to flee the jungle.",
    "http://ia.media-imdb.com/images/M/MV5BMTc3NTUzNTI4MV5BMl5BanBnXkFtZTgwNjU0NjU5NzE@._V1_SY1000_SX675_AL_.jpg", #noqa
    "https://www.youtube.com/watch?v=C4qgAaxB_pc",
    "http://www.imdb.com/title/tt3040964/")

# Array/List of all the Movies
movies_list = [ca_civil_war, jason_bourne, kung_fu_panda_3, the_martian, the_revenant, the_jungle_book]

# Sending the data to fresh_tomatoes.py
fresh_tomatoes.open_movies_page(movies_list)
