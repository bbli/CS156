# Practical Considerations Theory
---
* Feature selection(aka representation) is just as important as chosen algorithm.
* Tip: If your inputs have different ranges, you want to normalize the data so won't be minimizing skewed contours.
* Always shuffle data when training in batches/using for cross validation

## Hyperparameters
**Learning Rate**
* Too High-Will jump around, or worse explode for non-convex optimizations
* Too Slow-Just slow convergence

**Regularization**
* Too low-Costs may explode
* Too high-will just make weights small and ignore data.

**Epochs**
* Too little-final slope still steep
* Smaller batch size-> more updates in one epoch -> faster convergence time

**Activation Functions**
* Sigmoid-Derivative mostly 0, offsets mean
* Tanh-Derivative mostly 0
* RelU:
    * **Dead neuron problem**-High learning rate -> can make bias term too big -> intermediate values 0 on forward pass -> gradient won't get updated on backward pass
        * So RElU should be paired with Batch Norm, since we have to be conservative with our learning rate when using ReLU

    * **Sparsity**-RElU promote sparsity by having only a limited number of neurons activate for a input.
        * This is similar to biological unit step activation



# Practical Considerations Guidelines
---
## Pre-processing data
* Check for missing data
* **Randomly** Seperate into train, val, and test sets

**Numerics**
* normalize just the training set
* decorrelate the training set
* One hot encode output

**Matching the out of sample distribution**
* Deal with output class imbalence problem
* Resolve input sampling distribution bias
    * change tail/head heavy distributions to more of a bell shape
* Deal with outliers
    * Stay within 3 standard deviations
    * Take log of data
**Transformations/Additions**
* Reduce dimensionality with PCA
* Inject noisy balls into dataset/augment data

## Learning
* Initalize weights to be near 1 with variance 1/number_of_weights(for linear model only though?)--> Research this
* Tensorboard Graphs:
    * Get classification rate
    * cross entropy loss
    * update to current weight ratio 

    * Observation/action histogram(can't do 2d)
    * Reward per episode 
* Save model every 100 epochs or so(into a list or CPickle) 

* Train on simple model to test for overfitting/ whether code is working
* Augment data after training the low level features.
## Validation
To decide learning parameters, look at the corresponding graph
1. Inital Learning Rate

* l2 Regularization Parameter
* At what epoch to stop at
* At what point to turn on adaptive learning rate
* Dropout percentage
* Freeze initial layers when you start to overfit

## Sanity Checks
* Increasing regularization should increase training loss
* You should be able to overfit a small subset of data.
* Remember that each step requires a **new** validation set

## FastAI Gameplan
### Plan
1. find learning rate
2. precompute fit
3. data augment fit
4. fine tune fit(differential learning rates)

### Architecture
* use cos cyclical learning schedule
* set cycle length to 1 epoch 
* set cycle mult to 2(instead of decreasing magnitude)
3. cycle mult

### My additions
* train on unet example dataset
* before adding my hyperparameters, train on base Unet
    * exponentially smooth Nesterov momentum 
    * cylical learning rate

    * dropout layer
    * batchnorm layer
    * I also prefer a bit of stride to promote independence

