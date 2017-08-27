# Improving the Union Bound
=========================

* Remember, the union bound is needed because we don't know which one of the hypotheses will have to track $E_{out}$, even thought we just need to final hypothesis to track $E_{out}$
## Reduce to Finite
---
* **Equivalence Class**: If two different hypotheses return the same output on the training data, then they are consider "equivalent"
$$M\rightarrow 2^{N}$$
![dichotomies](dichotomies.PNG)

## Reduce to Polynomial
---
#### Growth Function
![growth](growth-function.PNG)
$$2^{N}\rightarrow m_{H}(N)$$

#### BreakPoint
* The Breakpoint for better models is as expected higher. But this means that the Hoeffding inequality will be weaker.
	* **The stronger the model, the less you will be able to learn.**
![break](break.PNG)

$$m_H(N)\rightarrow polynomial$$

