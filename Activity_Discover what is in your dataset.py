#!/usr/bin/env python
# coding: utf-8

# # Activity: Discover what is in your dataset

# ## Introduction
# 
# In this activity, you will discover characteristics of a dataset and use visualizations to analyze the data. This will develop and strengthen your skills in **exploratory data analysis (EDA)** and your knowledge of functions that allow you to explore and visualize data. 
# 
# EDA is an essential process in a data science workflow. As a data professional, you will need to conduct this process to better understand the data at hand and determine how it can be used to solve the problem you want to address. This activity will give you an opportunity to practice that process and prepare you for EDA in future projects.
# 
# In this activity, you are a member of an analytics team that provides insights to an investing firm. To help them decide which companies to invest in next, the firm wants insights into **unicorn companies**–companies that are valued at over one billion dollars. The data you will use for this task provides information on over 1,000 unicorn companies, including their industry, country, year founded, and select investors. You will use this information to gain insights into how and when companies reach this prestigious milestone and to make recommentations for next steps to the investing firm.

# ## Step 1: Imports

# ### Import libraries and packages 
# 
# First, import relevant Python libraries and modules. Use the `pandas` library and the `matplotlib.pyplot` module.

# In[3]:


# Import libraries and packages
import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
### YOUR CODE HERE ###


# ### Load the dataset into a DataFrame
# 
# The dataset provided is in the form of a csv file named `Unicorn_Companies.csv` and contains a subset of data on unicorn companies. As shown in this cell, the dataset has been automatically loaded in for you. You do not need to download the .csv file, or provide more code, in order to access the dataset and proceed with this lab. Please continue with this activity by completing the following instructions.

# In[4]:


# RUN THIS CELL TO IMPORT YOUR DATA.
### YOUR CODE HERE ###
companies = pd.read_csv("Unicorn_Companies.csv")


# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# Refer to what you learned about [loading data](https://www.coursera.org/learn/go-beyond-the-numbers-translate-data-into-insight/supplement/MdTG2/reference-guide-import-datasets-using-python) in Python.
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 2</strong></h4></summary>
# 
# Use the function in the `pandas` library that allows you to read data from a csv file and load the data into a DataFrame.
#  
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 3</strong></h4></summary>
# 
# Use the `read_csv()` function from the `pandas` library. 
# 
# </details>

# ## Step 2: Data exploration

# ### Display the first 10 rows of the data
# 
# Next, explore the dataset and answer questions to guide your exploration and analysis of the data. To begin, display the first 10 rows of the data to get an understanding of how the dataset is structured.

# In[5]:


# Display the first 10 rows of the data

### YOUR CODE HERE ###
companies.sort_values("Year Founded" , ascending=False ).head(10)


# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# Refer to [the content about exploratory data analysis in Python](https://www.coursera.org/learn/go-beyond-the-numbers-translate-data-into-insight/lecture/kfl9b/find-stories-using-the-six-exploratory-data-analysis-practices).
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 2</strong></h4></summary>
# 
# Use the function in the `pandas` library that allows you to get a specific number of rows from the top of a DataFrame.
#  
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 3</strong></h4></summary>
# 
# Use the `head()` function from the `pandas` library. 
# 
# </details>

# **Question:** What do you think the "Date Joined" column represents?

# * I think it represent the date of joining the company to Nasdak for stock mark in NewYork, or join to the NY stock market in general

# **Question:** What do you think the "Select Investors" column represents?

# * It represent the major investor/s in this company

# ### Assess the size of the dataset
# 
# Get a sense of how large the dataset is. The `size` property that DataFrames have can help.

# In[6]:


# How large the dataset is
companies.size
### YOUR CODE HERE ###


# **Question:** What do you notice about the size of the dataset?

# * The size of the set is greater than the number of columns, and this came due to multiply the rows in columns

# ### Determine the shape of the dataset
# 
# Identify the number of rows and columns in the dataset. The `shape` property that DataFrames have can help.

# In[7]:


# Shape of the dataset
companies.shape
### YOUR CODE HERE ###


# **Question:** What do you notice about the shape of the dataset?

# * the number of rows is greater than the number of columns

# ### Get basic information about the dataset
# 
# To further understand what the dataset entails, get basic information about the dataset, including the data type of values in each column. There is more than one way to approach this task. In this instance, use the `info()` function from `pandas`.

# In[8]:


# Get information

### YOUR CODE HERE ###
companies.info()


# **Question:** What do you notice about the type of data in the `Year Founded` column? Refer to the output from using `info()` above. Knowing the data type of this variable is helpful because it indicates what types of analysis can be done with that variable, how it can be aggregated with other variables, and so on.

# * The year is Intger

# **Question:** What do you notice about the type of data in the `Date Joined` column? Refer to the output from using `info()` above. Knowing the data type of this variable is helpful because it indicates what types of analysis can be done with that variable and how the variable can be transformed to suit specific tasks.

# * The data type here is object and it should be datetime

# ## Step 3: Statistical tests

# ### Find descriptive statistics
# 
# Find descriptive statistics and structure your dataset. The `describe()` function from the `pandas` library can help. This function generates statistics for the numeric columns in a dataset. 

# In[9]:


# Get descriptive statistics

### YOUR CODE HERE ###
companies.describe()


# **Question:** Based on the table of descriptive stats generated above, what do you notice about the minimum value in the `Year Founded` column? This is important to know because it helps you understand how early the entries in the data begin.

# * **The min year is 1919 from decade ago**
# 

# **Question:** What do you notice about the maximum value in the `Year Founded` column? This is important to know because it helps you understand the most recent year captured by the data. 

# * **The max is 2021 just from 2 years ago**

# ### Convert the `Date Joined` column to datetime
# 
# Use the `to_datetime()` function from the `pandas` library  to convert the `Date Joined` column to datetime. This splits each value into year, month, and date components. This is an important step in data cleaning, as it makes the data in this column easier to use in tasks you may encounter. To name a few examples, you may need to compare "date joined" between companies or determine how long it took a company to become a unicorn. Having "date joined" in datetime form would help you complete such tasks.

# In[10]:


# Step 1: Use pd.to_datetime() to convert Date Joined column to datetime 
# Step 2: Update the column with the converted values

### YOUR CODE HERE ###
companies["Date Joined"] = pd.to_datetime(companies["Date Joined"])


# In[11]:


# Use .info() to confirm that the update actually took place

### YOUR CODE HERE ###
companies.info()


# ### Create a `Year Joined` column
# 
# It is common to encounter situations where you will need to compare the year joined with the year founded. The `Date Joined` column does not just have year—it has the year, month, and date. Extract the year component from the `Date Joined` column and add those year components into a new column to keep track of each company's year joined.

# In[12]:


# Step 1: Use .dt.year to extract year component from Date Joined column
# Step 2: Add the result as a new column named Year Joined to the DataFrame

### YOUR CODE HERE ###
companies["Year Joined"] = companies["Date Joined"].dt.year


# In[13]:


# Use .head() to confirm that the new column did get added

### YOUR CODE HERE ###
companies.head(10)


# ## Step 4: Results and evaluation
# 

# ### Take a sample of the data
# 
# It is not necessary to take a sample of the data in order to conduct the visualizations and EDA that follow. But you may encounter scenarios in the future where you will need to take a sample of the data due to time and resource limitations. For the purpose of developing your skills around sampling, take a sample of the data and work with that sample for the next steps of analysis you want to conduct. Use the `sample()` function for this task.

# In[51]:


# Step 1: Use sample() with the n parameter set to 50 to randomly sample 50 unicorn companies from the data. 
# Specify the random_state parameter so that if you run this cell multiple times, you get the same sample each time. 
# Step 2: Save the result in a new variable.

### YOUR CODE HERE ###
rand_sample = companies.sample(n = 50 , random_state = 50 )
rand_sample


# ### Visualize the time it took companies to reach unicorn status
# 
# Visualize the longest time it took companies to reach unicorn status for each industry represented in the sample. To create a bar plot to visualize this, use the `bar()` function from the `matplotlib.pyplot` module.

# In[52]:


# Create bar plot
# with Industry column as the categories of the bars
# and the difference in years between Year Joined column and Year Founded column as the heights of the bars

### YOUR CODE HERE ###
plt.bar(x = rand_sample["Industry"] , height = (rand_sample["Year Joined"] - rand_sample["Year Founded"]) , label = "Time To Join The Stock Market" )
plt.plot()
# Set title

### YOUR CODE HERE ###
plt.title("Time To Join The Stock Market")

# Set x-axis label
### YOUR CODE HERE ###
plt.xlabel("The Industry")

# Set y-axis label
### YOUR CODE HERE ###

plt.ylabel("Num Of Year")

# Rotate labels on the x-axis as a way to avoid overlap in the positions of the text

### YOUR CODE HERE ###
plt.xticks(rotation = 90)

# Display the plot

### YOUR CODE HERE ###
plt.show()


# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# Refer to what you have learned about creating bar plots as part of [exploratory data analysis](https://www.coursera.org/learn/go-beyond-the-numbers-translate-data-into-insight/lecture/4k4Vg/eda-using-basic-data-functions-with-python).
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 2</strong></h4></summary>
# 
# There is a function in the `matplotlib.pyplot` module that allows you to create a bar plot, specifying the category and height for each bar. 
# 
# There are functions in the `matplotlib.pyplot` module that allow you to set the title, x-axis label, and y-axis label of plots. In that module, there are also functions for rotating the labels on the x-axis and displaying the plot. 
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 3</strong></h4></summary>
# 
# You can use the `plt.bar()` to create the bar plot, passing in the categories and heights of the bars.
# 
# You can use `plt.title()`, `plt.xlabel()`, and `plt.ylabel()` to set the title, x-axis label, and y-axis label, respectively. 
# 
# You can use `plt.xticks()` to rotate labels on the x-axis of a plot. The parameters `rotation=45, horizontalalignment='right'` can be passed in to rotate the labels by 45 degrees and align the labels to the right. 
# 
# You can use `plt.show()` to display a plot.
# 
# </details>

# In[53]:


rand_sample["Value_in_num"] = pd.to_numeric(rand_sample["Valuation"].str.slice(1,-2))


# In[54]:


rand_sample.info()


# **Question:** What do you observe from this bar plot?

# * **The other Item has the highest number of defrence to join the market**

# ### Visualize the maximum unicorn company valuation per industry
# 
# Visualize unicorn companies' maximum valuation for each industry represented in the sample. To create a bar plot to visualize this, use the `bar()` function from the `matplotlib.pyplot` module. Before plotting, create a new column that represents the companies' valuations as numbers (instead of strings, as they're currently represented). Then, use this new column to plot your data.

# In[55]:


# Create a column representing company valuation as numeric data
companies["compnay value"] = companies["Valuation"].str.slice(1,-1)
companies.info()


# In[62]:


companies["compnay value"] = pd.to_numeric(companies["compnay value"])
Grouped = companies.groupby("Industry").sum()
Grouped


# In[66]:


# Create bar plot
# with Industry column as the categories of the bars
# and new valuation column as the heights of the bars
plt.bar(x= Total_industry.index ,height= Total_industry["compnay value"])

# Set title
plt.title("Values Of Companies By Industry")

# Set x-axis label
plt.xlabel("Industry")

# Set y-axis label
plt.ylabel("compnay value")


# Rotate labels on the x-axis as a way to avoid overlap in the positions of the text  
plt.xticks(rotation = 90)

# Display the plot
plt.show()


# In[ ]:


companies["compnay value"] = pd.to_numeric(companies["compnay value"])


# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# Refer to what you have learned about creating bar plots as part of [exploratory data analysis](https://www.coursera.org/learn/go-beyond-the-numbers-translate-data-into-insight/lecture/4k4Vg/eda-using-basic-data-functions-with-python).
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 2</strong></h4></summary>
# 
# Use the function in the `matplotlib.pyplot` module that allows you to create a bar plot, specifying the category and height for each bar. 
# 
# Use the functions in the `matplotlib.pyplot` module that allow you to set the title, x-axis label, and y-axis label of plots. In that module, there are also functions for rotating the labels on the x-axis and displaying the plot. 
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 3</strong></h4></summary>
# 
# Use the `plt.bar()` to create the bar plot, passing in the categories and heights of the bars.
# 
# Use `plt.title()`, `plt.xlabel()`, and `plt.ylabel()` to set the title, x-axis label, and y-axis label, respectively. 
# 
# Use `plt.xticks()` to rotate labels on the x-axis of a plot. The parameters `rotation=45, horizontalalignment='right'` can be passed in to rotate the labels by 45 degrees and align the labels to the right. 
# 
# Use `plt.show()` to display a plot.
# 
# </details>

# **Question:** What do you observe from this bar plot? 

# * **Fintech is the highest valued companies in the market**

# ## Considerations

# **What are some key takeaways that you learned from this lab?**

# * **change the data types, to datetime, numeric, object**
# * **exctract the year, month, num of weeks, days, from a datetime type**
# * **convert the month from number to be words**
# * **slicing the column**
# * **group values, using index in ploting**
# * **Rotate teh columns overlap, to represent the column**

# **What findings would you share with others?**

# [Write your response here. Double-click (or enter) to edit.]

# **What recommendations would you share with stakeholders based on these findings?**

# [Write your response here. Double-click (or enter) to edit.]

# **References**
# 
# Bhat, M.A. (2022, March). [*Unicorn Companies*](https://www.kaggle.com/datasets/mysarahmadbhat/unicorn-companies). 
# 
# 
