import csv
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def get_greatest_user_id():
    greatest_id = 0
    with open("ml-latest-small/ratings.csv", newline='') as file:
        reader = csv.reader(file, delimiter=',')
        next(reader)
        for row in reader:
            movie_id = int(row[1])
            user_id = int(row[0])
            if movie_id == 1:
                greatest_id = user_id
    return greatest_id


def get_user_ids():
    size = get_greatest_user_id()
    users = np.empty(size+1, dtype=object)
    user_iterator = 0
    with open("ml-latest-small/ratings.csv", newline='') as file:
        reader = csv.reader(file, delimiter=',')
        next(reader)
        for row in reader:
            movie_id = int(row[1])
            if movie_id == 1:
                user_id = int(row[0])
                users[user_id] = user_iterator
                user_iterator += 1
    return users


def generate_x_and_y(users_, m_):
    highest_user_id = users_[-1]
    y_ = np.zeros(highest_user_id+1)
    x_ = np.zeros((highest_user_id+1, m_))
    with open("ml-latest-small/ratings.csv", newline='') as file:
        reader = csv.reader(file, delimiter=',')
        next(reader)
        for row in reader:
            user_id = int(row[0])
            movie_id = int(row[1])
            if users_[user_id] is not None and movie_id < m_ + 2:
                rating = float(row[2])
                if movie_id == 1:
                    y_[users_[user_id]] = rating
                else:
                    x_[users_[user_id]][movie_id-2] = rating  # -2 bo nie chcemy filmow o id=0 oraz id=1
    return x_, y_


def zad1(m_array_, training_set_size):
    users = get_user_ids()
    for m in m_array_:
        matrix_x, matrix_y = generate_x_and_y(users, m)
        matrix_x_training = matrix_x[:training_set_size]
        matrix_y_training = matrix_y[:training_set_size]

        model = LinearRegression().fit(matrix_x_training, matrix_y_training)
        model.score(matrix_x, matrix_y)

        predicted_y = model.predict(matrix_x)

        x = np.array(range(0, 215))
        plt.plot(x, matrix_y, 'o', label='Original data', markersize=10)
        plt.plot(x, predicted_y, 'r', label='Fitted line')
        plt.legend()
        plt.title("m: " + str(m) + " traing set size: " + str(training_set_size))
        plt.show()


m_array = [10, 100, 1000, 10000]

zad1(m_array, 215)
zad1(m_array, 200)
