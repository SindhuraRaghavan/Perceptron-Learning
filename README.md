#Perceptron Learning Algorithm

##Implementation
```
The Perceptron Learning Algorithm (PLA) is a supervised ML algorithm
It is a linear classifier of data points (x,y) where x is the input features and y is the label/classification class

The goal of training is to determine the model parameter w given the training data of input parameters and target labels

For all training samples (x,y):
    h(x) = w' * x
    If h(x) >= threshold, then h = 1; Else h = 0
    If h = y, classify x; Else, misclassify x

Do until there are misclassified data points or maximum number of iterations:
    Pick a random misclassified point
    Update w <- w + y * x

w after convergence or maximum number of iterations is the model parameter learnt during the training process
```

##Dataset
```
More about the Dataset : cleve_heart_disease.txt
* The complete dataset consists of 76 attributes
* We are interested in only 14 attributes of the 76 - Age, Sex, Chest pain type, Resting blood pressure, Cholesteral level, Fasting blood sugar, Resting ECG, Maximum heart rate, Angina, Oldpeak, Slope, Colored vessels, Thal, Healthy/sick* We discretize the input attributes 
* We discretize the attributes in the dataset as follows:

 +----------------------------+-------+---------+-------------------+---------+--------+
 |                            |   0   |    1    |      2            |    3    |   4    |
 |----------------------------|-------|---------|-------------------|---------|--------| 
 | 1. Age                     |       |   < 45  |  >= 45 and <= 65  |  > 65   |		   |
 | 2. Sex                     |       |  male   |      female       |         |		   |
 | 3. Chest Pain type         |       | angina  |      abnang       |  notang | others |
 | 4. Restin BP               |       | <= 120  |  > 120 and < 140  |  > 140  |   	   |
 | 5. Cholesteral             |       | <= 200  |  > 200 and <= 240 |  > 240  |        |
 | 6. Fasting Blood Sugar     | false |  true   |                   |         |        |
 | 7. Resting ECG             |       |  norm   |       abn         |  others |		   |
 | 8. Heart rate              |       |  < 60   | >= 60 and < 100   |  others |		   |
 | 9. Exercise induced angina | false |  true   |                   |         | 	   |
 | 10. Oldpeak                |       |  < 1.5  | >= 1.5 and < 2.55 | >= 2.55 |		   |
 | 11. Slope                  |       |    up   |       flat        |  others | 	   |
 | 12. Colored vessels        |       |   <=1   |    > 1 and <= 2   |  others |		   |
 | 13. Thal                   |       |  norm   |       fixed       |  others |		   |
 | 14. Healthy/Sick           |   H   |  others |                   |         |		   |
 +----------------------------+-------+---------+-------------------+---------+--------+							
```
