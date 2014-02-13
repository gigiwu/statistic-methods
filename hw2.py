#!/usr/bin/python

import sys
import math
import heapq
import numpy as np
import pylab as p

def numpy_result(data):
    print '=== numpy results ==='
    print 'mean : %f' % np.mean(data)
    print 'variance : %f' % np.var(data)
    print 'std deviation : %f' % np.std(data)
    print 'median : %f' % np.median(data)

def my_mean(data):
    s = sum(data)
    n = len(data)
    return s/n

def my_variance(data):
    n = len(data)
    mean = my_mean(data)
    sq_sum = 0
    for d in data:
	sq_sum += (d*d)
    return ((sq_sum/n) - (mean*mean))

def my_std(data):
    variance = my_variance(data)
    return math.sqrt(variance)

def my_median(data): 
    n = len(data)
    sorted_data = sorted(data)
    if n%2 == 0:
	return (sorted_data[n/2] + sorted_data[n/2 -1]) / 2
    else:
	return sorted_data[n/2]

def my_cdf(data):
    data.sort()
    n = len(data)
    y = []
    for i in range(n):
	y.append((float(i)+1)/n)

    p.step(data, y)
    p.title('CDF')
    p.show()        
    pass

def my_ccdf(data):
    # in-place sort
    data.sort()
    n = len(data)
    y = []
    for i in range(n):
	y.append(1-(float(i)+1)/n)
    p.step(data, y)
    p.ylabel('ccdf(x)')
    p.xlabel('x')
    p.title('CCDF')
    p.show()        
    pass

with open(sys.argv[1],'r+') as f :
    #read data by each line
    data = f.readlines()
    #convert to float
    data = [float(d) for d in data]

    if sys.argv[2] == 'numpy':
	numpy_result(data)
        print '-------------'
    elif sys.argv[2] == 'my' :
	print '=== my methods ==='
	mean = my_mean(data)
	print 'mean : %f' % mean 
	variance = my_variance(data)
	print 'variance : %f' % variance
	sd = my_std(data)
	print 'standard deviation : %f' % sd
	median = my_median(data)
	print 'median : %f' % median
    elif sys.argv[2] == 'ccdf':
	my_ccdf(data)

    elif sys.argv[2] == 'cdf':
	my_cdf(data)


