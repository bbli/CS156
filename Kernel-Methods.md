# Kernel Methods
==============

## Main Ideas
* Representation of weight vetor
* Why Slack is Better than Regression
    * Because there is **discreteness** in slack: it doesn't punish everything, just the **misclassifications**
* Formulation of Soft Margin SVM
    * 
* Normalization Generalization
    * **lazy conditon**: we don't know the normalization we solve the problem

> Q: Why is slack better than regression for classification? After all, it also involves the use of calculus
> A: Because there is **discreteness** in slack: it doesn't punish everything, just the **misclassifications**

## Kernel Formulation of SVM
In general, we applying a nonlinear transformation, two things change: the final hypothesis and the error function, because these are the objects that depend on the dataset.
* **Hypothesis**

![SVM hypothesis](kernel-SVM-hypothesis.PNG)

* **Lagrangian(aka Error function)**

![SVM lagrangian](kernel-SVM-Lagrangian.PNG)

## Normalization for SVM with soft margins
> Q: Why does the cost function not change?
> A: Because the normalization hasn't changed!

> Q: How is it that the soft margin SVM can seperate out points and maximize the margin at the same time? 
> By turning the classification error into a slack error. Namely, a bad seperation will have large slack variables, and the algorithm by default wants to minimize these.

* The inequality will **only hold if support vectors have norm 1.** As it turn out, when minimizing the cost function they do.
![slack](slack.jpeg)

## Key Black Boxes Learned from this Chapter
* Inequality allows us to solve for $x_{support}$ and margin **at the same time**.
![key tech](soft-margin-techs.jpeg)

