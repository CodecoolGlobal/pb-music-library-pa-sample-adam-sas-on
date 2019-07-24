def time_str_to_minutes(timestr):
    if ":" not in timestr or len(timestr) > 0:
        return 0.0

    tm = timestr.split(":", 2)
    try:
        tm[0] = int(tm[0])
    except ValueError:
        tm[0] = 0

    try:
        tm[1] = int(tm[1])
    except ValueError:
        tm[1] = 0

    tm[0] = float(tm[0]) + float(tm[1])/60.0
    return tm[0]
#

def get_albums_by_genre(albums, genre):
    """
    Get albums by genre

    :param list albums: albums' data
    :param str genre: genre to filter by

    :returns: all albums of given genre
    :rtype: list
    """
    genres = []
    for album in albums:
        if album[3] == genre:
            genres.append(album)

    return genres
#

def get_longest_album(albums):
    """
    Get album with biggest value in length field.
    If there are more than one such album return the first (by original lists' order)

    :param list albums: albums' data
    :returns: longest album
    :rtype: list
    """
    longest = []
    max_len = 0
    for album in albums:
        length = time_str_to_minutes(album[4])
        if length > max_len:
            longest = album
            max_len = length

    return longest
#

def get_total_albums_length(albums):
    """
    Get sum of lengths of all albums in minutes, rounded to 2 decimal places
    Example: 3:51 + 5:20 = 9.18
    :param list albums: albums' data
    :returns: total albums' length in minutes
    :rtype: float
    """
    pass
#

