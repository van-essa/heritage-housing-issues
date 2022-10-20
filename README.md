# Heritage Housing Issues

![](README_docs/image from the dashboad.png)

## Click [here](link to the dashboard) to live site.  

---

In this project, I've built a Data App with a Machine Learning User Interface (UI) combining: (1) Python packages for Machine Learning, Data Analysis and Data Visualization; and (2) Streamlit for fast Machine Learning prototyping. This project was created for my last milestone Project at Code Institute to showcase my knowledge to perform critical data analysis to generate valuable insights and deliver data-driven recommendations.

The project immerses you into an environment that fully reflects professional business requirements. It achieves this by encouraging you to reflect on the "whys" and the "hows" of a Machine Learning system that delivers tangible value to your organization. The UI and the data analysis are conducted in a way that aligns with the business requirements.

---
# Table of Contents
<details>
<summary>Table of Contents</summary>

* [Dataset Content(#dataset-content)
* [Business Requirements](#business-requirements)
* [Hypothesis and how to validate?](#hypothesis-and-how-to-validate?)
    * [Hypothesis One](#hypothesis-one)
    * [Hypothesis Two](#hypothesis-two)
    * [Hypothesis Two](#hypothesis-three)
* [Rationale to map the business requirements to the Data Visualizations and ML tasks](#rationale-to-map-the-business-requirements-to-the-data-visualizations-and-ml-tasks) 
    * [Business Requirement 1: Data Visualization and Correlation Study](#business-requirement-1:-data-visualization-and-correlation-study)
    * [Business Requirement 2: Classification, Regression, Cluster, Data Analysis](#business-requirement-2:-classification,-regression,-cluster,-data-analysis)
* [ML Business Case](#ml-business-case)
* [Dashboard Design](#dashboard-design)
    * [Pge 1](#page-1)
    * [Pge 2](#page-2) 
    * [Pge 3](#page-3)
    * [Pge 4](#page-4)
    * [Pge 5](#page-5)
    * [Pge 6](#page-6)
    * [Pge 7](#page-7)
* [Unfixed Bugs](#unfixed-bugs)
* [Deployment](#deployment) 
    * [Using Github & Gitpod](#using-github-&-gitpod)
    * [Forking the GitHub Repository](#forking-the-gitHub-repository) 
    * [Making a Local Clone](#making-a-local-clone) 
    * [Deployment To Heroku](#deployment-to-heroku) 
* [Main Data Analysis and Machine Learning Libraries](#main-data-analysis-and-machine-learning-libraries) 
* [Credits](#credits)
    * [Online resources](#online-resources)
    * [Tutorials and inspiration](#tutorials-and-inspiration) 
    * [People](#people)  
</details>
<hr>

---

## Dataset Content
* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/housing-prices-data). We created then a fictitious user story where predictive analytics can be applied in a real project in the workplace. 
* The dataset has almost 1.5 thousand rows and represents housing records from Ames, Iowa; indicating house profile (Floor Area, Basement, Garage, Kitchen, Lot, Porch, Wood Deck, Year Built) and its respective sale price for houses built between 1872 and 2010.

|Variable|Meaning|Units|
|:----|:----|:----|
|1stFlrSF|First Floor square feet|334 - 4692|
|2ndFlrSF|Second floor square feet|0 - 2065|
|BedroomAbvGr|Bedrooms above grade (does NOT include basement bedrooms)|0 - 8|
|BsmtExposure|Refers to walkout or garden level walls|Gd: Good Exposure; Av: Average Exposure; Mn: Mimimum Exposure; No: No Exposure; None: No Basement|
|BsmtFinType1|Rating of basement finished area|GLQ: Good Living Quarters; ALQ: Average Living Quarters; BLQ: Below Average Living Quarters; Rec: Average Rec Room; LwQ: Low Quality; Unf: Unfinshed; None: No Basement|
|BsmtFinSF1|Type 1 finished square feet|0 - 5644|
|BsmtUnfSF|Unfinished square feet of basement area|0 - 2336|
|TotalBsmtSF|Total square feet of basement area|0 - 6110|
|GarageArea|Size of garage in square feet|0 - 1418|
|GarageFinish|Interior finish of the garage|Fin: Finished; RFn: Rough Finished; Unf: Unfinished; None: No Garage|
|GarageYrBlt|Year garage was built|1900 - 2010|
|GrLivArea|Above grade (ground) living area square feet|334 - 5642|
|KitchenQual|Kitchen quality|Ex: Excellent; Gd: Good; TA: Typical/Average; Fa: Fair; Po: Poor|
|LotArea| Lot size in square feet|1300 - 215245|
|LotFrontage| Linear feet of street connected to property|21 - 313|
|MasVnrArea|Masonry veneer area in square feet|0 - 1600|
|EnclosedPorch|Enclosed porch area in square feet|0 - 286|
|OpenPorchSF|Open porch area in square feet|0 - 547|
|OverallCond|Rates the overall condition of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|OverallQual|Rates the overall material and finish of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|WoodDeckSF|Wood deck area in square feet|0 - 736|
|YearBuilt|Original construction date|1872 - 2010|
|YearRemodAdd|Remodel date (same as construction date if no remodeling or additions)|1950 - 2010|
|SalePrice|Sale Price|34900 - 755000|


---


## Business Requirements
As a good friend, you are requested by your friend, who has received an inheritance from a deceased great-grandfather located in Ames, Iowa, to  help in maximizing the sales price for the inherited properties.

Although your friend has an excellent understanding of property prices in her own state and residential area, she fears that basing her estimates for property worth on her current knowledge might lead to inaccurate appraisals. What makes a house desirable and valuable where she comes from might not be the same in Ames, Iowa. She found a public dataset with house prices for Ames, Iowa, and will provide you with that

* 1 - The client is interested in discovering how the house attributes correlate with the sale price. Therefore, the client expects data visualizations of the correlated variables against the sale price to show that.
* 2 - The client is interested to predict the house sales price from her 4 inherited houses, and any other house in Ames, Iowa.

---

## Hypothesis and how to validate?
* List here your project hypothesis(es) and how you envision to validate it (them)
### Hypothesis One
### Hypothesis Two
### Hypothesis Three


---

## Rationale to map the business requirements to the Data Visualizations and ML tasks
* ### Business Requirement 1: Data Visualization and Correlation Study
    - As a client, I want to inspect the data related to the house records to discover how the house attributes correlate with the sale price.
    - As a client, I want to conduct a correlation study(Pearson and Spearman) to understand better how the variables are correlated to Sale Price so that I can discover how the house attributes correlate with the sale price.
    - As a client, I want to plot the main variables against the Sale Price to Visualize insights, so I can discover how the house attributes correlate with the Sale Price.

* ### Business Requirement 2: Classification, Regression, Cluster, Data Analysis
    - As a client, I want to predict the Sale Price for a given house. We want to build an ML Model so the client can predict the house Sales Price from her four inherited dwellings and any other home in Ames, Iowa. 
    - As a client, want to build a regression model or change the ML task to classification depending on the regressor performance.

---


## ML Business Case
* In the previous bullet, you potentially visualized a ML task to answer a business requirement. You should frame the business case using the method we covered in the course 

---


## Dashboard Design
* List all dashboard pages and its content, either block of information or widgets, like: buttons, checkbox, image, or any other item that your dashboard library supports.
* Eventually, during the project development, you may revisit your dashboard plan to update a give feature (for example, in the beginning of the project you were confident you would use a given plot to display an insight but eventually you needed to use another plot type)
### Page 1 
### Quick project summary
	* Project Terms & Jargon
	* Describe Project Dataset
	* State Business Requirements

### Page 2
### Customer Base Churn Study
* Before the analysis, we knew we wanted this page to answer business requirement 1, but we couldn't know in advance which plots would need to be displayed.
* After data analysis, we agreed with stakeholders that the page will: 
	* State business requirement 1
	* Checkbox: data inspection on house attributes (display the number of rows and columns in the data, and display the first ten rows of the data)
	* Display the most correlated variables to Sale Price and the conclusions
	* Checkbox: Individual plots showing the Sale Price levels for each correlated variable 
	* Checkbox: Parallel plot using Sale Price and correlated variables 

### Page 3
### Prospect Churnometer
* State business requirement 2
* Set of widgets inputs, which relates to the prospect profile. Each set of inputs is related to a given ML task to predict prospect Sale Price, and Cluster.
* "Run predictive analysis" button that serves the prospect data to our ML pipelines, and predicts if the prospect will increase Sale Price or not, if so, when. It also shows to which cluster the prospect belongs and the cluster's profile. For the Sale Price predictions, the page will inform the associated probability for Sale Price level.

### Page 4
### Project Hypothesis and Validation
* Before the analysis, we knew we wanted this page to describe each project hypothesis, the conclusions, and how we validated each. After the data analysis, we can report that:
* 1 - ???
	* ???
* 2 -  ???
	* ???

### Page 5
### Predict Sale Price
* Considerations and conclusions after the pipeline is trained
* Present ML pipeline steps
* Feature importance
* Pipeline performance

### Page 6
### Predict ???
* Considerations and conclusions after the pipeline is trained
* Present ML pipeline steps
* Feature importance
* Pipeline performance

### Page 7
### Cluster Analysis
* Considerations and conclusions after the pipeline is trained
* Present ML pipeline steps
* Silhouette plot ???
* Clusters distribution across Sale Price levels
* Relative Percentage (%) of Sale Price in each cluster
* Most important features to define a cluster
* Cluster Profile

---

## Unfixed Bugs
* You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a big variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

---

## Deployment

The master branch of this repository has been used for the deployed version of this application.

### Using Github & Gitpod

To deploy my Data application, I had to use the [Code Institute Full Template](https://github.com/Code-Institute-Solutions/milestone-project-heritage-housing-issues).

- Click the `Use This Template` button.
- Add a repository name and brief description.
- Click the `Create Repository from Template` to create your repository.
- To create a Gitpod workspace you then need to click `Gitpod`, this can take a few minutes.
- When you want to work on the project it is best to open the workspace from Gitpod (rather than Github) as this will open your previous workspace rather than creating a new one. You should pin the workspace so that it isn't deleted.
-  Committing your work should be done often and should have clear/explanatory messages, use the following commands to make your commits:
    - `git add .`: adds all modified files to a staging area
    - `git commit -m "A message explaining your commit"`: commits all changes to a local repository.
    - `git push`: pushes all your committed changes to your Github repository.

### Forking the GitHub Repository

By forking the GitHub Repository you will be able to make a copy of the original repository on your own GitHub account allowing you to view and/or make changes without affecting the original repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](repo here???)
2. At the top of the Repository (not top of page) just above the "Settings" button on the menu, locate the "Fork" button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](repo here???)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open commandline interface on your computer
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone http..repo here???
```

7. Press Enter. Your local clone will be created.

### Deployment To Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly in case all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.

---


## Main Data Analysis and Machine Learning Libraries
* Here you should list the libraries you used in the project and provide example(s) on how you used these libraries.

|Libraries Used In The Project|How I Used The Library|Link|
|:----|:----|:----|
|Library|blablablabla|[Name](https://github.com/Code-Institute-Solutions/milestone-project-heritage-housing-issues)|
|Library|blablablabla|[Name](https://github.com/Code-Institute-Solutions/milestone-project-heritage-housing-issues)|
|Library|blablablabla|[Name](https://github.com/Code-Institute-Solutions/milestone-project-heritage-housing-issues)|
|Library|blablablabla|[Name](https://github.com/Code-Institute-Solutions/milestone-project-heritage-housing-issues)|
|Library|blablablabla|[Name](https://github.com/Code-Institute-Solutions/milestone-project-heritage-housing-issues)|
|Library|blablablabla|[Name](https://github.com/Code-Institute-Solutions/milestone-project-heritage-housing-issues)|
|Library|blablablabla|[Name](https://github.com/Code-Institute-Solutions/milestone-project-heritage-housing-issues)|

---

## Credits 

Throughout the process of building this website, various online sources have been used to help fix bugs & tackle problems, in addition to multiple modules to create the functionality of this website:

### Online resources
* John Ade-Ojo's blog post on the towardsdatascience online source regarding [creating a model to predict house prices](https://towardsdatascience.com/predicting-house-prices-with-machine-learning-62d5bcd0d68f)
* Exploratory Data Analysis of Iowa Housing Price Prediction Problem blop post from [Revathi Suriyadeepan](https://medium.com/analytics-vidhya/exploratory-data-analysis-of-iowa-housing-price-prediction-problem-3d50a016797a)
* Categorical encoding using Label-Encoding and One-Hot-Encoder from [Dinesh Yadav](https://towardsdatascience.com/categorical-encoding-using-label-encoding-and-one-hot-encoder-911ef77fb5bd)
* 

### Tutorials and inspiration

* The walkthrough project 'Churnometer ' from Code Institute [videos](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+DDA101+2021_T4/courseware/bba260bd5cc14e998b0d7e9b305d50ec/c83c55ea9f6c4e11969591e1b99c6c35/).
* How to predict House Prices in Ames, Iowa | Kaggle Competition in Data Science & Machine Learning [YouTube Video](https://www.youtube.com/watch?v=VSeGseoJsNA&ab_channel=AlexanderHess-Pythonista) from Alexander Hess, PhD Student atWHU - Otto Beisheim School of Management, Vallendar, Germany 
* 

### People

* 


