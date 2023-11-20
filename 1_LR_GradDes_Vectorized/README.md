# Logistic Regression with Vectorized Gradient Descent
Here you can find a self implemented logistic regression algorithm using gradient descent. 

It was trained with 64x64 pixel pictures to recognize whether a picture contains the image of a cat (the animal) or not.

This exercise is used to formulate the math as a a basis for more complex algorithms like shallow neural networks. All the equations, forward and backward propagation are vectorized so the algorithm is fast.

The scores of the algorithm show that it overfits on the training set and has a not as good  performance on the test set. The recall score is the lowest (~0.7), meaning the system generates false negatives in 30% of the cases. False positives (precision score) happen about 18% of the cases. The overall f1-score of 75% is fair.
 
## Files and Folders:
<ul>
<li>logistic_regression: executable for Linux</li>
<li>\_internal: directory with other necessary files for execution</li>
</ul>
