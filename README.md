# Property Price Prediction
[Price Prediction App](https://price--prediction-app.herokuapp.com)

A Machine Learning based project deployed on Heroku and developed with Python and streamlit library. Supervised Machine Learning problem, solved using Linear Regresssion with a **test accuracy of more than 85%**<br>

**Problem Statement -** Predict the property prices based on Information provided by user.
## Data
Dataset contains 9 variables (8 independent and 1 target) and more than 13000 records. Data is in tedious form and needs to be cleaned for further processing. <br>
So below is a snap of only 10 records from our data and it can be seen that there are a lot of ambiguities (highlighted) in data. I need to fix all this in order to make data suitable for machine learning process.

[<img src="screenshots/data.JPG" width="450"/>](screenshots/data.JPG)

## Exploring Data (EDA)
Before satarting any Data Science Project, knowing Problem Statement and the data one is going to work upon are must.<br>
Looking at problem statement it gets cleared enough how to proceed and what sort of data we need, from data present with us. <br>
So, **Exploratory Data Analysis (EDA)** comes in handy for data filtering.

### Types of Areas available
Here am working on Property data so it is best practice to know, what types of properties are there and what is there count. So for that am using plotting method to easily get an idea about the same. From graph it is clear that there are 3 types of properties and among them ***super built-up area*** type have the highest number of count i.e more than 9000.

[<img src="screenshots/area.JPG" width="450"/>](screenshots/area.JPG)

### Missing Values in Data
I need to handle missing values so that the data do not misbehave from its original conclusions. To know which variable have what count of missing values, again I will use plotting method but this time a heatmap so as to perfectly visualize missing values.

[<img src="screenshots/missing.JPG" width="450"/>](screenshots/missing.JPG)

### Price Distribution
Variable ***Price*** in data is target variable i.e we are going to predict the Price for property. Here am visualizing the how much price is distrbuted. For this I am using histogram.

[<img src="screenshots/price.JPG" width="450"/>](screenshots/price.JPG)

