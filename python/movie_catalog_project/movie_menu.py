#%% Menu for movie catalog!
"""
A simple menu for operate with the classes movie and movie catalog.

There would be 4 options:

1. Add Movie
2. Show Movies
3. Delete all movies
4. Close program

"""
from classes import MovieCatalog
from movie_catalog_project.classes import Movie

# enumerate constant
ADDMOVIE = 1
SHOWMOVIES = 2
DELETEMOVIES = 3
CLOSE = 4

# initializing variables
movie_name = str

#%% Creating the menu

if __name__ == '__main__':
    option = 0
    # Menu
    while option != CLOSE:
        
        # Menu
        print('Menu Catalog'.center(45, '*'))
        print('\t1.\t Add Movie')
        print('\t2.\t Show Movies')
        print('\t3.\t Delete All Movies')
        print('\t4.\t Close Program')
        option = int(input('Welcome, Select your option!'))

        if option == ADDMOVIE:
            # add a movie
            movie_name = input("What's the Movie's name?")
            MovieCatalog.addMovie(movie_name)
            pass

        elif option == SHOWMOVIES:
            # Show the list of movies
            pass

        elif option == DELETEMOVIES:
            # Delete all movies
            pass
        
        elif option == CLOSE:
            # Closing the program
            pass

        else
            # Unconsidered cases
            print('[ERROR] No valid option, try again.')
        


# %%
()