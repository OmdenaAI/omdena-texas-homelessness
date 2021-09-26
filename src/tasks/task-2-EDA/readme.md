# Task-2-EDA
## Resources
* app.py is designed for you to be able to do base-line data preprocessing and cleaning on the datasets provided through Omdena. Please let me know if you have any other suggestions on what we should do to add to this file as the collaborative effort on this is key to our success. If we can get this functioning at a high enough level, we can turn this over to the modeling team and the app building team as it will help them in the long run!

* Google Doc located [here](https://docs.google.com/spreadsheets/d/1clkY5UN5CpG_hbx1x8voCfqsJs-r9ym07e2xrLQ1WrQ/edit#gid=1386834576) has an overview of who is doing what on which dataset. Our goal is to get this done by the end of the week. Anyone who signs up will receive messages from me checking in every day or two as we progress.

* If you need assistance with your project and Slack is unable to answer your questions or you just want to schedule some 1-1 time with me to go over the data and gain a better understanding, you can schedule that time with me [here](https://calendly.com/alexlucchesi/30min) for a 30 minute interval and [here](https://calendly.com/alexlucchesi/15min) for a 15min. 

* Notebook Folder
  * This folder holds my initial exploratory notebooks with some key visuals to help you get started on a few different questions as you work to develop your own. 
  * These notebooks were built using some of the datasets already located within our Google Drive Doc as well as the Data Folder of this Git Repo. 
  * I hope you can build upon these visuals as well as you progress through your data exploration.
  
* Team Submissions
  * If you participated in this activity with more than yourself, please place your notebooks here. We want to see those who are working with others and making that effort to colaborate. You can put into the Readme.md the colaborators names, short description of your work, and link the file to it!
  
* Individual Submissions
  * If you participated in this activity on your own, please place your notebooks here! We want to see the efforts you put in! You can put into the Readme.md your name, short description of your work, and link your file to it! 
  
* Projects Tab
  * Has tasks in the form of "Notes" that you can grab, drag, and drop in different lists, as well as iterate over with your work completed
  * This is a great way for us to also keep track of contributions and keep redundancy to a minimum.  

## What is EDA? 
Check [this link here](https://www.ibm.com/cloud/learn/exploratory-data-analysis) for some more information on exactly what we mean when we say EDA. We are focused on analyzing the data, summarizing the main features, and use visualizations to show the data. Feature Engineering, Statistical Modeling, Hypothesis Testing, and Dimensionality Reduction. These all fall under our category. We will need to understand the data and how everything correlates in order to effectively accomplish this task. 

## Task & Task List
Our task is to complete the EDA so that our Modeling team can intake the data and run it into their models and focus on hyperparameter tuning. We will complete this by splitting the work flow as follows:
* Data Visualization and Normalizing
  * Data Visualizations
    * ***This is one of the most key factors in EDA***
    * Can we create visualizations that we can show to a consumer or marketing supervisor(basically anyone with little knowledge of DS) and get them to understand the data?
    * Using these visualizations, what insights do we gain from the data? Do we need to manipulate our data anymore than we already have?
  * Normalization vs. Scaling
    * As we create these visualizations, we need to think about how the data falls. Are we going to experience a skew that can lead to data leakage down the road? How does the data from this set fall on the map as opposed to the other data sets? Is it well-generalized or is this only specific to a certain circumstance? How is everything intraconnected? These are the key points in this subtask.
* Feature Engineering and Dimension Reduction
  * Target Identification and Feature Identification. What works with the data, what doesn't?
    * Do we need to create a target? How can we given the data provided?
    * If provided a target, are we sure that there isn't any columns in the data associated with the calculation of that target that can lead to Data Leakage?
    * What features are present in the data? Given these features, can we combine into one that may hold more significance than the two seperately?
    * Can we merge/join any of these sets together to give a stronger sense of the data? Some of these are short and small, what can we do with them?
  * Dimension Reduction
    * How does the data look? Is it a wide dataset? Long dataset? How is that going to work for our Modeling Task?
    * Low Variance: Should we filter out the variables that have a low variance compared to others? 
    * Decision Tree vs FillNA: Is it better for us to use a decision tree to deal with our NaN values in some of the datasets? Why?
    * PCA: Map the data to lower dimensional space in a linear fashion as to maximize the variance of the data
* Insights and DataSet Summarizations
  * Just as I posed questions to you guys at the beginning of the project in my EDA notebooks, what insights has the data given you into homelessness? Can we incur any hypothesis? Can this be tested? 
  * When we have the Data all pieced together, what does that look like? What is included in each of these data sets? The more information we can pass along to the next team about our data, the better
* Statistical Model Testing of Data
  * Ensure data fits into a model and can attain higher than baseline accuracy.
  * Once that is achieved, I would consider that a "win" that we can pass along to Task 3 for deployment modeling
  * Anyone who is in Task 3 as well is encouraged to take on this task!
