# Fresh Tomatoes - View all the movie trailers in one place!

Fresh Tomatoes is a movie trailers website where you can view all the trailers for the popular movies. The website is built using Python.

## Files:
- fresh_tomatoes.py
- entertainment_center.py
- media.py

## Config:
The data about the movies are defined in the file "entertainment_center.py" which is then passed onto the "open_movies_page" function in file "fresh_tomatoes.py"

## Installing:
  Compile the source code by using Python IDLE, first open entertainment_center.py and compile it. The .html file will be compiled the directory and automatically opened using your default web browser.

## Adding Data for a Movie:
  To add another movie trailer, open the file "entertainment_center.py" and create a variable of the movie name before the "movies_list" array. The following data should be provided for each of the movie:
  - The movie's title - movie_title
  - The movie's storyline - movie_storyline
  - The movie's poster image URL - poster_image
  - The movie's youtube trailer - trailer_youtube
  - The movie's IMDB url - imdb

  Example:
  ```
  # The Revenant (2016)
  the_revenant = media.Movie(
  "The Revenant",
  "A frontiersman on a fur trading expedition in the 1820s fights for survival "
  "after being mauled by a bear.",
  "http://ia.media-imdb.com/images/M/MV5BMjU4NDExNDM1NF5BMl5BanBnXkFtZTgwMDIyMTgxNzE@._V1_SY1000_CR0,0,674,1000_AL_.jpg", #noqa
  "https://www.youtube.com/watch?v=LoebZZ8K5N0",
  "http://www.imdb.com/title/tt1663202/")
  ```
