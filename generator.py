#!python3

import sys
import getopt
import numpy as np
import matplotlib.pyplot as plt
from xml.etree.ElementTree import tostring

def help_text():
    print("Gaussian Generator - Generates a List of Gauss-Distributed Values (2022 March 07)")
    print(" ")
    print("Usage: generator [arguments]           generates a list of gauss-distributed integers")
    print(" ")
    print("Arguments:")
    print("       -c [N]                Center of Gaussian-Distribution")
    print("       -s [N]                Spread of Gaussian-Distribution")
    print("       -n [N]                Number of Values to generate")
    print("       -f <filename>         Save Values to File")

def version_text():
    print("Version 1.0 written by Stephan Bökelmann, stephan.boekelmann@thga.de")

mu = 0
sigma = 0
number_of_values = 10000
filename = "list_of_integers"


argv = sys.argv[1:]

try:
    opts, args = getopt.getopt(argv, "c:s:n:f:hv",
        ["center =", "stddev =","amount =","filename ="])
except:
    print("Incorrect usage")
    help_text()

for opt, arg in opts:
    if opt in ['-c', '--center']:
        mu = arg
    elif opt in ['-s', '--stddev']:
        sigma = arg
    elif opt in ['-n', '--amount']:
        number_of_values = arg
    elif opt in ['-h']:
        help_text()
        exit()
    elif opt in ['-f', '--filename']:
        filename = arg
    elif opt in ['-v']:
        version_text()
        exit()

print(" ")    
print("Generating Gaussian Distribution with center = "+mu+" and a standard deviation of "+sigma)
print("Printing values into "+filename)
print(" ")

mu_int = int(mu)
sigma_int = int(sigma)
number_of_values_int = int(number_of_values)

data = np.random.normal(mu_int, sigma_int, number_of_values_int)

data_int = list(map(int, data))

data_int_postemp = [0 if x < 0 else x for x in data_int]
data_int_positive = [1024 if x > 1024 else x for x in data_int_postemp]

count, bins, ignored = plt.hist(data_int_positive, 30, density=True)
plt.plot(bins, 1/(sigma_int * np.sqrt(2 * np.pi)) *
               np.exp( - (bins - mu_int)**2 / (2 * sigma_int**2) ),
         linewidth=2, color='r')
plt.show()

filehandle = open(filename, "w")
for element in data_int_positive:
    filehandle.write(str(element)+"\n")
filehandle.close()