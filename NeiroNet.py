import numpy as np

vodka = 0.0
rain = 0.0
friend = 1.0


def activation_function(x):
    if x >= 0.5:
        return 1
    else:
        return 0


def predict(vodka, rain, friend):
    inputs = np.array([vodka, rain, friend])
    print("Input = " + str(inputs) + "\n \/")
    weights_input_to_hiden_1 = [0.25, 0.25, 0]
    weights_input_to_hiden_2 = [0.5, -0.4, 0.9]
    weights_input_to_hiden = np.array([weights_input_to_hiden_1, weights_input_to_hiden_2])
    weights_hiden_to_output = np.array([-1, 1])
    hiden_input = np.dot(weights_input_to_hiden, inputs)
    print("Hiden Input = " + str(hiden_input) + "\n \/")
    hiden_output = np.array([activation_function(x) for x in hiden_input])
    print("Hiden Output = " + str(hiden_output) + "\n \/")
    output = np.dot(weights_hiden_to_output, hiden_output)
    print("Output = " + str(output) + "\n")
    return activation_function(output) == 1


print("RESULT: " + str(predict(vodka, rain, friend)))
