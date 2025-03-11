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
  ## L.16 | Exam Part II Review

  </div>
  </div>
  <div class="c2 col-centered" style = "bottom: 0; right: 0; width: 80%; padding-top: 30%">
  <iframe src="https://lottie.host/embed/bd6c5b65-d724-4f97-882c-40f58367ea38/BIKhZdSeqW.json" height="100%" width = "100%"></iframe>
  </div>
</div>

<!--s-->

<div class="header-slide">

# L.16 | Exam Part II  Review

</div>

<!--s-->

## Announcements

- Exam Part II will take place on Thursday at 11A.

- Office hours from 1-2P today in Mudd. 

- [CTECs are open](https://canvas.northwestern.edu/courses/226962/external_tools/8871)! Please take a moment to fill them out.

<!--s-->

# Lockdown Browser (Canvas)

1. [Download Lockdown Browser](https://download.respondus.com/lockdown/download7.php?id=171646780).
2. Install the browser on your computer.
3. Ensure that you can log in to your Northwestern University Canvas account using the browser.

**Note**: I have enabled the Monitoring feature for students that are unable to join us in-person, but I ask that everyone use it to ensure a fair testing environment.

<!--s-->

<div class = "col-wrapper">
  <div class="c1 col-centered">
    <div style="font-size: 0.8em; left: 0; width: 60%; position: absolute;">

  # Intro Poll
  ## On a scale of 1-5, how confident are you feeling about Exam Part II?

  </div>
  </div>
  <div class="c2" style="width: 50%; height: 100%;">
  <iframe src="https://drc-cs-9a3f6.firebaseapp.com/?label=Intro Poll" width="100%" height="100%" style="border-radius: 10px"></iframe>
  </div>

</div>

<!--s-->

<div class="header-slide">

# Exam Part II Review

</div>

<!--s-->

## Exam Part II

You will **not** be expected to do any programming on the exam. You will be asked to interpret code, identify errors, and explain concepts. The exam will be **closed book** and **closed notes**. You will not be allowed to use any resources during the exam. You will not need a calculator.

The following topics will likely be covered on the exam -- they are not exhaustive but should give you a good idea of what to expect. Anything talked about in lecture or on your homework is fair game. 

The exam is approximately 60/40 in point value between Part I and Part II and of the course. There are ~ 50 questions written as of today.

<!--s-->

# L.02 | Data Sources

[[slides]](https://drc-cs.github.io/WINTER25-CS326/lectures/L02_data_sources/#/)

- Be able to identify structured, semi-structured, and unstructured data, as well as the advantages and disadvantages of each.

- Given a scenario with missing data, pick the appropriate method to handle it.

- Be able to describe several methods for identifying outliers in a dataset.

<!--s-->

# H.01 | Hello World

[[homework]](https://github.com/drc-cs/WINTER25-CS326/tree/main/homeworks/H01)

- Understand the roles of conda, GitHub, vscode, and pytest in your development workflow.

<!--s-->

# L.03 | Exploratory Data Analysis

[[slides]](https://drc-cs.github.io/WINTER25-CS326/lectures/L03_eda/#/)

- Understand central tendency (mean, median, mode) and spread (range, variance, standard deviation).

- Identify skew (positive, negative).

- Know key properties of a normal distribution.

<!--s-->

# L.04 | Correlation

[[slides]](https://drc-cs.github.io/WINTER25-CS326/lectures/L04_correlation_association/#/)

- Differentiate when to use Pearson vs Spearman correlation.

- Interpret correlation results (negative / positive / no relationship).

- Identify a scenario as Simpson's Paradox (or not).

- Recall Support, Confidence, and Lift and how they are used in association rule mining.

<!--s-->

# L.05 & H.02 | Hypothesis Testing

[[slides]](https://drc-cs.github.io/WINTER25-CS326/lectures/L05_hypothesis_testing/#/)
[[homework]](https://github.com/drc-cs/WINTER25-CS326/tree/main/homeworks/H02)

- Construct an A/B Test to test a hypothesis.

- Define hypothesis testing for a scenario in terms of $H_0$ and $H_1$.

- Provided a scenario, identify the hypothesis test to use (t-test, paired t-test, chi-squared test, anova).

- Understand what a p-value represents, how it is used in hypothesis testing, and how to interpret it.

- Know the non-parametric analogs to the tests we covered in lecture.

<!--s-->

# L.06 | Data Preprocessing

[[slides]](https://drc-cs.github.io/WINTER25-CS326/lectures/L06_data_preprocessing/#/)

- Define feature engineering in the context of machine learning applications.

- Define and be able to identify data that has been scaled and the method used to scale it (min-max, standard).

- Describe the curse of dimensionality and how it affects machine learning models.

- Understand dimensionality reduction techniques (Feature Selection, Feature Sampling, or PCA).

<!--s-->

# L.07 | Machine Learning I

[[slides]](https://drc-cs.github.io/WINTER25-CS326/lectures/L07_supervised_machine_learning_i/#/)

- Define the terms: training set, validation set, and test set and their primary uses.

- Identify a scenario as a classification or regression problem.

- Explain the KNN algorithm and how it works.

- Explain where the normal equation for linear regression comes from.

- Be able to identify L1 and L2 regularization and explain at a high level how they work.

- Understand the intuition behind the cross-entropy loss function.

- Know that logistic regression is just a linear regression model with a sigmoid function applied to the output.

<!--s-->

# H.03 | Machine Learning

[[homework]](https://github.com/drc-cs/WINTER25-CS326/tree/main/homeworks/H03)

- Be able to look at code for logistic regression gradient descent and identify missing or incorrect components.

- Provided with a **simple** numpy operation, identify the shape of the output. This may include an axis argument. [[🔗]](https://numpy.org/doc/stable/user/basics.broadcasting.html)

<!--s-->

# L.08 | Machine Learning II

[[slides]](https://drc-cs.github.io/WINTER25-CS326/lectures/L08_supervised_machine_learning_ii/#/)

- Explain ROC curves (axes) and what the AUC represents.

- Explain the value of k-fold cross-validation.

- Explain the value of a softmax function in the context of a multi-class classification problem.

<!--s-->

# L.09 | Machine Learning III

[[slides]](https://drc-cs.github.io/WINTER25-CS326/lectures/L09_supervised_machine_learning_iii/#/)

- Explain the ID3 algorithm and how it works (understand entropy & information gain).

- Be able to identify a decision tree model as overfitting or underfitting.

- Differentiate between and be able to explain different ensemble modeling methods (bagging, boosting, stacking).

<!--s-->

# L.10 & H.04 | Clustering

[[slides]](https://drc-cs.github.io/WINTER25-CS326/lectures/L10_clustering/#/)
[[homework]](https://github.com/drc-cs/WINTER25-CS326/tree/main/homeworks/H04)

- Understand the k-means algorithm.

- Be able to look at an elbow plot or silhouette score and identify the optimal number of clusters for k-means.

- Understand agglomerative (bottom-up) clustering, and be able to identify different linkage patterns.

- Understand the difference between hierarchical and partitioning clustering.

- Describe DBScan in the context of $\epsilon$ and $\text(m)$.

<!--s-->

# L.11 | Recommendation Systems

[[slides]](https://drc-cs.github.io/WINTER25-CS326/lectures/L11_recommendation_modeling/#/)

- Differentiate between content and collaborative filtering.

- Understand User-User vs Item-Item collaborative filtering in a User-Item Matrix.

- Understand the intuition behind matrix factorization in collaborative filtering.

<!--s-->

# L.12 | Time Series

[[slides]](https://drc-cs.github.io/WINTER25-CS326/lectures/L12_time_series/#/)
[[homework]](https://github.com/drc-cs/WINTER25-CS326/tree/main/homeworks/H05)

- Identify additive vs multiplicative decomposition in time series data.

- Know the value of differencing in time series data (i.e. what does it do, why is that important, and how do we evaluate the number of differences).

- Look at ACF / PACF plots and determine what order of AR or MA to use in an ARIMA model.

- Explain walk-forward validation in the context of time series data.

<!--s-->

# L.13 | Natural Language Processing I

[[slides]](https://drc-cs.github.io/WINTER25-CS326/lectures/L13_nlp_I/#/)

- Explain TF-IDF and how it is used in text analysis.

- Define a bag-of-words model and explain how it is used in text analysis.

- Explain the intuition behind a Markov model and how it is used in text analysis.

<!--s-->

# L.14 | Natural Language Processing II

[[slides]](https://drc-cs.github.io/WINTER25-CS326/lectures/L14_nlp_ii/#/)

- Explain the benefits of word embeddings over one-hot encoding.

- Explain the difference between traditional word embeddings over contextual embeddings.

- Differentiate between a CBOW and Skip-Gram model.

- Know what vector databases do and how they are used in NLP / RAG systems.

<!--s-->

# L.15 | Ethics

[[slides]](https://drc-cs.github.io/WINTER25-CS326/lectures/L15_ethics/#/)

- Evaluate metrics for their interpretability.

- Know GDPR, CCPA, and HIPAA and how they relate to data science.

- Differentiate between opt-in and opt-out consent.

<!--s-->

<div class = "col-wrapper">
  <div class="c1 col-centered">
    <div style="font-size: 0.8em; left: 0; width: 60%; position: absolute;">

  # Exit Poll
  ## On a scale of 1-5, how confident are you feeling about Exam Part II?

  </div>
  </div>
  <div class="c2" style="width: 50%; height: 100%;">
  <iframe src="https://drc-cs-9a3f6.firebaseapp.com/?label=Exit Poll" width="100%" height="100%" style="border-radius: 10px"></iframe>
  </div>

</div>

<!--s-->
