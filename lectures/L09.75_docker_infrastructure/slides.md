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
  ## L.09<span>$\frac{3}{4}$</span> | Docker Essentials & Exam Review

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

- H.03 is due tonight at 11:59 PM.
  - Autograder bugs have been fixed. 🫠🫠🫠
  - If your grade was affected by these bugs in any way, please don't hesitate to reach out.
  - Everyone was given +2 extra attempts to compensate (total 4).

- Lockdown Browser is required for the exam.
  - Practice quiz due 11:59PM on Monday.


<!--s-->

<div class="header-slide"> 

# Docker Essentials

</div>

<!--s-->

## Docker Essentials | Agenda

<div class = "col-wrapper">
<div class="c1" style = "width: 70%">

1. Why Containerization?
2. What is Docker and Why is it Useful?
3. Benefits of Using Docker
4. Docker Theory
5. Using Docker
6. Docker Demo

</div>
<div class="c2" style = "width: 30%">

<img src="https://raw.githubusercontent.com/docker-library/docs/c350af05d3fac7b5c3f6327ac82fe4d990d8729c/docker/logo.png" width="100%">

</div>

</div>

> <span style="font-style: normal;"> Vocabulary will be placed in boxes. </span>

<!--s-->

## Why Containerization?

A **container** is a lightweight, portable, and efficient way to package applications and their dependencies. Containers isolate applications from the host system and other containers, making them easier to deploy and manage.

| **Container** | **Virtual Machine** |
|---------------|---------------------|
| Lightweight | Heavyweight |
| Faster startup | Slower startup |
| Less resource usage | More resource usage |
| Shared kernel | Separate kernel |

> <span style="font-style: normal;"> The **kernel** is the core of an operating system that manages system resources. </span>

> <span style="font-style: normal;"> **Virtual machines** are software emulations of physical computers that run an operating system and applications. </span>

<!--s-->

## What is Docker and Why is it Useful?

**Docker** is an open-source platform designed to simplify the process of creating, deploying, and running applications. You can think of Docker as a self-contained package that includes everything an application needs to run: the code, runtime, system tools, libraries, and settings. 

This package is called a **image**. When you run an image, it creates a **container**, an isolated environment that runs the application.

> <span style="font-style: normal;">An **image** is a snapshot of an application and its dependencies. </span>

> <span style="font-style: normal;">A **container** is a running instance of an image. </span>

<!--s-->

## Benefits of Using Docker

1. Consistency Across Environments

2. Efficiency

3. Scalability

4. Isolation and Security

<!--s-->

## Benefits of Using Docker | Consistency

<div class = "col-wrapper" style = "height: 70%;">
<div class="c1" style = "width: 50%;">

Docker ensures that software behaves the same on every machine. Developers can be confident that applications that work on their computers will work in production.

Docker containers are typically based on a Linux distribution, which provides a consistent environment for applications.

</div>
<div class="c2" style = "width: 50%">

<img src = "https://miro.medium.com/v2/resize:fit:1400/0*Qqqd7UsfFDPL7WXh.jpeg" width="100%">

</div>
</div>

> <span style="font-style: normal;"> **Linux** distributions: Variants of the Linux operating system. Linux is by far the most popular OS in the world for web servers, cloud computing, and supercomputers. </span>
 
<!--s-->

## Benefits of Using Docker | Efficiency


Containers share the host's operating system kernel, which makes them more lightweight and efficient than traditional virtual machines.

This results in faster application delivery, reduced resource consumption, and lower overhead.


<img src="https://www.docker.com/wp-content/uploads/2022/12/admins-ask-about-docker-2.png" width="100%">
<p style="text-align: center; font-size: 0.6em; color: grey;">Docker 2022</p>


<!--s-->

## Benefits of Using Docker | Scalability

Docker makes it easy to scale applications horizontally by adding more containers. This supports modern cloud-native development practices.

Containers can be easily replicated and distributed across multiple hosts, providing flexibility and scalability.

<img src = "https://miro.medium.com/v2/resize:fit:1400/1*MzGIkBAGQwUyN2-Rs9opfA.jpeg" width="100%" style = "border-radius: 10px;">
<p style="text-align: center; font-size: 0.6em; color: grey;">Thakur 2024</p>

<!--s-->

## Benefits of Using Docker | Isolation and Security

<div class = "col-wrapper">
<div class="c1" style = "width: 50%">

Containers encapsulate applications and their dependencies completely, providing isolation that improves security.

</div>
<div class="c2" style = "width: 50%">

<img src="https://joeeey.com/static/c161c59028d1e817d0cdce747b9e79e7/d8bb9/covers.png" width="100%" style = "border-radius: 10px;">
<p style="text-align: center; font-size: 0.6em; color: grey;">Miller 2023</p>

</div>
</div>

<!--s-->


## Docker Architecture


<img src="https://miro.medium.com/v2/resize:fit:1400/0*G82uZfX0ozIih3-_" width="100%" style = "border-radius: 10px;">
<p style="text-align: center; font-size: 0.6em; color: grey;">NordicAPIs</p>



<!--s-->

## Docker Architecture | Key Docker Components

<div class = "col-wrapper">
<div class="c1" style = "width: 50%">

- Docker Daemon

- Docker Client

- Docker Images

- Docker Containers

- Docker Registries

- Namespaces and Control Groups

</div>
<div class="c2" style = "width: 50%">

<img src="https://miro.medium.com/v2/resize:fit:1400/0*G82uZfX0ozIih3-_" width="100%" style = "border-radius: 10px;">
<p style="text-align: center; font-size: 0.6em; color: grey;">NordicAPIs</p>


</div>
</div>

<!--s-->

## Docker Architecture | Daemon

The **Docker Daemon** (`dockerd`) is the heart of Docker, responsible for running containers on a host. It listens for API requests and manages Docker objects (images, containers, networks, etc.).

<div class = "col-wrapper">

<div class="c1" style = "width: 50%">

<img src="https://miro.medium.com/v2/resize:fit:1400/0*G82uZfX0ozIih3-_" height="50%" style = "border-radius: 10px;">
<p style="text-align: center; font-size: 0.6em; color: grey;">NordicAPIs</p>

</div>

<div class="c2" style = "width: 50%">

> <span style="font-style: normal;"> A **daemon** is a background process that runs continuously, waiting for requests to process. </span>

</div>

</div>


<!--s-->

## Docker Architecture | Client

The **Docker Client** is a command-line tool (CLI) used by the user to interact with the Docker daemon. 

<div class = "col-wrapper">
<div class="c1" style = "width: 50%">

Common CLI commands include <span class="code-span">docker pull</span>, <span class="code-span">docker build</span>, and <span class="code-span">docker run</span>. The client sends commands to the daemon, which executes them on the host.

</div>
<div class="c2" style = "width: 50%">

<img src="https://miro.medium.com/v2/resize:fit:1400/0*G82uZfX0ozIih3-_" width="100%" style = "border-radius: 10px;">
<p style="text-align: center; font-size: 0.6em; color: grey;">NordicAPIs</p>

</div>
</div>



<!--s-->

## Docker Architecture | Images

**Docker Images** are immutable, read-only templates used to create containers.

<div class = "col-wrapper">
<div class="c1" style = "width: 50%">

An image might include an OS, application code, and dependencies required to run an application. Images are built from a series of layers. Each layer represents a modification to the previous layer, allowing for efficient storage and distribution of images.

</div>
<div class="c2" style = "width: 50%">

<img src="https://miro.medium.com/v2/resize:fit:1400/0*G82uZfX0ozIih3-_" width="100%" style = "border-radius: 10px;">
<p style="text-align: center; font-size: 0.6em; color: grey;">NordicAPIs</p>

</div>
</div>


<!--s-->

## Docker Architecture | Containers

**Docker Containers** are running instances of Docker images.

<div class = "col-wrapper">
<div class="c1" style = "width: 50%">

They can be started, stopped, moved, or deleted using Docker commands. Containers are isolated from each other and the host system, but they share the host OS's kernel. This makes them lightweight and efficient.

</div>
<div class="c2" style = "width: 50%">

<img src="https://miro.medium.com/v2/resize:fit:1400/0*G82uZfX0ozIih3-_" width="100%" style = "border-radius: 10px;">
<p style="text-align: center; font-size: 0.6em; color: grey;">NordicAPIs</p>

</div>
</div>

<!--s-->

## Docker Architecture | Registries

**Docker Registries** store Docker images. A popular public registry is Docker Hub, but private registries can also be used. Docker images can be pushed to and pulled from registries, allowing for easy distribution and sharing of images.

<div class = "col-wrapper">
<div class="c1" style = "width: 50%">

Other examples of registries include:

- **Amazon Elastic Container Registry (ECR)**
- **Google Container Registry (GCR)**
- **Azure Container Registry (ACR)**

</div>
<div class="c2" style = "width: 50%">

<img src="https://miro.medium.com/v2/resize:fit:1400/0*G82uZfX0ozIih3-_" width="100%" style = "border-radius: 10px;">
<p style="text-align: center; font-size: 0.6em; color: grey;">NordicAPIs</p>

</div>
</div>

<!--s-->

## Docker Architecture | Core Concepts

### Namespaces and Control Groups
Docker uses Linux namespaces to provide isolation for containers and control groups (cgroups) to limit resource usage.

### Union File System
Layers are used to create Docker images. Each layer is a modification over the previous one, which allows efficient storage and reduced bandwidth usage when distributing an image. A Union File System (UFS) combines these layers into a single view (union) of the file system.

<div class = "col-wrapper">
<div class="c1" style = "width: 50%">

> <span style="font-style: normal;"> **Namespaces**: Isolate containers from each other and the host system. </span>

> <span style="font-style: normal;"> **Control Groups (cgroups)**: Limit resource usage for containers. </span>

</div>
<div class="c2" style = "width: 50%">

> <span style="font-style: normal;"> **Union File System**: Efficiently store and distribute Docker images. </span>

</div>
</div>

<!--s-->

## Using Docker

1. Installing Docker
2. Building from a Dockerfile
3. Running Containers

<!--s-->

## Using Docker | Installing Docker

To start using Docker, you need to install the Docker Engine on your machine. It can be downloaded from the Docker website and is available for various operating systems, including Windows, MacOS, and Linux.

Download Docker Desktop: [Docker Desktop](https://www.docker.com/products/docker-desktop)

<!--s-->

## Using Docker | Building a Dockerfile

<div class = "col-wrapper">
<div class="c1" style = "width: 50%">

A **Dockerfile** is a text document that contains all the commands needed to assemble a Docker **image**. It starts with a <span class="code-span">FROM</span> instruction that specifies the base image. 


Usually, it also includes commands like <span class="code-span">WORKDIR</span>, <span class="code-span">COPY</span>, <span class="code-span">RUN</span>, and <span class="code-span">CMD</span> to set up the environment and run the application.

</div>
<div class="c2" style = "width: 50%">

```dockerfile

# Use an official Python runtime as a parent image.
FROM python:3.8-slim

# Set the working directory.
WORKDIR /app

# Copy the current directory contents into the container at /app.
COPY . /app

# Install any needed packages specified in requirements.txt.
# RUN is used to execute commands during the build process.
RUN pip install --no-cache-dir -r requirements.txt

# Start the application. CMD specifies the command to run when the container starts.
CMD ["python", "app.py"]

```

</div>
</div>

<!--s-->

## Dockerfile | Cheatsheet

Here are some common Dockerfile commands.


| Command | Description |
|---------|-------------|
| <span class="code-span">FROM</span> | Specifies the base image to use. |
| <span class="code-span">WORKDIR</span> | Sets the working directory for subsequent commands. |
| <span class="code-span">COPY</span> | Copies files from the host to the container. |
| <span class="code-span">RUN</span> | Executes commands during the build process. |
| <span class="code-span">CMD</span> | Specifies the command to run when the container starts. |
| <span class="code-span">EXPOSE</span> | Exposes a port to the host machine. |
| <span class="code-span">ENV</span> | Sets environment variables. |
| <span class="code-span">ENTRYPOINT</span> | Configures the container to run as an executable. |
<!--s-->

## Docker | CLI Cheatsheet

Here are some common Docker CLI commands.

| Command | Description |
|---------|-------------|
| <span class="code-span">docker --version</span> | Checks the installed version of Docker. |
| <span class="code-span">docker pull [image_name]</span> | Pulls an image from a registry. |
| <span class="code-span">docker build -t [image_name] .</span> | Builds an image from a Dockerfile. |
| <span class="code-span">docker run [image_name]</span> | Runs a container from an image, common flags include <span class="code-span">-d</span> for detached mode, <span class="code-span">-p</span> for port mapping, and <span class="code-span">-v</span> for volume mounting. |
| <span class="code-span">docker ps</span> | Lists running containers. |
| <span class="code-span">docker images</span> | Lists images on the host. |

<!--s-->

## Docker Demo

Let's see Docker in action. Many of you working on Windows had difficulty installing the <span class="code-span">cs326</span> requirements for local development.

Imagine you could run the course env locally with minimal setup... Let's see how Docker can help with that.

<!--s-->

## Docker Demo | Course Environment

<div class = "col-wrapper">
<div class="c1" style = "width: 50%">

To the right is a dockerfile that will install the course environment and run <span class="code-span">code-server</span> in a container. 

This will allow you to run the course environment locally without installing any dependencies to your operating system (Windows, MacOS, Linux).

</div>
<div class="c2" style = "width: 70%; height: 100%;">

```dockerfile
# Use the official Miniconda3 image as a parent image.
FROM continuumio/miniconda3

# Clone the class repository.
RUN apt-get update && apt-get install -y git curl
RUN git clone https://github.com/drc-cs/WINTER25-CS326.git

# Set the working directory.
WORKDIR /WINTER25-CS326

# Create a new Conda environment from the environment.yml file.
RUN conda env create -f environment.yml

# Install vscode server.
RUN curl -fsSL https://code-server.dev/install.sh | bash

# Add code-server to PATH
ENV PATH="/root/.local/bin:${PATH}"

# Expose the port that the server is running on.
EXPOSE 8080

# Run the code-server command when the container starts.
CMD ["code-server", "--auth", "none", "--bind-addr", "0.0.0.0:8080", "."]

```

</div>
</div>

<!--s-->

## Docker Demo | Running the Course Environment

Since we run the <span class="code-span">code-server</span> on port 8080, we need to map the container's port to the host machine. We can do this using the <span class="code-span">-p</span> flag. Here we mapped the container's port 8080 to the host machine's port 8080. Since code-server is already running within the docker container, we can access it by visiting <span class="code-span">localhost:8080</span> in your browser.

As long as the container is running, you can access the course environment by visiting <span class="code-span">localhost:8080</span> in your browser at any time. It will even work offline!

<div class = "col-wrapper">
<div class="c1" style = "width: 50%">

```bash
# Build the Docker image.
docker build -t cs326-env .

# Run the Docker container on port 8080 (local).
docker run -p 8080:8080 cs326-env
```

</div>
<div class="c2" style = "width: 50%">

<img src="https://user-images.githubusercontent.com/35271042/118224532-3842c400-b438-11eb-923d-a5f66fa6785a.png" width="100%">

</div>
</div>

<!--s-->

## Conclusion

Docker is a powerful tool that simplifies the process of creating, deploying, and running applications. 

It provides consistency, efficiency, scalability, isolation, and portability for modern software development. Understanding Docker's core concepts and best practices can help you leverage its benefits in your projects.

<div class = "col-centered">
<img src="https://miro.medium.com/v2/resize:fit:1400/0*G82uZfX0ozIih3-_" style = "border-radius: 10px" width="50%">
<p style="text-align: center; font-size: 0.6em; color: grey;">NordicAPIs</p>
</div>

<!--s-->

<div class="header-slide">

# Exam Part I Review

</div>

<!--s-->

## Ground Rules

You will **not** be expected to do any programming on the exam. You will be asked to interpret code, identify errors, and explain concepts. The exam will be **closed book** and **closed notes**. You will not be allowed to use any resources during the exam. You will not need a calculator.

The following topics will be covered on the exam -- they are not exhaustive but should give you a good idea of what to expect.

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

- Identify kurtosis (leptokurtic, mesokurtic, platykurtic).

- Know key properties of a normal distribution.

<!--s-->

# L.04 | Correlation

[[slides]](https://drc-cs.github.io/WINTER25-CS326/lectures/L04_correlation_association/#/)

- Differentiate when to use Pearson vs Spearman correlation

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
