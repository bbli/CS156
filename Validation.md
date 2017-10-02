# Validation
==========

## Validation Tradeoff Mental Model
* $E_{out}(g^-)$ as Good Estimator for $E_{out}(g)$
* $E_{val}(g^-)$ as Good Estimate of Estimator

![testing tradeoff](testing-tradeoff.jpeg)

* We return the "full hypothesis" because we care more about the model than a prediction of the error

## Full Protocol with Cross Validation
* Note that this procedure will cause optimistic bias in the error, due to the error being a "weird" function of many random variables.

![full protocol](full-protocol.jpeg)
