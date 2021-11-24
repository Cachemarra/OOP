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


# enumerate constant
ADDMOVIE = 1
SHOWMOVIES = 2
DELETEMOVIES = 3
CLOSE = 4

# initializing variables
movie_name = str

movies_path = './movies.txt'
#%% Creating the menu

if __name__ == '__main__':
    option = 0
    MovieCatalog(movies_path)

    # Menu
    while option != CLOSE:
        
        # Menu
        print('Menu Catalog'.center(45, '*'))
        print('\t1.\t Add Movie')
        print('\t2.\t Show Movies')
        print('\t3.\t Delete All Movies')
        print('\t4.\t Close Program')
        option = int(input('Welcome, Select your option!'))
        print('\n')

        if option == ADDMOVIE:
            # add a movie
            print('Adding Movie!'.center(45, '-'))
            movie_name = input("What's the Movie's name?")
            MovieCatalog.addMovie(movie_name)
            print('Movie added!')

        elif option == SHOWMOVIES:
            # Show the list of movies
            print('Printing Movie Catalog')
            MovieCatalog.showMovies()


        elif option == DELETEMOVIES:
            # Delete all movies
            print('Deleting all movies.')
            MovieCatalog.delete()
            print('All movies are deleted.')
        
        elif option == CLOSE:
            # Closing the program
            print('Closing program'.center(45, '*'))
            break

        else:
            # Unconsidered cases
            print('[ERROR] No valid option, try again.')
            option = 0
        


# %%
