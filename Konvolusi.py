# -*- coding: utf-8 -*-



def convolution(signal1, signal2):
    result_length = len(signal1) + len(signal2) - 1
    result = [0] * result_length

    # Perform convolution
    for i in range(len(signal1)):
        for j in range(len(signal2)):
            result[i + j] += signal1[i] * signal2[j]

    return result

# Define two 1-dimensional arrays (signals)
signal1 = [1, 2, 4,7]
signal2 = [1, 5, 6]

# Perform convolution
convolution_result = convolution(signal1, signal2)

# Output the convolution result
print("Convolution Result: ", convolution_result)

print("Naive Implementation of Convolution")
print("nama: Rafi Andromeda Pratama")
print("nrp: 5009211001") 


