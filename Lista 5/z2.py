import csv
import numpy as np


def get_greatest_movie_id_below(max_movie_id):
    """Znajduje najwieksze movie_id < max_movie_id // + 1 aby miescilo sie do tablic"""
    greatest = 0
    with open("ml-latest-small/ratings.csv", newline='') as file:
        reader = csv.reader(file, delimiter=',')
        next(reader)
        for row in reader:
            movie_id = int(row[1])
            if movie_id < max_movie_id and movie_id > greatest:
                greatest = movie_id
    return greatest + 1


def get_ratings(max_movie_id):
    """Pobiera z pliku ratings.csv krotki [user_id, rating, movie_id] takie, że movie_id < max_movie_id"""
    print("Getting ratings...")
    ratings_ = np.zeros((611, max_movie_id))
    with open("ml-latest-small/ratings.csv", newline='') as file:
        reader = csv.reader(file, delimiter=',')
        next(reader)
        for row in reader:
            movie_id = int(row[1])
            if movie_id < max_movie_id:
                user_id = int(row[0])
                rating = float(row[2])
                ratings_[user_id][movie_id] = rating
    return ratings_


def get_movie_titles(max_movie_id):
    """"Pobiera z pliku movies.csv krotki postaci [movie_id, title]"""
    movies_ = np.empty(max_movie_id, dtype=object)
    with open("ml-latest-small/movies.csv", newline='') as file:
        reader = csv.reader(file, delimiter=',')
        next(reader)
        for row in reader:
            movie_id = int(row[0])
            if movie_id < max_movie_id:
                movies_[movie_id] = row[1]
    return movies_


def normalize(matrix):
    """Normalizuje macierz"""
    norm = np.nan_to_num(np.linalg.norm(matrix, axis=0))
    return np.nan_to_num(matrix / norm)


def create_film_profile_norm(user_ratings, ratings_):
    """Tworzy profil filmowy uzytkownika"""
    user_ratings_normalized = normalize(user_ratings)
    ratings_normalized_ = normalize(ratings_)
    z = np.dot(ratings_normalized_, user_ratings_normalized)
    z_normalized = normalize(z)
    return z_normalized


def get_recommendations(ratings_, user_ratings_):
    profile_ = create_film_profile_norm(user_ratings_, ratings_)
    ratings_normalized_ = normalize(ratings_)
    return np.dot(ratings_normalized_.T, profile_)


def assign_movies_to_recommendations(recommendations_, movies_):
    size = len(recommendations_)
    result = np.empty(size, dtype=object)
    for index, recommendation_ in enumerate(recommendations_):
        result[index] = (recommendation_[0], movies_[index], index)
    return np.array(result)


def sorting_key(entry):
    a, *_ = entry
    return a


max_movie_id = get_greatest_movie_id_below(10000)
ratings = get_ratings(max_movie_id)

my_ratings = np.zeros((9019,1))
my_ratings[2571] = 5      # patrz movies.csv  2571 - Matrix
my_ratings[32] = 4        # 32 - Twelve Monkeys
my_ratings[260] = 5       # 260 - Star Wars IV
my_ratings[1097] = 4

recommendations = get_recommendations(ratings, my_ratings)

end_result = assign_movies_to_recommendations(recommendations, get_movie_titles(max_movie_id))
print(sorted(end_result, key=sorting_key, reverse=True))
