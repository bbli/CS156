# Overfitting
===========

* Overfitting is when using a **more complex model leads to worse result**
## Overfitting Mental Model
* Dataset Size
	* Most important: with enough data, the other factors are negligible.
	* **Machine learning is achieving the best fit given the data resources. It is not achieving the best fit.**
* Noise Level
* Target Complexity
![overfit](overfitting-factors.PNG)

## Regularizer Key Point
* Regularization reduces variance at expense of increasing bias a bit
* reduces complexity
* smaller weights means "wider" functions (5x^2 vs 0.01x^2) -> Punishes noise
* weight decay = (1-2*lambda*learning rate/number_of_datapoints)

![regularizer](regularizer.jpeg)

## 3 Regularizers Examples

![reg example](reg-examples.jpeg)
