# Cigar Recommendation Application

## Project Motivation
I am a cigar afficianado who enjoys exploring new cigars. There are over 2000 different brands of cigars on the market and finding a few that match my preferences can be a daunting task. I realized that other people who enjoy cigars may have the same dilemma and would get a lot of value out of a finely tuned cigar recommender. As the project evolved, I realized there was an opportunity to earn a commission on cigars purchased after clicking on a affiliate link in my recommendation application.

## Data Source
Cigars International Website https://www.cigarsinternational.com/

## Process Overview
* Collect data by webscraping the largest online cigar retailer
* Explore data for insights that may contribute to an effective model
* Process and clean data for it to be in a usable format for modeling
* Model the data so it returns the best possible recommendations

## Process Details
There are four notebooks in this repository:
1. Acquire Data
In this notebook all the webscraping is executed. Specifically, product names, attributes, and text descriptions are stored in a dictionary and then prepared for EDA in a dataframe.

2. EDA
This notebook is dedicated to finding what the data looks like and preparing it for processing. Examples of processes included in this section include finding null values, creating dataframes of relevant attributes, encoding and imputing to fill null values, visualizing attribute qualities, and creating a WordCloud of the most relevant product descriptive words. At the end of this notebook there is a section dedicated to NLP analysis of text data that was not used in the final model.

3. Processing
The processing notebook expands off the EDA section by standardizing the data and scaling it in order to be used in a model. Count vectorization and MinMax scaling were employed on attributes that had many variations.

4. Model
This notebook deployed a k-nearest neighbors algorithm with a weighted Minkowski metric. The weights are used to give less weight to flavor characteristics and more weight to sweet and flavored attributes. Cigars that are sweet or flavored are distinctly different from traditional cigars. The final section of this notebook is dedicated to preparing the data to be used in a web based application.

## Conclusions 
* This projects outcome is subjective considering the recommendation algorithm was not trained on labeled data. I am a cigar enthusiast who has been enjoying cigars for over 20 years. I have found the results of the predictions to be highly accurate with very good recommendations. I have also verified the results in many online communities with positive feedback.
* The algorithm did a good job of recommending cigars that had similar attributes, while keeping sweet and flavored cigars in a category of their own.
* Cigars brands offered to consumers change frequently. When starting on this project, there were 200 fewer cigars in my data than when running it again several months later. In order to keep the application relevant, this project should be executed with regular frequency, possibly quarterly.
* Next steps include monetizing the application with affiliate links and completing a cigar to whisky recommendation functionality.
