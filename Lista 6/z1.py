from naural_network import *
import itertools

x = np.array([[0, 0, 1],
              [0, 1, 1],
              [1, 0, 1],
              [1, 1, 1]])

y_xor = [np.array([[0], [1], [1], [0]]), "XOR"]
y_or = [np.array([[0], [1], [1], [1]]), "OR"]
y_and = [np.array([[0], [0], [0], [1]]), "AND"]

logic_gates = [y_xor, y_or, y_and]
activation_functions = [sigmoid_activation, relu_activation]

print("FUNKCJA LOGICZNA | AKTYWACJA WARSTWY UKRYTEJ | AKTYWACJA WARSTWY WYJSCIOWEJ")
for logic_gate, activation_fun_hidden, activation_fun_output in \
        itertools.product(logic_gates, activation_functions, activation_functions):
    nn = NeuralNetwork(x, logic_gate[0], 4, activation_fun_hidden, activation_fun_output)
    for i in range(5000):
        nn.feedforward()
        nn.back_propagation()
    print(logic_gate[1],
          activation_fun_hidden.name,
          activation_fun_output.name,
          "\n", nn.output)


# ODPOWIEDZ NA PYTANIE
# Każdy neuron ma na wyjsciu sumę iloczynów wejść i wag pomnożony przez funkcję aktywacji.
# Bez jedynek, wagi w warstwie wyjściowej muszą być większe, aby otrzymane wartości z warstwy poprzedniej
# zostały zwiększone do odpowiedniej wartości wynikowej. Z jedynkami natomiast, ostatnia warstwa
# może 'pożyczyć' trochę z tych jedynek zamiast zwiększać wagi, tym samym wracając oczekiwany wynik.
