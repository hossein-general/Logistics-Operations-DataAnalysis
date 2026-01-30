import numpy as np
from numpy import random
# import ipdb

#region predefined arrays
a = np.array([1,2,3,4])
b = np.array([[1,2,3,4], [5,6,7,8]])
c = np.array([[[1,2,3,4,5],[6,7,8,9,10]]])
d = np.array([3,2,3,1])
a1 = np.array([1.5, 2.3, 4.6, 5.4, 3.8])
a2 = np.array([[1,2,5],[3,4,4]])
a3 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
a4 = np.array([[1,2],[3,4]])
a5 = np.array([[10,20],[30,40]])
a6 = np.array([1.002, 2.1234, 1.0, 1, 5.3])
a7 = np.array([3.1, 3.8, -3.1, -3.8])
a8 = np.array([[1,2], [3,4]])
a8 = np.array([[10,20], [30,40]])
a9 = np.array([1,3,5,3,3,2,1])
a10 = np.array([1,5,7,8,4,2])
a11 = np.array([2,8,7,4])
a12 = np.array([1,2,5])
test = np.array([[11,22],[13,23],[1,2]])
test2 = np.array([[1,2,3],[4,5,6]])
test3 = np.array([[[111,112],[121,122],[131,132]],[[111,112],[121,122],[131,132]],[[211,212],[221,222],[231,232]]])
#endregion

#region numpy
# ------------------------ numpy--------------------------------
# Variables/Classes:
np.__version__          # numpy version 
np.sctypeDict           # different available data types
np.newaxis              # as a placeholder for an empty axis in array. e.g.: test = a1[:, :, np.newaxis]
                        # test = a1[:, :, np.newaxis]  --(works the same as)--> test = a1[:, :, None]

# Functions:
x = np.array([11,22,33], ndmin=5)       # with kw argumenst:

x1 = np.array([[1,2],[3,4]])
x2 = np.matrix([[1,2],[3,4]])

np.concatenate((a4,a5), axis=0)         # axis=0: (vertically) the arrays are joined along the first dimension | axis=1: (horizontally) the arrays are joined along the second dimension
                                        # self-added note: all axises except the axis specified have to have the same value in both arrays. e.g.: a4.shape=(1,2,9,1) a5.shape=(1,2,18,1) axis=2
np.split(a3,4)                          # split the array into 4 different arrays, returned as a list (splits on the axis=0)
np.where(a%2==0)                        # returns the indexes for items that meets the conditions
# TODO chech the returns for where

np.add(a,d)                             # a+d
np.subtract(a,d)                        # a-d
np.multiply(a,d)                        # a*d
np.divide(a,d)                          # a/d
np.power(a,d)                           # a^d
np.mod(a,d)                             # a%d
np.sqrt(4)                              # returns the square root for the number given

np.absolute(7)                          # changes negative values to their positive value
np.fix(a7)                              # removes the floating point (both negative and positive values)
np.floor(a7)                            # rounds to the smaller number
np.ceil(a7)                             # rounds to the larger number
np.round(a6, 2)                         # rounds the number. a6 could be an array (or tuple, list, ...) and the second argument (2 in this case) shows the number of digits after floating point (if no value given, it will remove floating point and round the number)

np.sum((a,d), axis=1)                   # sums up the valumatrises (it has kind of a veird behaviour, check it yourself)
# TODO check the sum() functions behaviour

x1.dot(x1)                              # matrix multiplier firs matrix/arrays should have the same column count as the second ones row count
x1@x1                                   # matrix multiplier1

np.prod(x1)                             # multiplies all values within the array by each other (in this case: 1*2*3*4=24)

np.size(b)                              # gives the total count of values within an array/matrix/list/...

np.ones((3,3))                          # fills the array with 1. (float values)
np.zeros((3,3))                         # fills the array with 0. (float values )
np.arange(1,10,2)                       # returns an array consisting of numbers (1) to (10) with the step of (2)
                                        # e.g.: making a plots x-axis have labels with a certain start point, end point and step
np.linspace(1,10,4)                     # retunrs an array consisting of (4) numbers evenly seperated between (1) and (10)

np.nan                                  # not a number
np.inf                                  # infinite

np.logical_and(a>2,a<12)                # considering both conditions it will broadcast arrays together if the shapes were not the same and if it was possible. it will return an array of boolean values
np.logical_or(a>2,a<12)                 # considering both conditions it will broadcast arrays together if the shapes were not the same and if it was possible. it will return an array of boolean values
np.logical_xor(a>2,a<12)                # considering both conditions it will broadcast arrays together if the shapes were not the same and if it was possible. it will return an array of boolean values
np.logical_not(a<3)                     # considering the condition it will negate the resault and return the value as an array of booleans

np.unique(a9)                           # removes duplicate values

np.union1d(a10,a11)                     # returns the union of two arrays
np.intersect1d(a10,a11)                 # retunrs the intersection of two arrays

np.polyval(a12,3)                       # uses the a12 values as the multipliers for x in a funcition. e.g.: 1*x^2 + 2*x^1 + 5*x^0
                                        # e.g. 2: [1,0,0,3,0,7] ----> x^5 + 3*x^2 + 7
np.polyder(a12)                         # gives the derivation of a funciton (in this case the derivation for 1*x^2 + 2*x^1 + 5*x^0 is --> 2*x^1 + 2*x^0)
np.polyint(a12)                         # returns the integeral for that function



#endregion


#region Random
# ------------------------ random ----------------------------------
# Functions
random.randint(10,100, size=(5,3))      # can specify a matrix with size argument. it could be a single number to indicate an array of that size full of random values
random.rand(3,2)                        # gives a matrix 3x2 of numbers between 0 and 1
random.choice(np.array([1,3,5,9]), size=(3,2))      # the size kwarg is optional
random.choice(np.array([1,3,5]), p=[0.4, 0, 0.6], size=(3,3))      # p indicats the chance for each value. the size kw argument is optional


#endregion



#region Array
# ------------------------ numpy.ndarray -----------------------
# Attributes: 
a.ndim
a2.shape
a2.dtype                    # shows the data type used in that array

# Methods:
a1.astype("i")              # changes the type of the items within an array. "i": integer, bool: boolean, float: float
a3.reshape(2,6)             # 2 rows and 6 columns


# indexings (behaviours)
a[3]
a[-1]
a3[a]                       # if given an array, will return another array containing indexes from the first array. multiple arrays will in
                            # a3[(a)] is allowed as well (tuple of an array) (its a normal python behaviour btw)
                            # as arrays accept other arrays as index, and logical operations return a tuple containing an array, a3[a3%2==0]                 
                            # it works by getting the new array, using the values within it as indexes to refrence to the main array, then places each value in the new arrays positions. if the second arrays type is boolean, it will match each index of each array and keep the true values referenced to the first array

# slicing (behaviours)
a[1:3:2]


# Operations
a3%2==2                     # returns an array with the same structure, cosnsisting of boolean values
a+d                         # returns an array with each item from array a is summed with the item item with the same index from array b (same shape required) (it has the broadcast effect, which may expand one array and create a new array with a different shape)
                            # e.g: np.ones((3,1)) + np.array([1,3,5])
a+3                         # adds the value (3) to all items within the array

# -------------------------------------------------------------
#endregion


# other python functions:
zip(a, d)


# ipdb.set_trace()




#region Questions
# --------------------------------------------------------------
# Generic Numpy Functions
# how to get a packages version?
# how to get all available data types?
# how to return an empty axis?


# Operations on Arrays
# how to mix two arrays
# how to separate an array into 4 different other arrays
# how to filter the array to get the indexes of certain values within the array?
# adding two arrays? subtracting? multiplying? dividing? power? modulus? square root?
# applying logical operations like and, or, xor ,not?
# replacing values with  positive value for all items? or removing float point?
# getting the array with all values reduced to the nearest integer before them? what about growing to the larger integer? to the nearest integer?
# adding all valueys within an array togather? multiplying all by each other?
# getting the number of items within an array?
# matrix multiplication (multiplying two matrixes)? (2 ways)


# Creating Objects
# Making Arrays:
# how to create an array?
# making an array consisiting of only 1? what about 0?
# making an array with values from a starting number to an ending number, differing by a certain value
# making an array with a certain number of values spreaded evenly within a range
# how to create matrix?
# how to make a not-a-number object? how to make an infinite object
# returning an array of non-duplicate values from another array
# getting the union for two arrays as another arry? intersect? (in 1d)


# Operations done by arrays:
# calculating a functions value? 1*x^2 + 2*x^1 + 5*x^0
# calculating derivation
# calculating integeral


# for random:
# random integer?  (returning an array)
# random number between 0 and 1?
# random selection? (returning an array)

# For Array
# number of dimintions?
# shape of array?
# changing the type?
# changing shape?
# slicing?
# 