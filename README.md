# Tugas-2
# A. Convolution of two 1-dimensional array signals.
![Screenshot (1523)](https://github.com/RafiAndro/Tugas-2/assets/144668735/2237662f-98e4-40fa-81e7-0ac60132b580)
In this implementation, 'the convolution()' function takes two input arrays 'signal1' and 'signal2' and calculates their convolution without using any external libraries. The result is stored in the 'convolution_result list', which is then printed

# How it works 
1) Initialization:
result_length is calculated as the sum of the lengths of signal1 and signal2 minus 1. This determines the length of the resulting convolution signal.
result is initialized as a list of zeros with a length of result_length. This list will store the calculated convolution values.
2) Nested Loops:
The outer loop iterates over each element of signal1.
The inner loop iterates over each element of signal2.
3) Multiplication and Accumulation:
For each combination of elements from signal1 and signal2, their product is calculated: signal1[i] * signal2[j].
The product is then added to the appropriate position in the result list. The position is determined by the sum of the indices i and j. This corresponds to the convolution operation where overlapping elements are multiplied and accumulated.
