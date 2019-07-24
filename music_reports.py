def time_str_to_minutes(timestr):
    if ":" not in timestr or len(timestr) < 1:
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

def time_minutes_to_str(timemin):
    mins,secs = divmod(timemin*60, 60)
    return "{0:02.0f}:{1:02.0f}".format(mins, secs)
#

def get_albums_by_genre(albums, genre):
    """
    Get albums by genre

    :param list albums: albums' data
    :param str genre: genre to filter by

    :returns: all albums of given genre
    :rtype: list
    """
    albums2 = []
    for album in albums:
        if album[3] == genre:
            albums2.append(album)

    if len(albums2) < 1:
        raise ValueError("Wrong genre")

    return albums2
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
    time_tot = 0.0
    for album in albums:
        length = time_str_to_minutes(album[4])
        time_tot += length

    return time_tot
#

def get_genre_stats(albums):
    genres_dict = {}
    for album in albums:
        if len(album) < 4:
            continue

        genres_dict[album[3]] = genres_dict[album[3]] + 1 if album[3] in genres_dict else 1

    return genres_dict
#


def get_last_oldest(albums):
    return []
#

def get_last_oldest_of_genre(albums, genre):
    oldest = []
    year = False

    for album in albums:
        if len(album) < 4 or album[3] != genre:
            continue

        try:
            year2 = int(album[2])
        except:
            continue

        if year2 < year or year == False:
            oldest = album
            year = year2
    return oldest
#

#/ - - - - - -

def get_genres(albums):
    genres_dict = {}
    for album in albums:
        if len(album) < 4:
            continue

        genres_dict[album[3]] = 1

    return list(genres_dict.keys())
#

