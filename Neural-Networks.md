# Neural Networks
===============

## Stochastic Gradient Descent
* Used when function is a sum of functions(which for us, means a sum of datapoints)
* Randomness is good for avoiding shallow wells
![sgd](sgd.PNG)

## Logic Gates with Perceptons
> We can create complicated models by feeding the binary outputs of perceptons into more perceptons, and change the weights to get the operaton we want.

* AND/OR can be implemented by changing the constant weight vector of a 3 dimensional percepton
* Negatives can be implement by chaning the input weight vectors of a 3 dimensional percepton

![logic gates](logic-gates.PNG)

## Transition to Neural Network
1. Replace percepton node by tanh(s) nodes
* Allow weight to vary
* More than just 3 inputs into each node

![neural net](neural-net.jpeg)


## Compiling the gradient: Backpropagation Algorithm. 
* Calculating the analytic error function is hard
* We don't want to numerically calculate the gradient after every step.
* **Algorithm**:
	1. Express in terms of $s^l_{j}$
	* Calculate $\delta$ for last layer
	* Backpropagate delta

![e weight](e-weight.jpeg)

![backprop](backpropagation.jpeg)

![back-formula](back-formula.PNG)
