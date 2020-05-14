import numpy as np
from scipy.special import expit


def sigmoid(x):
    return expit(x)


def sigmoid_derivative(x):
    return x * (1.0 - x)


def relu(x):
    return np.maximum(0, x)


def relu_derivative(x):
    return np.where(x <= 0, 0, 1)


def tanh(x):
    return np.tanh(x)


def tanh_derivative(x):
    return 1.0 - x**2


class ActivationFunction:
    def __init__(self, function, derivative, name):
        self.name = name
        self.function = function
        self.derivative = derivative


sigmoid_activation = ActivationFunction(sigmoid, sigmoid_derivative, "SIGMOID")
relu_activation = ActivationFunction(relu, relu_derivative, "RELU")
tanh_activation = ActivationFunction(tanh, tanh_derivative, "TANH")


class NeuralNetwork:
    def __init__(self, x, y, hidden_layer_length,
                 hidden_layer_activation: ActivationFunction,
                 output_layer_activation: ActivationFunction):
        self.input = x
        self.weights1 = np.random.rand(hidden_layer_length, self.input.shape[1])
        self.weights2 = np.random.rand(1, hidden_layer_length)
        self.y = y
        self.output = np.zeros(self.y.shape)
        self.eta = 0.5
        self.layer1 = np.empty_like
        self.hidden_layer_activation = hidden_layer_activation
        self.output_layer_activation = output_layer_activation

    def feedforward(self):
        self.layer1 = self.hidden_layer_activation.function(
            np.dot(self.input, self.weights1.T))
        self.output = self.output_layer_activation.function(
            np.dot(self.layer1, self.weights2.T))

    def back_propagation(self):
        delta2 = (self.y - self.output) * self.output_layer_activation.derivative(self.output)
        d_weights2 = self.eta * np.dot(delta2.T, self.layer1)
        delta1 = self.hidden_layer_activation.derivative(self.layer1) * \
            np.dot(delta2, self.weights2)
        d_weights1 = self.eta * np.dot(delta1.T, self.input)

        self.weights1 += d_weights1
        self.weights2 += d_weights2


class NeuralNetwork2:
    def __init__(self, x, y, hidden_layer_length,
                 hidden_layer_activation: ActivationFunction,
                 output_layer_activation: ActivationFunction):
        self.input = x
        self.weights1 = np.random.rand(hidden_layer_length, self.input.shape[1])
        self.weights2 = np.random.rand(hidden_layer_length, hidden_layer_length)
        self.weights3 = np.random.rand(1, hidden_layer_length)
        self.y = y
        self.output = np.zeros(self.y.shape)
        self.eta = 0.5
        self.layer1 = np.empty_like
        self.layer2 = np.empty_like
        self.hidden_layer_activation = hidden_layer_activation
        self.output_layer_activation = output_layer_activation

    def feedforward(self):
        self.layer1 = self.hidden_layer_activation.function(
            np.dot(self.input, self.weights1.T))
        self.layer2 = self.hidden_layer_activation.function(
            np.dot(self.layer1, self.weights2.T))
        self.output = self.output_layer_activation.function(
            np.dot(self.layer2, self.weights3.T))

    def back_propagation(self):
        delta3 = (self.y - self.output) * self.output_layer_activation.derivative(self.output)
        d_weights3 = self.eta * np.dot(delta3.T, self.layer2)
        delta2 = self.hidden_layer_activation.derivative(self.layer2) * np.dot(delta3, self.weights3)
        d_weights2 = self.eta * np.dot(delta2.T, self.layer1)
        delta1 = self.hidden_layer_activation.derivative(self.layer1) * np.dot(delta2, self.weights2)
        d_weights1 = self.eta * np.dot(delta1.T, self.input)

        self.weights1 += d_weights1
        self.weights2 += d_weights2
        self.weights3 += d_weights3


def mean_square_error(x: list, y):
    sum_ = 0
    for item1, item2 in zip(x, y):
        sum_ += (item1 - item2)**2
    error = sum_/len(x)
    return error
