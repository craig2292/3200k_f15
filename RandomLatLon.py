import random
def random_point():

    """This function will return a random latitude and longitude tuple

    >>> lat, lon = random_point()
    >>> -90 <= lat <= 90
    True
    >>> -180 <= lon <= 180
    True
    >>> random.seed(100)
    >>> random_point()
    (-63.77953408125654, -16.2262783749523)

    """



    lat = random.uniform(-90, 90)
    lon = random.uniform(-180, 180)
    return lat, lon


if __name__ == '__main__':
    import doctest
    doctest.testmod()
