from naural_network import *
import matplotlib.pyplot as plt

training_x_plot = np.linspace(-50, 50, 26, dtype=np.float128)
training_x = np.array(list(zip(training_x_plot, np.ones(26))), dtype=np.float128)

training_y_temp = np.linspace(-50, 50, 26)**2
training_y = np.array([[item] for item in training_y_temp])

testing_x_plot = np.linspace(-50, 50, 101)
testing_x = np.array(list(zip(testing_x_plot, np.ones(101))), dtype=np.float128)

testing_y_plot = np.linspace(-50, 50, 101) ** 2
testing_y = np.array([[item] for item in testing_y_plot])

nn = NeuralNetwork(training_x, training_y, 10, sigmoid_activation, tanh_activation)

for i in range(5000):
    nn.feedforward()
    nn.back_propagation()
    if i % 1000 == 0:
        nn.input = testing_x
        nn.feedforward()
        print("SQUARE", i, mean_square_error(testing_y_plot, nn.output))
        plt.scatter(testing_x_plot, nn.output)
        nn.input = training_x
        plt.show()

training_x_plot = np.linspace(0, 2, 21, dtype=np.float128)
training_x = np.array(list(zip(training_x_plot, np.ones(21))), dtype=np.float128)

training_y_temp = np.sin((3 * np.pi / 2) * training_x_plot)
training_y = np.array([[item] for item in training_y_temp])

np.seterr(all='raise')

testing_x_plot = np.linspace(0, 2, 161)
testing_x = np.array(list(zip(testing_x_plot, np.ones(161))), dtype=np.float128)

testing_y_plot = np.sin((3 * np.pi / 2) * testing_x_plot)
testing_y = np.array([[item] for item in testing_y_plot])

nn = NeuralNetwork(training_x, training_y, 10, sigmoid_activation, sigmoid_activation)


for i in range(5000):
    nn.feedforward()
    nn.back_propagation()
    if i % 1000 == 0:
        nn.input = testing_x
        nn.feedforward()
        print("SIN", i, mean_square_error(testing_y_plot, nn.output))
        plt.scatter(testing_x_plot, nn.output)
        nn.input = training_x
        plt.show()





