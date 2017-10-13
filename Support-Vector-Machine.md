# Support Vector Machine
======================

* **Why it works**: We can afford to shift the line because probability of training point being on boundary is low. 
* Note that the V.C Dimension of the SVM is **dependent** on the dataset, because the constraints are dependent on the dataset.

## Calculating the margin
* This normalization gives a nice formula 

![calc margin](calc-margin.jpeg)

## Minimizing the margin
* Notice that minimizing the margin is "lowering the VC dimension", as was the case in weight decay regularization.
* In general, **Constraints lower VC dimension**

![min margin](min-margin.jpeg)

## Nonlinear Transformations with SVM
* The VC dimension of SVM is more closely related to **the number of support vectors rather than the dimensionality of the space.**
* **So, the cost of nonlinear transformations** is not as drastic

