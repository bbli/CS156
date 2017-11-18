# Practical Considerations
========================

* Feature selection(aka representation) is just as important as chosen algorithm.
* Tip: If your inputs have different ranges, you want to normalize the data so won't be minimizing skewed contours.
* Always shuffle data when training in batches/using for cross validation

## Learning Rate
* Too High-Will jump around, or worse explode for non-convex optimizations
* Too Slow-Just slow convergence

## Regularization
* Too low-Costs may explode
* Too high-will just make weights small and ignore data.

## Epochs
* Too little-final slope still steep

## Cons of Activation Functions
* Sigmoid-Derivative mostly 0, offsets mean
* Tanh-Derivative mostly 0
* RelU-dead neuron problem
