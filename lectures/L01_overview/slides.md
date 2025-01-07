---
title: CS 326
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
  ## L.01 | Overview & Logistics

  </div>
  </div>
  <div class="c2 col-centered" style = "bottom: 0; right: 0; width: 80%; padding-top: 30%">
  
  <iframe src="https://lottie.host/embed/bd6c5b65-d724-4f97-882c-40f58367ea38/BIKhZdSeqW.json" height="100%" width = "100%"></iframe>
  </div>
</div>

<!--s-->

<div class = "col-wrapper">
  <div class="c1 col-centered">
  <div style="font-size: 0.8em; left: 0; width: 70%; position: absolute;">

  # Welcome to CS 326.
  ## Please check in using PollEverywhere.
  Scan the QR code or go to [pollev.com/nucs](https://pollev.com/nucs)

  </div>
  </div>
  <div class="c2 col-centered" style = "bottom: 0; right: 0; width: 100%; padding-top: 5%">
  <img src="https://storage.googleapis.com/slide_assets/PollEverywhere.png" width="50%">
  </div>
</div>

<!--s-->

## Attendance

Attendance at lectures is **mandatory** and in your best interest!

Attendance is worth 10% of your final grade. Most lectures will have interactive quizzes throughout the lecture that will be graded for completion. The top 16 quiz scores will be used to calculate your attendance grade, leaving you with 4 freebies throughout the quarter.

<!--s-->

## Grading

There is a high emphasis on the practical application of the concepts covered in this course. 
<div class = "col-wrapper">
<div class="c1" style = "width: 50%">

| Component | Weight |
| --- | --- |
| Homework | 50% |
| Exam Part I | 20% |
| Exam Part II | 20% |
| Attendance | 10% |

</div>
<div class="c2" style = "width: 50%">

| Grade | Percentage |
| --- | --- |
| A | 94-100 |
| A- | 90-93 |
| B+ | 87-89 |
| B | 83-86 |
| B- | 80-82 |
| C+ | 77-79 |
| C | 73-76 |
| C- | 70-72 |

</div>
</div>

<!--s-->

## Homework 

Homeworks are designed to reinforce the concepts covered in lecture. They will be a mix of theoretical and practical problems, and each will include a programmatic and free response portion. If there is time, we will work on homework at the end of every lecture as a group. For the automated grading server, you get 2 attempts per homework assignment. The highest score will be recorded.

- **Due**: Homework due dates are posted in the syllabus.

- **Late Policy**: Late homeworks will lose 1 out of 10 points per day (1% of your final grade).

- **Platform**: A submission script has been provided to submit your homeworks.

- **Collaboration**: You are encouraged to work with your peers on homeworks. However, you must submit your own work. Copying and pasting code from other sources will be detected and penalized.

<!--s-->

## LLMs (The Talk)

<iframe src="https://lottie.host/embed/e7eb235d-f490-4ce1-877a-99114b96ff60/OFTqzm1m09.json" height = "100%" width = "100%"></iframe>

<!--s-->

## Exams

There are two exams in this class. They will cover the theoretical and practical concepts covered in the lectures and homeworks. If you follow along with the lectures and homeworks, you will be well-prepared for the exams.

<!--s-->

## Academic Integrity [&#x1F517;](https://www.northwestern.edu/provost/policies-procedures/academic-integrity/index.html)

### Homeworks

- Do not exchange code fragments on any assignments.
- Do not copy solutions from any source, including the web or previous CS 326 students.
- You cannot upload / sell your assignments to code sharing websites.

<!--s-->

## Accommodations

Any student requesting accommodations related to a disability or other condition is required to register with AccessibleNU and provide professors with an accommodation notification from AccessibleNU, preferably within the first two weeks of class. 

All information will remain confidential.

<!--s-->

## Mental Health

If you are feeling distressed or overwhelmed, please reach out for help. Students can access confidential resources through the Counseling and Psychological Services (CAPS), Religious and Spiritual Life (RSL) and the Center for Awareness, Response and Education (CARE).

<!--s-->

## Stuck on Something?

### **Office Hours**

- Time: TBA
- Location: TBA

### **Canvas Discussion**

- Every homework & project will have a discussion thread on Canvas.
- Please post your questions there so that everyone can benefit from the answers!

<!--s-->

## Stuck on Something?

### **Email**

We are here to help you! Please try contacting us through office hours or the dedicated Canvas discussion threads.

<div class = "col-wrapper" style="font-size: 0.8em;">
<div class="c1" style = "width: 50%">

**Peer Mentors**:
- Sai Chakradhar Induvasi: wvg6368@ads.northwestern.edu
- Shreya Singh: wku8357@ads.northwestern.edu
- Nathan Mo: nmf0887@ads.northwestern.edu
- Ishan Mukherjee: ishanmukherjee2027@u.northwestern.edu
- Shubhi Gupta: ShubhiGupta2025@u.northwestern.edu

</div>
<div class="c2" style = "width: 50%">

**TA**:
- Sayak Chakrabarty: sayakchakrabarty2025@u.northwestern.edu

**Intructor**:
- Joshua D'Arcy: joshua.darcy@northwestern.edu

</div>

<!--s-->

<div class = "col-wrapper">
  <div class="c1 col-centered">
  <div style="font-size: 0.8em; left: 0; width: 60%; position: absolute;">
    
  ## L.01 | Q.01

  What are you most looking forward to learning in CS 326?

  Scan the QR code or go to [pollev.com/nucs](https://pollev.com/nucs)

  </div>
  </div>
  <div class="c2 col-centered" style = "bottom: 0; right: 0; width: 100%; padding-top: 5%; padding-bottom: 0%;">
  <img src="https://storage.googleapis.com/slide_assets/PollEverywhere.png" width="50%">
  </div>
</div>

</div>

<!--s-->

<div class="header-slide">

# Homework Assignment
## H.01 "Hello World!"

Due: 01.14.2025

</div>

<!--s-->

## H.01 | Installing Conda

We will be using Python for this course. Conda is a package manager that will help us install Python and other packages. 

Don't have <span class="code-span">conda</span> installed? [[click-here]](https://docs.conda.io/en/latest/miniconda.html)

<!--s-->

## H.01 | Cloning Repo & Installing Environment

We will be using a public GitHub repository for this course. Enter the following commands in your terminal to clone the repository and install the class environment.


```bash
git clone https://github.com/drc-cs/WINTER25-CS326.git
cd WINTER25-CS326
```

We will be using a conda environment (cs326) for this course. 

```bash
conda env create -f environment.yml
conda activate cs326
```

Don't have <span class="code-span">git</span> installed? [[click-here]](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

<!--s-->

## H.01 | VSCode

All demonstrations will be in VSCode, which is a popular IDE. You're welcome to use any IDE you want, but we will be best equipped to help you if you use VSCode.

Don't have <span class="code-span">visual studio code</span> installed? [[click-here]](https://code.visualstudio.com/)

After installing VSCode, you will need to install the Python extension: 

1. Open VSCode
2. Click on the "Extensions" icon in the "Activity Bar" on the side of the window
3. Search for "Python" and click "Install"

Add the <span class="code-span">code</span> command to your PATH so you can open VSCode from the terminal.

1. Open the "Command Palette" (Ctrl+Shift+P on PC or Cmd+Shift+P on Mac)
2. Search for "Shell Command: Install 'code' command in PATH" and click it

<!--s-->

## H.01 | Opening Repo in VSCode

Restart your terminal and open the cloned repository in VSCode using the following command:

```bash
code WINTER25-CS326
```

You should see the following folders:

- <span class="code-span">README.md</span>: Contains the course syllabus.
- <span class="code-span">lectures/</span>: Contains the lecture slides in markdown format.
- <span class="code-span">homeworks/</span>: Contains the homework assignments.

<!--s-->

## H.01 | Pulling

Before you start working on any homework, make sure you have the latest version of the repository.

The following command (when used inside the class folder) will pull the latest version of the repository and give you access to the most up-to-date homework:

```bash
git pull
```

If you have any issues with using this git-based system, please reach out to us during office hours or via email.

<!--s-->

## H.01 | Opening Homework

Open the <span class="code-span">homeworks/</span> folder in VSCode. You should see a folder called <span class="code-span">H.01/</span>. Open the folder and you will see three files: 

- <span class="code-span">hello_world.py</span>: This file contains placeholders for the methods you will write.

- <span class="code-span">hello_world.ipynb</span>: This is a Jupyter notebook that provides a useful narrative for the homework and methods found in the <span class="code-span">hello_world.py</span> file.

- <span class="code-span">hello_world_test.py</span>: This is the file that will be used to test your code. Future homeworks will not include this file, and this is for demonstration purposes only.

Let's do the first homework together.

<!--s-->
<div class = "header-slide">

 ## Homework Demonstration

</div>
<!--s-->

## H.01 | Submitting Homework

You will submit your homework using the provided submission script. 

But first, you need a username (your **northwestern** email e.g. JaneDoe2024@u.northwestern.edu) and password!

```bash
python account.py --create-account
```

Once you have a username and password, you can submit your completed homework. You should receive your score or feedback within a few seconds, but this may take longer as the homeworks get more involved.

```bash
python submit.py --homework H01/hello_world.py --username your_username --password your_password 
```

You can save your username and password as environment variables so you don't have to enter them every time (or expose them in your notebooks)!

```bash
export AG_USERNAME="your_username"
export AG_PASSWORD="your_password"
```
<!--s-->

## H.01 | Homework Grading

The highest score will be recorded, so long as it is submitted before the deadline! You have 2 attempts for every homework. 

Late homeworks will be penalized 10% per day.

<!--s-->

## H.01 | Expected Learnings / TLDR;

With this <span class="code-span">hello_world</span> assignment, we worked on the following:

1. Environment installation practice (<span class="code-span">conda</span>)
2. Exposure to git management (<span class="code-span">GitHub</span>)
3. Local development IDE practice (<span class="code-span">vscode</span>)
4. Familiarity with unit testing (<span class="code-span">pytest</span>)

These tools are all critical for any industry position and are often expected for entry level positions. Please continue to familiarize yourself with them over the course of the quarter.

<!--s-->

<div class="header-slide">

# Questions?

</div>

<!--s-->