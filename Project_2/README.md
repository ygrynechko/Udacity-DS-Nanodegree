# Disaster Response Pipeline Project
 With the use of over 50 k historical tweets which were categorized we were able to build and train machine learning classification model that will allow us to classify future tweets. With help of this model organizations will be able to filter for relevant tweets and categorize them which will result in faster response to people in need. 

## Content
- Data
  - process_data.py: reads in the data, cleans and stores it in a SQL database. Basic usage is python process_data.py MESSAGES_DATA CATEGORIES_DATA NAME_FOR_DATABASE
  - disaster_categories.csv and disaster_messages.csv (dataset)
  - DisasterResponse.db: created database from transformed and cleaned data.
- Models
  - train_classifier.py: includes the code necessary to load data, transform it using natural language processing, run a machine learning model using GridSearchCV and train it. Basic usage is python train_classifier.py DATABASE_DIRECTORY SAVENAME_FOR_MODEL  
- App
  - run.py: Flask app and the user interface used to predict results and display them.
  - templates: folder containing the html templates
- ScreenShots
  - screenshots of the webapp 
- Notebooks
  - jupyter notebooks that show step by step how the data cleaning and model creation were done

## Example:
> python process_data.py disaster_messages.csv disaster_categories.csv DisasterResponse.db

> python train_classifier.py ../data/DisasterResponse.db classifier.pkl

> python run.py

## Screenshots
Text classification:
![Alt text](https://github.com/ygrynechko/Udacity_DS_Nanodegree/blob/master/Project_2/ScreenShots/clasiffication.png?raw=true "Screenshot1")

Basic graphs:
![Alt text](https://github.com/ygrynechko/Udacity_DS_Nanodegree/blob/master/Project_2/ScreenShots/graphs.png?raw=true "Screenshot2")

## About
This project was prepared as part of the Udacity Data Scientist nanodegree programme. The data was provided by Figure Eight. 
