---
title: CS 326
separator: <!--s-->
verticalSeparator: <!--s-->
theme: serif
revealOptions:
  transition: 'none'
---

<div class = "col-wrapper">
  <div class="c1 col-centered">
  <div style="font-size: 0.8em; left: 0; width: 70%; position: absolute;">

  # Introduction to Data Science Pipelines
  ## L.02 | Data Sources

  </div>
  </div>
  <div class="c2 col-centered" style = "bottom: 0; right: 0; width: 80%; padding-top: 30%">
  
  <iframe src="https://lottie.host/embed/bd6c5b65-d724-4f97-882c-40f58367ea38/BIKhZdSeqW.json" height="100%" width = "100%"></iframe>
  </div>
</div>

<!--s-->

<div class = "header-slide">

# L.02 Data Sources

</div>

<!--s-->

L.02-Q.01
<div style="height: 100%; width: 100%;"><iframe src="https://docs.google.com/forms/d/e/1FAIpQLSdzqNfeJ2lnYgs6rvYziy_VRiQQTvt54ktjf_7_eLBSwf11Lw/viewform?embedded=true" width="80%" height="100%" frameborder="0" marginheight="0" marginwidth="0" style="margin-left: 10%; margin-right: 10%;">Loading…</iframe></div><!--s-->

## Data Sources

Data is at the heart of all data science! It's the raw material that we use to build models, make predictions, and draw conclusions. Data can be gathered from a variety of sources, and it comes in many different forms. 

<div class = "col-wrapper">
<div class = "c1" style = "width: 50%;">

Common Data Sources:

- Bulk Downloads
- APIs
- Scraping, Web Crawling
- BYOD (Bring Your Own Data)

</div>

<div class = "c2" style = "width: 50%">

<img src="https://imageio.forbes.com/blogs-images/gilpress/files/2016/03/Time-1200x511.jpg?format=jpg&width=1440" width="100%">
<p style="text-align: center; font-size: 0.6em; color: grey;">Forbes 2022</p>

</div>

<!--s-->

## Data Sources | Bulk Downloads

Large datasets that are available for download from the internet.


| Source | Examples | Advantages | Disadvantages |
| --- | --- | --- | --- |
| Government | data.gov | often free, very large datasets | Non-specific |
| Academic | UCI Machine Learning Repository | usually free, large datasets | Non-specific |
| Industry | Kaggle, HuggingFace | sometimes free, large datasets | Non-specific, sometimes expensive |


```python
# Demonstration of pulling from the UCI machine learning repository.
import pandas as pd
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
df = pd.read_csv(url, header=None)
```

```python
# Demonstration of pulling from the HuggingFace datasets library.
from datasets import load_dataset
dataset = load_dataset('imdb')
```

<!--s-->

## Data Sources | APIs

Data APIs are often readily available for sign up (usually for a fee).

While offering a lot of data, APIs can be restrictive in terms of the data they provide (and the rate at which you can pull it!).

API's often have better structure (usually backed by a db), and they often have the additional benefit of streaming or real-time data that you can poll for updates.

```python
import requests

API_KEY = 'your_api_key'
url = f'https://api.yourapi.com/data?api_key={API_KEY}'
r = requests.get(url)
data = r.json()
```

```python
from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-3.5-turbo-0125",
  response_format={ "type": "json_object" },
  messages=[
    {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
    {"role": "user", "content": "Who won the world series in 2020?"}
  ]
)
```

<!--s-->

## Data Sources | Scraping, Web Crawling

Web crawling is a free way to collect data from the internet. But be **cautious**. Many websites have terms of service that prohibit scraping, and you can easily overstep those and find yourself in legal trouble.

Examples of packages built for webscraping in Python include <span class="code-span">beautifulsoup</span> and <span class="code-span">scrapy</span>.

```python
import requests
from bs4 import BeautifulSoup
url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
soup.find_all('p')
```

<!--s-->

## Data Sources | BYOD (Bring Your Own Data)

Data that you collect yourself. In this case, you determine the format.

Examples for collecting survey data include Qualtrics and SurveyMonkey.

```python
import pandas as pd
df = pd.read_csv('survey_data.csv')
```
<!--s-->

## Data Sources | BYOD (Bring Your Own Data)
Collecting data yourself is common in academia and industry. But you need to be careful.

<div class = "col-wrapper">
<div class = "c1" style = "width: 70%;">

**Policies Exist**
- *GDPR*: Controllers of personal data must put in place appropriate technical and organizational measures to implement the data protection principles.
- *HIPAA*: Covered entities must have in place appropriate administrative, technical, and physical safeguards to protect the privacy of protected health information.

**Bias *Always* Exists** Bias is everywhere. It's in the data you collect, the data you don't collect, and the data you use to train your models. In almost all cases, we perform a *sampling*. It's your job to ensure it is a reasonable sample.

**Ethical Concerns**
Don't collect data that you don't need. Definitely don't collect data that you don't have permission to collect.

</div>
<div class = "c2 col-centered"  style = "width: 30%">
<iframe width="256" height="256" src="https://www.youtube.com/embed/R2vhjC5qCQk?si=m3ImvZqhDawRoMTo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>
</div>

<!--s-->

L.02-Q.02
<div style="height: 100%; width: 100%;"><iframe src="https://docs.google.com/forms/d/e/1FAIpQLSdpU_zAiiYBDpEEq7gpzLHuxyRryyUjKvwhTTE-kG2YrYf07w/viewform?embedded=true" width="80%" height="100%" frameborder="0" marginheight="0" marginwidth="0" style="margin-left: 10%; margin-right: 10%;">Loading…</iframe></div><!--s-->

L.02-Q.03
<div style="height: 100%; width: 100%;"><iframe src="https://docs.google.com/forms/d/e/1FAIpQLSdBmCohjRve3qh4BWwixBUAQV3Eu8xRi30gYN0-3ME7wv1qsg/viewform?embedded=true" width="80%" height="100%" frameborder="0" marginheight="0" marginwidth="0" style="margin-left: 10%; margin-right: 10%;">Loading…</iframe></div><!--s-->

<div class = "header-slide">

# Data Structures

</div>
<!--s-->


## Data Structures

| Type | Example | Advantages | Disadvantages |
| --- | --- | --- | --- |
| Structured | Relational Database | easy to query, fast | not flexible, hard to update schema |
| Semi-Structured | XML, CSV, JSON | moderate flexibility, easy to add more data | slow, harder to query |
| Unstructured | Plain Text, Images, Audio, Video | very flexible, easy to add more data | slow, hardest to query |

<!--s-->

## Data Structures | Structured Example (Relational Database)

| Type | Example | Advantages | Disadvantages |
| --- | --- | --- | --- |
| Structured | Relational Database | easy to query, fast | not flexible, hard to update schema |
| Semi-Structured | XML, CSV, JSON | moderate flexibility, easy to add more data | slow, harder to query |
| Unstructured | Plain Text, Images, Audio, Video | very flexible, easy to add more data | slow, hardest to query |

```sql
CREATE TABLE employees (
  employee_id INT PRIMARY KEY,
  name VARCHAR(100),
  hire_date DATE
);
```
<!--s-->

## Data Structures | Semi-Structured Example (JSON)

| Type | Example | Advantages | Disadvantages |
| --- | --- | --- | --- |
| Structured | Relational Database | easy to query, fast | not flexible, hard to update schema |
| Semi-Structured | XML, CSV, JSON | moderate flexibility, easy to add more data | slow, harder to query |
| Unstructured | Plain Text, Images, Audio, Video | very flexible, easy to add more data | slow, hardest to query |

```json
employeeData = {
  "employee_id": 1234567,
  "name": "Jeff Fox",
  "hire_date": "1/1/2013"
};
```

<!--s-->

## Data Structures | Unstructured Example (Plain Text)

| Type | Example | Advantages | Disadvantages |
| --- | --- | --- | --- |
| Structured | Relational Database | easy to query, fast | not flexible, hard to update schema |
| Semi-Structured | XML, CSV, JSON | moderate flexibility, easy to add more data | slow, harder to query |
| Unstructured | Plain Text, Images, Audio, Video | very flexible, easy to add more data | slow, hardest to query |

```text
Dear Sir or Madam,

My name is Jeff Fox (employee id 1234567). I'm excited to start on 1/1/2013.

Sincerely,
Jeff Fox
```

<!--s-->

<div class = "header-slide">

# Data Cleaning

</div>
<!--s-->

## Data Cleaning

Data is often dirty! Don't ever give your machine learning or statistical model dirty data.

Remember the age-old adage:

> Garbage in, garbage out.

 Data cleaning is the process of converting source data into target data without errors, duplicates, or inconsistencies. You will often need to structure data in a way that is useful for your analysis, so learning some basic data manipulation is **essential**.

<!--s-->

## Data Cleaning | Common Data Issues

1. Incompatible data
2. Missing values
3. Extreme Outliers

<!--s-->

## Data Cleaning | Handling Incompatible Data

<div style = "font-size: 0.85em;">

| Data Issue | Description | Example | Solution |
| --- | --- | --- | --- |
| Unit Conversions | Numerical data conversions can be tricky. | 1 mile != 1.6 km | Measure in a common unit, or convert with caution. |
| Precision Representations | Data can be represented differently in different programs. | 64-bit float to 16-bit integer | Use the precision necessary and hold consistent. |
| Character Representations | Data is in different character encodings. | ASCII, UTF-8, ... | Create using the same encoding, or convert with caution. |
| Text Unification | Data is in different formats. | D'Arcy; Darcy; DArcy; D Arcy; D&-#-3-9-;Arcy | Use a common format, or convert with caution. <span class="code-span">RegEx</span> will be your best friend.| 
| Time / Date Unification | Data is in different formats. | 10/11/2019 vs 11/10/2019 | Use standard libraries & UTC. A personal favorite is seconds since epoch. |

</div>
<!--s-->

## Data Cleaning | Handling Missing Values

<div class = "col-wrapper">
<div class="c1" style = "width: 50%">

  Data is often missing from datasets. It's important to identify why it's missing. Once you have established that it is **missing at random**, you can proceed with **substitution**.

  When missing data, we have a few options at our disposal:

  1. Drop the entire row
  2. Drop the entire column
  3. Substitute with a reasonable value

</div>
<div class="c2" style = "width: 50%">

  ``` [1-5|4]
  id    col1    col2    col3    col4
  p1    2da6    0.99    32     43
  p2    cd2d    1.23    55      38
  p3    9999    89.2    NaN     32
  p4    4e7c    0.72    9.7     35
  ```

</div>
</div>

<!--s-->

## Data Cleaning | Handling Missing Values with Substitution

<div class = "col-wrapper"> 
<div class = "c1" style = "width: 70%; font-size: 0.85em;">


| Method | Description | When to Use |
| --- | --- | --- |
| Forward / backward fill | Fill missing value using the last / next valid value. | Time Series |
| Imputation by interpolation | Use interpolation to estimate missing values. | Time Series |
| Mean value imputation | Fill missing value with mean from column. | Random missing values |
| Conditional mean imputation | Estimate mean from other variables in the dataset. | Random missing values |
| Random imputation | Sample random values from a column. | Random missing values | 
| KNN imputation | Use K-nearest neighbors to fill missing values. | Random missing values |
| Multiple Imputation | Uses many regression models and other variables to fill missing values. | Random missing values |

</div>

<div class = "c2 col-centered" style = "width: 40%">

```python
import pandas as pd

# Load data.
df = pd.read_csv('data.csv')

# Forward fill.
df_ffill = df.fillna(method='ffill')

# Backward fill.
df_bfill = df.fillna(method='bfill')

# Mean value imputation.
df_mean = df.fillna(df.mean())

# Random value imputation.
df_random = df.fillna(df.sample())

# Imputation by interpolation.
df_interpolate = df.interpolate()
```

</div>
</div>

<!--s-->

L.02-Q.04
<div style="height: 100%; width: 100%;"><iframe src="https://docs.google.com/forms/d/e/1FAIpQLSfZsYR39A9u0YLKv2WJTOaXFEseBg_b-UrpgLIC6TMaHGOmuQ/viewform?embedded=true" width="80%" height="100%" frameborder="0" marginheight="0" marginwidth="0" style="margin-left: 10%; margin-right: 10%;">Loading…</iframe></div><!--s-->

## Data Cleaning | Handling Outliers

Outliers are extreme values that deviate from other observations on data. They may indicate a variability in a measurement, experimental errors, or a novelty.

Outliers can be detected using:

- **Boxplots**: A visual representation of the five-number summary.
- **Scatterplots**: A visual representation of the relationship between two variables.
- **z-scores**: A measure of how many standard deviations a data point is from the mean.
- **IQR**: A measure of statistical dispersion, being equal to the difference between the upper and lower quartiles.

Handling outliers should be done on a case-by-case basis. Don't throw away data unless you have a very compelling (and **documented**) reason to do so!

<!--s-->

## Data Cleaning | Keep in Mind

- Cleaning your data is an iterative process.
  - **Hot tip**: Focus on making your data preprocessing *fast*. You will be doing it a lot, and you'll want to be able to iterate quickly. Look into libraries like <span class="code-span">dask</span>, <span class="code-span">pyspark</span>, and <span class="code-span">ray</span> for large datasets.
- Data cleaning is often planned with visualization. 
  - Always look at the data. Always. We'll go over plotting approaches for L.03.
- Data cleaning can fix modeling problems.
  - Your first assumption should always be "something is wrong with the data", not "I should try another model".
- Data cleaning is not a one-size-fits-all process, and often requires domain expertise.

<!--s-->

L.02-Q.05
<div style="height: 100%; width: 100%;"><iframe src="https://docs.google.com/forms/d/e/1FAIpQLSdS_BzH7-HBHWwEeCIV2e3rydlqY6bfjtFRu4wVmNliBuxckQ/viewform?embedded=true" width="80%" height="100%" frameborder="0" marginheight="0" marginwidth="0" style="margin-left: 10%; margin-right: 10%;">Loading…</iframe></div><!--s-->

<div class="header-slide">

# Questions?

</div>