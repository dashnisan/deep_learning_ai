# (Deep) Neural Network  with Vectorized Gradient Descent

Here you can find a self implemented neural network algorithm for binary classification. It uses gradient descent for optimization. The criterion for stopping optimization is the number of iterations, set to 2200.

The code allows to train as many different neural networks as desired with different amount of layers and units in each layer. All hidden layers use ReLU as activation function and the output layer a sigmoid for the calculation of the probabilities of positive predictions.

The models are trained with 64x64 pixel pictures to recognize whether a picture contains the image of a cat (the animal) or not. The same dataset was used for the binary classification using logistic regression.

Three models are trained:
<ol>
<li>2-layer NN with 5 hidden units. F1-score of 0.81 on the test set. </li>
<li>4-layer NN with 20, 7, 5 units in the respective hidden layers: Best model with F1-score of 0.86 on the test set</li>
<li>7-layer NN with 80, 60, 40, 20, 10, 5 units in the respective hidden layers: Worst model with F1-score of 0.70 on the test set</li>
</ol>

The shallower models give better results than the deepest of the three. The 7-layer model performs even worse than the other two on the training set, which means higher bias. This model has similar performance to the logistic regression performed in the first exercise. This shows that just increasing complexity does not necessary leads to better results. This phenomenon can be understood and addressed with hyperparameter tuning and best practices like use of train/development/test sets. This we will address in a coming exercise.

Concerning the false positives (precision score) and false negatives (recall score), the shallower models are balanced. The best model tends to produce more false positives than false negatives (see the screenshots).


 
## Files and Folders:
<ul>
<li>dnn_grad_desc: executable for Linux for deep neural networks with specified depth</li>
<li>_internal: directory with other necessary files for execution</li>
</ul>
