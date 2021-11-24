#%% 
"""
Classes for the movie calatog project.

2 Classes must be created:
Domain and Service.

Domain:
    class name: Movie
    Parameters:
        name: str
    methods:
        __str__()
    Responsabilities:
        Represent a movie object

Service:
    Class name: MovieCatalog
    Parameters:
        filePath = str <<static>>
    Methods:
        addMovie(Movie) <<static>>
        showMovies() <<Static>>
        delete() <<static>>
    Responsabilities
        Operations over movie file (.txt)

"""

class Movie:
    """
    Creation of movie objects
    """
    def __init__(self, name: str) -> None:
        self._name = name

    def __str__(self):
        return f'Movie name: {self._name}'

    # Getter and Setter
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, name: str):
        self._name = name


###### Movie Catalog.
# Needs aggregate movies
class MovieCatalog:
    """ 
    A movie catalog object!
    """
    # Static parameters
    file_path = ''

    # Static Methods (classmethod)
    @classmethod
    def addMovie(cls, name: str=None,  movie: Movie=None) -> None:
        # Add a movie to the .txt file.
        
        # If just name is passed.
        if name != None:
            movie = Movie(name)
            cls.addMovie(movie=movie)

        # If Movie object is passed.
        elif movie != None:
            with open(cls.file_path, 'a', encoding='utf8') as file:
                file.write(f'{movie.name}\n')
                file.close()

    @classmethod
    def showMovies(cls):
        # Show the movie list in the file_path file.
        try:
            with open(cls.file_path, 'r', encoding='utf8') as file:
                print('Movie Catalog'.center(45, '*'))
                print(file.read()) 
        
        # Catching error!         
        except FileNotFoundError:
            print('[ERROR] The file dont exists or wrong path.')


    @classmethod
    def delete(cls):
        # Delete the file.
        import os
        
        os.remove(cls.file_path)
        print('Catalog deleted!'.center(45, '*'))


    # Init method
    def __init__(self, file_path: str) -> None:
        MovieCatalog.file_path = file_path


# %% Testing the clases
if __name__ == '__main__':

    # Creating a movie
    spiderman = Movie('Spiderman 1')
    print(spiderman)

    # Creating a catalog
    firstCatalog = MovieCatalog('./movie_catalog.txt')
    print(firstCatalog.file_path)
    firstCatalog.addMovie(spiderman)
    firstCatalog.addMovie(movie=Movie('Spiderman 2'))
    firstCatalog.addMovie(movie=Movie('2012'))
    firstCatalog.addMovie('Titanic')
    # Testing catalog
    firstCatalog.showMovies()

    firstCatalog.delete()

    firstCatalog.showMovies()

# %%
