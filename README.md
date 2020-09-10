# Grocery recommender
Work in progress

By Pepe Nunez

[final-project] - August 2020 - Data Analytics Bootcamp, Berlin

## Content
- [Project Description](#project)
- [Questions & Hypotheses](#questions)
- [Dataset](#dataset)
- [Workflow](#workflow)
- [Organization](#organization)
- [Links](#links)

## Project Description
<a name="project"/>
(1) Have you ever moved to a New city and didn't know where to fo your groceries?
(2) Do you struggle to find some ingredients-products in the supermarket?
(3) Are you bored of always buying the same ingredients or are one of those that always forget about some crucial ingredient?

In any case, I'll have you covered with this Grocery Recommender. I've decided to build an tool where you can provide a list of ingredients and will compare 6 differents supermarkets (REWE, Aldi north, Aldi south, Lidl, Edeka, Kaufland) and tell you where you'll be able to find the products that you are looking and the prices. Additionally, it will recommend you additional ingredients that you might be interested in buying based on the rating of other users. 

## Questions & Hypotheses
<a name="questions"/>
I'd like to build a tool that can help new visitors to Berlin to optimize their grocery shopping process. To do so, the tool must:
- Find the supermarket with highest product availability and lower prices
- Translate the ingredients to the product reference in each supermarket
- Recommend other products that the user might be interested in buying based on their current cart. 

## Datasets
<a name="dataset"/>
- **Allrecipes** (Kaggle) - https://www.kaggle.com/elisaxxygao/foodrecsysv1 - 52,821 recipes from 27 categories posted between 2000 and 2018. To ensure the quality of the data, we filter recipes that do not have images and that contain repeated ingredients and zero reviews. Then we obtain raw_data, including 1,160,267 users, 49,698 recipes with 38,131 ingredients and 3,794,003 interactions

- **Supermarkets** (Ironhack former student) - https://github.com/kklichowski/Third-Project - A former Student from the Data Analytics Bootcamp successfuly scraped https://www.supermarktcheck.de/ to obtain information about the products offered in REWE, Aldi north, Aldi south, Lidl, Edeka, Kaufland. The data includes:
- Name of ingredient (German)
- Price
- Quantity


## Workflow
<a name="workflow"/>


## Supermarket recommender / comparison / clusterization
- What is the total cost of ingredients needed for a homemage meal vs restaurant meal?
- What are the most common ingredients used?
- How are the categories distributed within the lists (fresh, ...)
- Types of users?
- Add nutritional factors?
- Add images to ingredient names?
- Bring (app recommend)
- Google Maps (supermarket)
- Foursquare & Yelp (supermarket)
- Recipe builder

## Organization
<a name="problems"/>

- **00_demo.ipynb**
- **01_allrecipes-cleaning.ipynb** - In this notebook I explore, clean and prepare the data from allrecipes. 
- **02_supermarkets-cleaning.ipynb** - In this notebook I explore, clean and prepare the data from the supermarkets. 
- **03_allrecipes-modeling.ipynb**
- **04_supermarkets-modeling.ipynb**
- **10_supermarkets-translation-dynamic.ipynb**
- **data-insights.ipynb**
- **sql_connection.ipynb**

## Links
<a name="links"/>

- [Presentation](https://github.com/pepenunez/final-project/blob/master/Grocery%20recommender.pdf)
- [Demo](https://github.com/pepenunez/final-project/blob/master/00_demo.ipynb)
