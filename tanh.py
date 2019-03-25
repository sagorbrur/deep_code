# Tanh Activation function
# The range of the tanh function is from (-1 to 1)
# tanh(x)=((e^x-e^(-x))/(e^x+e^(-x)))

e = 2.7182818284590451


def tanh(x):
    return ((e**x)-(e**(-x)))/((e**x)+(e**(-x)))

values = [5,6,-3,1,0]

for i in values:
    print(tanh(i))
