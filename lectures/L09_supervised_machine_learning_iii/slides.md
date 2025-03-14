---
title: COMP_SCI 326
separator: <!--s-->
verticalSeparator: <!--v-->
theme: serif
revealOptions:
  transition: 'none'
---

<div class = "col-wrapper">
  <div class="c1 col-centered">
  <div style="font-size: 0.8em; left: 0; width: 70%; position: absolute;">

  # Introduction to Data Science Pipelines
  ## L.09 | Supervised Machine Learning III

  </div>
  </div>
  <div class="c2 col-centered" style = "bottom: 0; right: 0; width: 80%; padding-top: 30%">
  <iframe src="https://lottie.host/embed/bd6c5b65-d724-4f97-882c-40f58367ea38/BIKhZdSeqW.json" height="100%" width = "100%"></iframe>
  </div>
</div>

<!--s-->

<div class = "col-wrapper">
  <div class="c1 col-centered">
  <div style="font-size: 0.8em; left: 0; width: 50%; position: absolute;">

  # Welcome to CS 326.
  ## Please check in by entering the code on the board.

  </div>
  </div>
  <div class="c2" style="width: 50%; height: auto;">
  <iframe src="https://drc-cs-9a3f6.firebaseapp.com/?label=Enter Code" width="100%" height="100%" style="border-radius: 10px;"></iframe>
  </div>
</div>


<!--s-->

## Announcements

- H.03 due on Thursday, 02.06.2025 at 11:59 PM.

- Exam Part I will be on 02.11.2025 at 11:00 AM.
  - The exam will cover all material up to and including L.09.
  - Multiple choice and free response questions (~40 total).
  - LockDown Browser required. There will be a **graded** practice exam due before the exam.

<!--s-->

<div class="header-slide">

# L.09 | Supervised Machine Learning III

</div>

<!--s-->

<div class = "col-wrapper">
  <div class="c1 col-centered">
    <div style="font-size: 0.8em; left: 0; width: 60%; position: absolute;">

  # Intro Poll
  ## On a scale of 1-5, how confident are you with the following methods:

  1. Decision Trees
  2. Ensemble Models

  </div>
  </div>
  <div class="c2" style="width: 50%; height: 100%;">
  <iframe src="https://drc-cs-9a3f6.firebaseapp.com/?label=Intro Poll" width="100%" height="100%" style="border-radius: 10px"></iframe>
  </div>

</div>

<!--s-->

<div class="header-slide">

# Decision Trees

</div>

<!--s-->

## Decision Trees | Overview

**Decision Trees** are a non-parametric supervised learning method used for classification and regression tasks. They are simple to **understand** and **interpret**, making them a popular choice in machine learning.

A decision tree is a tree-like structure where each internal node represents a feature or attribute, each branch represents a decision rule, and each leaf node represents the outcome of the decision.

<img src="https://media.geeksforgeeks.org/wp-content/uploads/20220831135057/CARTClassificationAndRegressionTree.jpg" height="50%" style="margin: 0 auto; display: block;">
<p style="text-align: center; font-size: 0.6em; color: grey;">Geeksforgeeks, 2024</p>

<!--s-->

## Decision Trees | ID3 Algorithm

The construction of a decision tree involves selecting the best feature to split the dataset at each node. One of the simplest algorithms for constructing categorical decision trees is the ID3 algorithm.

**ID3 Algorithm (Categorical Data)**:

1. Calculate the entropy of the target variable.
2. For each feature, calculate the information gained by splitting the data.
3. Select the feature with the highest information gain as the new node.

The ID3 algorithm recursively builds the decision tree by selecting the best feature to split the data at each node.

<img src="https://media.geeksforgeeks.org/wp-content/uploads/20220831135057/CARTClassificationAndRegressionTree.jpg" height="40%" style="margin: 0 auto; display: block;">
<p style="text-align: center; font-size: 0.6em; color: grey;">Geeksforgeeks, 2024</p>

<!--s-->

## Decision Trees | Entropy

**Entropy** is a measure of the impurity or disorder in a dataset. The entropy of a dataset is 0 when all instances belong to the same class and is maximized when the instances are evenly distributed across all classes. Entropy is defined as: 

$$ H(S) = - \sum_{i=1}^{n} p_i \log_2(p_i) $$

Where:

- $H(S)$ is the entropy of the dataset $S$.
- $p_i$ is the proportion of instances in class $i$ in the dataset.
- $n$ is the number of classes in the dataset.

<img src="https://miro.medium.com/v2/resize:fit:565/1*M15RZMSk8nGEyOnD8haF-A.png" width="40%" style="margin: 0 auto; display: block;">
<p style="text-align: center; font-size: 0.6em; color: grey;">Provost, Foster; Fawcett, Tom. </p>

<!--s-->

## Decision Trees | Information Gain

**Information Gain** is a measure of the reduction in entropy achieved by splitting the dataset on a particular feature. IG is the difference between the entropy of the parent dataset and the weighted sum of the entropies of the child datasets.

$$ IG(S, A) = H(S) - H(S|A)$$

Where:

- $IG(S, A)$ is the information gain of splitting the dataset $S$ on feature $A$.
- $H(S)$ is the entropy of the parent dataset.
- $H(S | A)$ is the weighted sum of the entropies of the child datasets.


<br><br>
<img src="https://miro.medium.com/max/954/0*EfweHd4gB5j6tbsS.png" width="50%" style="margin: 0 auto; display: block;">
<p style="text-align: center; font-size: 0.6em; color: grey;">KDNuggets</p>


<!--s-->

## Decision Trees | ID3 Pseudo-Code

```text
ID3 Algorithm:
1. If all instances in the dataset belong to the same class, return a leaf node with that class.
2. If the dataset is empty, return a leaf node with the most common class in the parent dataset.
3. Calculate the entropy of the dataset.
4. For each feature, calculate the information gain by splitting the dataset.
5. Select the feature with the highest information gain as the new node.
6. Recursively apply the ID3 algorithm to the child datasets.
```

Please note, ID3 works for **categorical** data. For **continuous** data, we can use the C4.5 algorithm, which is an extension of ID3 that supports continuous data.

<img src="https://media.geeksforgeeks.org/wp-content/uploads/20220831135057/CARTClassificationAndRegressionTree.jpg" height="50%" style="margin: 0 auto; display: block;">
<p style="text-align: center; font-size: 0.6em; color: grey;">Geeksforgeeks, 2024</p>

<!--s-->

## Decision Trees | How to Split Continuous Data

For the curious, here is a simple approach to split continuous data with a decision tree. ID3 won't do this out of the box, but C4.5 does have an implementation for it.

1. Sort the dataset by the feature value.
2. Calculate the information gain for each split point.
3. Select the split point with the highest information gain as the new node.

```text
Given the following continuous feature:

    [0.7, 0.3, 0.4]

First you sort it: 

    [0.3, 0.4, 0.7]

Then you evaluate information gain for your target variable at every split:

    [0.3 | 0.4 , 0.7]

    [0.3, 0.4 | 0.7]
```

<!--s-->

## Decision Trees | Overfitting

**Overfitting** is a common issue with decision trees, where the model captures noise in the training data rather than the underlying patterns. Overfitting can lead to poor **generalization** performance on unseen data.

<img src="https://gregorygundersen.com/image/linoverfit/spline.png" height="50%" style="margin: 0 auto; display: block; border-radius: 10px;">
<p style="text-align: center; font-size: 0.6em; color: grey;">Gunderson 2020</p>


<!--s-->

## Decision Trees | Overfitting

**Overfitting** is a common issue with decision trees, where the model captures noise in the training data rather than the underlying patterns. Overfitting can lead to poor **generalization** performance on unseen data.

**Strategies to Prevent Overfitting in Decision Trees**:

1. **Pruning**: Remove branches that do not improve the model's performance on the validation data.
    - This is similar to L1 regularization in linear models!
2. **Minimum Samples per Leaf**: Set a minimum number of samples required to split a node.
3. **Maximum Depth**: Limit the depth of the decision tree.
4. **Maximum Features**: Limit the number of features considered for splitting.

<!--s-->


## Decision Trees | Pruning

**Pruning** is a technique used to reduce the size of a decision tree by removing branches that do not improve the model's performance on the validation data. Pruning helps prevent overfitting and improves the generalization performance of the model.

Practically, this is often done by growing the tree to its maximum size and then remove branches that do not improve the model's performance on the validation data. A loss function is used to evaluate the performance of the model on the validation data, and branches that do not improve the loss are pruned: 

$$ L(T) = \sum_{t=1}^{T} L(y_t, \widehat{y}_t) + \alpha |T| $$

Where:

- $L(T)$ is the loss function of the decision tree $T$.
- $L(y_t, \widehat{y}_t)$ is the loss function of the prediction $y_t$.
- $\alpha$ is the regularization parameter.
- $|T|$ is the number of nodes in the decision tree.


<!--s-->

## Decision Tree Algorithm Comparisons

| Algorithm | Data Types | Splitting Criteria |
|-----------|------------|--------------------|
| ID3       | Categorical | Entropy & Information Gain    |
| C4.5      | Categorical & Continuous | Entropy & Information Gain |
| CART      | Categorical & Continuous | Gini Impurity |


<!--s-->

## L.09 | Q.01

Which of the following decision tree algorithms is a reasonable choice for continuous data?

<div class='col-wrapper' style = 'display: flex; align-items: top; margin-top: 2em; margin-left: -1em;'>
<div class='c1' style = 'width: 60%; display: flex; align-items: center; flex-direction: column; margin-top: 2em'>
<div style = 'line-height: 2em;'>
&emsp;A. ID3 <br>
&emsp;**B. C4.5 **<br>
</div>
</div>
<div class='c2' style = 'width: 40%; display: flex; align-items: center; flex-direction: column;'>
<iframe src="https://drc-cs-9a3f6.firebaseapp.com/?label=L.09 | Q.01" width="100%" height="100%" style="border-radius: 10px"></iframe>
</div>
</div>

<!--s-->

<div class="header-slide">

# Ensemble Models

</div>

<!--s-->

## Ensemble Models | Overview

**Ensemble Models** combine multiple individual models to improve predictive performance. The key idea behind ensemble models is that a group of weak learners can come together to form a strong learner. Ensemble models are widely used in practice due to their ability to reduce overfitting and improve generalization.

We will discuss three types of ensemble models:

1. **Bagging**: Bootstrap Aggregating
2. **Boosting**: Sequential Training
3. **Stacking**: Meta-Learning

<!--s-->

## Ensemble Models | Bagging

**Bagging (Bootstrap Aggregating)** is an ensemble method that involves training multiple models on different subsets of the training data and aggregating their predictions. The key idea behind bagging is to reduce variance by averaging the predictions of multiple models.

**Intuition**: By training multiple models on different subsets of the data, bagging reduces the impact of outliers and noise in the training data. The final prediction is obtained by averaging the predictions of all models.

<img src="https://media.geeksforgeeks.org/wp-content/uploads/20230731175958/Bagging-classifier.png" width="50%" style="margin: 0 auto; display: block;">
<p style="text-align: center; font-size: 0.6em; color: grey;">Geeksforgeeks</p>

<!--s-->

## Ensemble Models | Bagging | Example: Random Forests

**Random Forests** are an ensemble learning method that combines multiple decision trees to create a more robust and accurate model. Random Forests use bagging to train multiple decision trees on different subsets of the data and aggregate their predictions.

**Key Features of Random Forests**:
- Each decision tree is trained on a random subset of the features.
- The final prediction is obtained by averaging the predictions of all decision trees.

Random Forests are widely used in practice due to their robustness, scalability, and ability to handle high-dimensional data.

<img src="https://tikz.net/janosh/random-forest.png" height="40%" style="margin: 0 auto; display: block; padding: 10">
<p style="text-align: center; font-size: 0.6em; color: grey;">Geeksforgeeks</p>

<!--s-->

## Ensemble Models | Boosting

**Boosting** is an ensemble method that involves training multiple models sequentially, where each model learns from the errors of its predecessor.

**Intuition**: By focusing on the misclassified instances in each iteration, boosting aims to improve the overall performance of the model. The final prediction is obtained by combining the predictions of all models.

<img src="https://media.geeksforgeeks.org/wp-content/uploads/20210707140911/Boosting.png" width="50%" style="margin: 0 auto; display: block;">
<p style="text-align: center; font-size: 0.6em; color: grey;">Geeksforgeeks</p>

<!--s-->

## Ensemble Models | Boosting | Example: AdaBoost

**AdaBoost (Adaptive Boosting)** is a popular boosting algorithm. AdaBoost works by assigning weights to each instance in the training data and adjusting the weights based on the performance of the model.

**Key Features of AdaBoost**:

1. Train a weak learner on the training data.
2. Increase the weights of misclassified instances.
3. Train the next weak learner on the updated weights.
4. Repeat the process until a stopping criterion is met.

<img src="https://media.geeksforgeeks.org/wp-content/uploads/20210707140911/Boosting.png" width="50%" style="margin: 0 auto; display: block;">
<p style="text-align: center; font-size: 0.6em; color: grey;">Geeksforgeeks</p>

<!--s-->

## Ensemble Models | Boosting | Example: Gradient Boosting

**Gradient Boosting** is another popular boosting algorithm. Gradient Boosting works by fitting a sequence of weak learners to the residuals of the previous model. This differs from AdaBoost, which focuses on the misclassified instances. A popular implementation of Gradient Boosting is **XGBoost** (❤️).

**Key Features of Gradient Boosting**:

1. Fit a weak learner to the training data.
2. Compute the residuals of the model.
3. Fit the next weak learner to the residuals.
4. Repeat the process until a stopping criterion is met.

<img src="https://media.geeksforgeeks.org/wp-content/uploads/20200721214745/gradientboosting.PNG" width="50%" style="margin: 0 auto; display: block;">
<p style="text-align: center; font-size: 0.6em; color: grey;">Geeksforgeeks</p>

<!--s-->

## Ensemble Models | Stacking

**Stacking (Stacked Generalization)** is an ensemble method that combines multiple models using a meta-learner. The key idea behind stacking is to train multiple base models on the training data and use their predictions as input to a meta-learner.

**Intuition**: By combining the predictions of multiple models, stacking aims to improve the overall performance of the model. The final prediction is obtained by training a meta-learner on the predictions of the base models.

<img src="https://miro.medium.com/v2/resize:fit:946/1*T-JHq4AK3dyRNi7gpn9-Xw.png" height="50%" style="margin: 0 auto; display: block; border-radius: 10px;">
<p style="text-align: center; font-size: 0.6em; color: grey;">Setunga, 2020</p

<!--s-->

## Ensemble Models | Stacking | Example

**Stacked Generalization** involves training multiple base models on the training data and using their predictions as input to a meta-learner. The meta-learner is trained on the predictions of the base models to make the final prediction.

**Key Features of Stacked Generalization**:

1. Train multiple base models on the training data.
2. Use the predictions of the base models as input to the meta-learner.
3. Train the meta-learner on the predictions of the base models.
4. Use the meta-learner to make the final prediction.

Stacking is often trained end-to-end, where the base models and meta-learner are trained simultaneously to optimize the overall performance.

<img src="https://miro.medium.com/v2/resize:fit:946/1*T-JHq4AK3dyRNi7gpn9-Xw.png" height="30%" style="margin: 0 auto; display: block;">
<p style="text-align: center; font-size: 0.6em; color: grey;">Setunga, 2020</p

<!--s-->

## L.09 | Q.02

Let's say that you train a sequence of models that learn from the mistakes of the predecessors. Instead of focusing on the misclassified instances (and weighting them more highly), you focus on improving the residuals. What algorithm is this most similar to?

<div class='col-wrapper' style = 'display: flex; align-items: top; margin-top: 2em; margin-left: -1em;'>
<div class='c1' style = 'width: 60%; display: flex; align-items: center; flex-direction: column; margin-top: 2em'>
<div style = 'line-height: 2em;'>
A. Bagging (e.g. Random Forest) <br>
B. Boosting (e.g. Adaboost) <br>
C. **Boosting (e.g. Gradient Boosting)** <br>
D. Stacking
</div>
</div>
<div class='c2' style = 'width: 40%;'>
<iframe src="https://drc-cs-9a3f6.firebaseapp.com/?label=L.09 | Q.02" width="100%" height="100%" style="border-radius: 10px"></iframe>
</div>
</div>
<!--s-->

## Summary

In this lecture, we explored two fundamental concepts in supervised machine learning:

1. **Decision Trees**:
    - A non-parametric supervised learning method used for classification and regression tasks.
    - Can be constructed using the ID3 algorithm based on entropy and information gain.
    - Prone to overfitting, which can be mitigated using pruning and other strategies.

2. **Ensemble Models**:
    - Combine multiple individual models to improve predictive performance.
    - Include bagging, boosting, and stacking as popular ensemble methods.
    - Reduce overfitting and improve generalization by combining multiple models.

<!--s-->

<div class = "col-wrapper">
  <div class="c1 col-centered">
    <div style="font-size: 0.8em; left: 0; width: 60%; position: absolute;">

  # Exit Poll
  ## On a scale of 1-5, how confident are you with the following methods:

  1. Decision Trees
  2. Ensemble Models

  </div>
  </div>
  <div class="c2" style="width: 50%; height: 100%;">
  <iframe src="https://drc-cs-9a3f6.firebaseapp.com/?label=Exit Poll" width="100%" height="100%" style="border-radius: 10px"></iframe>
  </div>

</div>

<!--s-->

<div class = "col-wrapper">
  <div class="c1 col-centered">
  <div style="font-size: 1em; left: 0; width: 60%; position: absolute;">

  # H.03 | machine_learning.py
  ## Code & Free Response

  ### Due Thursday, 02.06.2025 at 11:59 PM.

```bash
cd <class directory>
git pull
```

</div>
</div>
<div class="c2 col-centered" style = "bottom: 0; right: 0; width: 100%; padding-top: 0%; margin: 10px;">
<iframe src="https://lottie.host/embed/6c677caa-d54a-411c-b0c0-6f186378d571/UKVVhf0EJN.json" height = "100%" width = "100%"></iframe>

</div>
</div>

<!--s-->