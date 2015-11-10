import numpy as np
from random import *
import DataProcessing
data_size = 303

def perceptron(data, attr, target_attr):
    ''' 
    Implementation of the Perceptron Learning Algorithm
    '''
	#initial random weight matrix
	w = np.matrix([randint(-1, 1) for i in range(len(attr))])
	converged = 0
	max_iter = 1000
	count = 0
	while not converged and count < max_iter:	
		print("trial:", count)
		r, c = data.shape
		output = [data.item(i, target_attr) for i in [j for j in range(r) if j != target_attr]]	#output matrix
		#data[0] 
		misclassified = []
		for row in range(0, data_size):
			record = [1]
			record.extend([data.item(row, i) for i in range(len(attr) - 1)])
			record = np.matrix(record)
			y = data.item(row, target_attr)

            #wx is a linear function of the weights and input
			wx = w * record.transpose()
			
            #hypothesis, h is true if wx is positive, else it is false
			if wx >= 0:
				h = 1
			else:
				h = 0

	        #if hpyothesis and target labels don't match, then the example has been misclassified
			if h != y:
				misclassified.append(row)

		if len(misclassified) != 0:
			#pick random misclassified point
			point = choice(misclassified)
			record = [data.item(point, i) for i in range(len(attr))]
			w = w + np.matrix(record[target_attr]) * np.matrix(record[0:len(attr)])
			count += 1
		else:
            #no misclassifications, Perceptron has attained convergence
			converged = 1

	if not converged:
		print("No convergence")
	
if __name__ == "__main__":
    data = np.matrix(DataProcessing.process("data.txt","processedData.txt"))
    perceptron(data, range(14), 13) 	
