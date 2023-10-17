# Housing Price Predictor

Housing Price Predictor is a project developed to predict the sale price of houses in Ames, Iowa, USA, based on attributes of the houses.

This project has been created for the fifth portfolio project for Code Institute's Diploma in Full Stack Software Development, in the Predictive Analytics specialisation. The project is written in Python using Jupyter Notebooks with dashboard development using Streamlit, and is deployed with Heroku.

The project encompasses both data analysis and machine learning components. Through data analysis, it provides insights into the factors influencing housing prices, and quantifies their impact. The machine learning aspect allows users to input property information via the dashboard and receive a prediction of the expected sale price of that property.

The live application can be found [xxx](link).

## Business Requirements

Our client has received an inheritance comprising four houses located in Ames, Iowa, USA. While she has a strong understanding of property prices in her home country of Belgium, she is uncertain about accurately estimating property values in the Iowan real estate market. She is concerned that her knowledge of what makes a house desirable and valuable in Belgium might not be applicable to Ames, Iowa.

The client's primary objective is to maximise the sales price for the inherited properties. She has found a public dataset with house prices for Ames, Iowa, and has provided this to us. She is also interested in predicting the sale price from any house in Ames, Iowa in case of future property ownership in that area.

As such, two business requirements have been agreed with the client:

* **BR1** The client is interested in discovering how the house attributes correlate with the sale price. Therefore, the client expects data visualizations of the correlated variables against the sale price to show that.
* **BR2** The client is interested in predicting the house sales price from her four inherited houses, and any other house in Ames, Iowa.

## Dataset Content
* The dataset for this project is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/housing-prices-data). A fictitious user story was created, where predictive analytics can be applied as in a real project in the workplace. 
* The dataset has 1460 observations and represents housing records from Ames, Iowa, indicating house profile (Floor Area, Basement, Garage, Kitchen, Lot, Porch, Wood Deck, Year Built) and its respective sale price for houses built between 1872 and 2010.
* The variables contained in the dataset (both features and target) are described in the table below.

|Variable|Meaning|Units|
|:----|:----|:----|
|1stFlrSF|First Floor square feet|334 - 4692|
|2ndFlrSF|Second-floor square feet|0 - 2065|
|BedroomAbvGr|Bedrooms above grade (does NOT include basement bedrooms)|0 - 8|
|BsmtExposure|Refers to walkout or garden level walls|Gd: Good Exposure; Av: Average Exposure; Mn: Minimum Exposure; No: No Exposure; None: No Basement|
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
|YearRemodAdd|Remodel date (same as construction date if no remodelling or additions)|1950 - 2010|
|SalePrice|Sale Price|34900 - 755000|

## Hypotheses and how we validated them?

**Project hypotheses and their validation processes**

The following hypotheses were developed based on general knowledge of housing and of what features are likely to correlate with higher sale price of a property, in combination with the available features in the dataset (for example, we suspect that the precise location of a properly is likely to be highly relevant, but none of the features in the dataset provides detailed information regarding location, so this is not referenced in our hypotheses).
* The hypotheses relate to correlation. Note that they do not reference causation, since correlation in and of itself does not prove causation, although in this case it is highly likely that there is a causative relationship.
* The hypotheses were validated as follows:
    - Once the hypotheses had been clearly stated, the dataset needed to be examined for evidence of the hypothesised correlations.
    - The dataset was imported (notebook 1) and cleaned (notebook 2) in order for the data analysis to take place (notebook 3).
    - To examine our hypotheses, we then analysed Spearman and Pearson correlations between the different variables, as well as the Predictive Power Score ("PPS").
    - For ease of visualisation, these correlations were represented in heatmaps. For Spearman and Pearson correlations, a correlation threshold of 0.4 was set, and for Predictive Power Score a threshold of 0.2.
    - We then examined the heatmaps for evidence of correlation between the relevant variables. In each case, we were looking at the correlation coefficients between the features (input variables) and the target variable of `SalePrice`.
    - Since Spearman and Pearson correlations are widely recognised and understood, we looked for evidence to support our hypotheses here first. These provided at least adequate evidence to support the hypothesese in all cases; however, where there was a gap or where we felt that further supporting evidence might be valuable, we also looked to the PPS heatmap for any further information it might be able to provide.

**Hypothesis 1: The size of a house is positively correlated with its sale price**
* There are several variables that relate to the size of a house. Both Spearman and Pearson correlations show positive correlation betwen these variables and the sale price. For example, we see from our Spearman and Pearson heatmaps that:
    - `1stFlrSF` has a Spearman correlation coefficient of 0.58 and a Pearson correlation coefficient of 0.61 with `SalePrice`.
    - `GarageArea` has a Spearman correlation coefficient of 0.65 and a Pearson correlation coefficient of 0.62 with `SalePrice`.
    - `GrLivArea` has a Spearman correlation coefficient of 0.73 and a Pearson correlation coefficient of 0.71 with `SalePrice`.
    - Other variables relating to property size, such as `LotArea`, `MasVnrArea`, `OpenPorchSF` and `TotalBsmtSF` also show positive Spearman and / or Pearson correlation coefficients with `SalePrice`.
    - In combination, these findings provide solid validation of the hypothesis that larger houses tend to have higher sale prices.
    - We conclude that the size of a house is positively correlated with its sale price.

**Hypothesis 2: The quality of a house is positively correlated with its sale price**
* The variables that relate to the quality of a house are `OverallQual` and `KitchenQual`. We see from our Spearman and Pearson heatmaps that:
    - `OverallQual` has a Spearman correlation coefficient of 0.81 and a Pearson correlation coefficient of 0.79 with `SalePrice`.
    - `KitchenQual` does not have a high enough correlation coefficient with `SalePrice` to appear on our heatmaps, where the threshold for positive correlation is 0.4.
    - However, we see from the Power Predictive Score heatmap that both `OverallQual` and `KitchenQual` have reasonable correlations with `SalePrice` of 0.44 and 0.26 respectively.
    - If our hypothesis is true, we would in any case expect the overall quality of a house to have more correlation with its value than the quality of one room only. The correlation coefficients to `SalePrice` for both Spearman and Pearson correlations are strong. We can therefore also validate this hypothesis.
    - We conclude that the quality of a house is positively correlated with its sale price.

**Hypothesis 3: The year of construction of a house is positively correlated with its sale price (i.e., more recently constructed houses have higher sale prices)**
* The main variable relating to the age of a house is `YearBuilt`. We could also consider remodelling of a property (`YearRemodAdd`) and the year its garage was constructed (`GarageYrBlt`) to seek supporting evidence.
    - `YearBuilt` has a Spearman correlation coefficient of 0.65 and a Pearson correlation coefficient of 0.52 with `SalePrice`.
    - `YearRemodAdd` also shows correlation; it has a Spearman correlation coefficient of 0.57 and a Pearson correlation coefficient of 0.51 with `SalePrice`.
    - `GarageYrBlt` has a Spearman correlation coefficient of 0.63 with `SalePrice`, though we note that it does not meet our threshold of 0.4 for Pearson correlation.
    - Again, there is enough evidence to conclude that our hypothesis is correct.
    - We conclude that the year of construction of a house is positively correlated with its sale price.

## The rationale to map the business requirements to the Data Visualisations and ML tasks

* The two business requirements that have been agreed with the client are:

* **BR1:** The client is interested in discovering how the house attributes correlate with the sale price. Therefore, the client expects data visualizations of the correlated variables against the sale price to show that.
* **BR2:** The client is interested in predicting the house sales price from her four inherited houses, and any other house in Ames, Iowa.

Based on these business requirements and considering the potential needs of the various types of user, a number of Epics and User Stories have been developed. The Epics also map to the CRISP-DM (Cross Industry Standard Process for Data Mining) workflow shown below:

<img src="assets/images/crisp-dm.png" alt="CRISP-DM process">

**Epic 1:** Business Understanding

**Epic 2:** Information gathering and data collection

**Epic 3:** Data visualisation, cleaning, and preparation

**Epic 4:** Model training, optimisation and validation

**Epic 5:** Dashboard planning, designing, and development

**Epic 6:** Dashboard deployment and release

* User Stories relating to BR1 are addressed in the [data analysis notebook](https://github.com/frankiesanjana/housing-price-predictor/blob/main/jupyter_notebooks/03-data-analysis.ipynb) and are as follows:
    - **US1:** As any user, I want to know which attributes of a house are most correlated with its sale price so that I can base my predictions on the most appropriate features.
        - Task: produce heatmaps for Spearman and Pearson correlations and Power Predictive Score, and note which input variables are most highly correlated with the sale price.
    - **US2:** As any user, I want to see graphs showing the relationship between the relevant input variables and the target variable, so that I can understand the relationships between sale price and other features.
        - Task: produce appropriate graphs (scatter graphs for numerical variables, violin plots for categorical variables and line graphs for time series variables) to illustrate the relationships between the relevant input variables and the target.
    - **US3:** As any user, I want to understand the project hypotheses and how they were validated, so that I can better understand the determinants of a property's sale price.
        - Task: interpret the data from the heatmaps described above and highlight how these data confirm the project hypotheses.

* User Stories relating to BR2 are addressed in the [modelling and evaluation notebook](https://github.com/frankiesanjana/housing-price-predictor/blob/main/jupyter_notebooks/05-modelling-evaluation.ipynb) and the dashboard, and are as follows:
    - **US4:** As the client, I want to be able to reliably predict the sale price of the houses I have inherited, so that I can sell them for the greatest possible price.
        - Task: conduct regression analysis using machine learning so that the sale price can be predicted from the most relevant features (note: regression analysis is a supervised ML task that is used to predict the value of the label from a set of related features)
        - Note: if the model's performance using regression analysis is poor, this could be changed to a classification problem: another supervised ML task, but where the category of a house's sale price is predicted rather than a value. Categories in this case could be in a format such as "up to and including price A", "between price A and price B", "equal to or greater than price B".
    - **US5:** As any user, I want to have interactive input widgets in my dashboard, so that I can provide new data relating to features of a house and obtain a prediction of its likely sale price.
        - Task: Develop a dashboard that provides the appropriate interface for the user to interact with the data and obtain a price prediction based on newly obtained information.
    - **US6:** As any user, I want to be able to access the pipelines that were used in the model, so that these can be used with new data and allow me to predict the sale price of houses that were not in the original dataset.
        - Task: Develop functionality that provides the pipelines and technology to the dashboard that enables the price prediction to function correctly based on new data that the user inputs.
    - **US7:** As a technical user, I want to understand the ML steps that were used to predict the sale price, so that I can understand the model that was used.
        - Task: Present clear information relating to the ML development process.
    - **US8:** As a technical user, I want to know the technical details relating to model performance, so that I can understand how reliable the predictions are.
        - Task: Note the model evaluation metrics and display the regression evaluation plots relating to train and test sets.

* User Stories relating to both BRs are addressed in the dashboard, and are as follows:
    - **US9:** As the client, I want to be able to access a dashboard that is easy to interpret and use, so that I can easily view the results of the analysis and modelling.
        - Task: Provide a dashboard to the client and ensure that it is clear and easy to use, with any necessary instructions provided to the user.
    - **US10:** As any user, I want the dashboard to be available online, so that it is readily accessible for all users.
        - Task: Deploy the dashboard to a web server or hosting platform such as Heroku for convenient access through a web browser.
    - **US11:** As any user, I want to understand the dataset that was used in the analysis and the model training, so that I understand the dataset and the quality and limitations of the analysis and modelling.
        - Task: Provide a clear description of the dataset in the dashboard.

## Machine Learning Business Case

[Articulate a Business Case for each Machine Learning task which must include the aim behind the predictive analytics task, the learning method, the ideal outcome for the process, success/failure metrics, model output and its relevance for the user, and any heuristics and training data used.]
[ensure proper ML terminology is used In the “ML Business Case” section at the README file, as described in the LMS section “Machine Learning Essentials” : “Machine Learning Terminology”]

* A Machine Learning model will be trained in order to meet the second business requirement (BR2).

* We want an ML model to predict the sale price in US dollars of properties in Ames, Iowa, USA.
    - The model should allow our client to predict the sale price of four houses that she has inherited.
    - It should also allow prediction of the sale price of other houses with similar attributes.

* Since we are predicting a value that is a continuous variable, using a number of predictor variables, the most appropriate ML task is linear regression (a supervised ML task).
    - The sale price is the target variable, i.e., the variable that we are interested in predicting.

* Our ideal outcome is to develop a model that will provide reliable predictions of the sale price of a house based on its known attributes.

* The model success metrics are:
    - **The model should achieve an R2 score of at least 0.75 on both train and test set.**
        - R2 is a statistical measure that describes the proportion of variance in the data that is explained by the model.
        - That is, it shows how well a regression model predicts the outcome of observed data.
        - Values range from 0 to 1.
        - As such, a R2 value of 0.75 means that the model provides a good, but not perfect, prediction of the target variable (sale price) based on the input variables.
    - The model will be considered to have failed if it does not achieve an R2 score of at least 0.75. In this case, other modelling techniques could be considered to try and develop a model that achieves a satisfactory performance.
    - We will also evaluate the mean absolute error, mean squared error and the root mean squared error.
        - However, these are not used separately to evaluate the model performance and are presented here for information only.

* The output is defined as a continuous value for sale price in US dollars.
    - Since the client wishes to find the total sale price for four inherited houses, we will also present the summed predicted sale price for the four houses. However, this will not be included in the live prediction of the model, since the user will enter data for one house at a time.

* Heuristics in general are problem-solving techniques that provide quick and approximate solutions when traditional, more complex methods might be slow or impractical.
    - Heuristics can also serve as preprocessing steps for more advanced machine learning models. For example, they can help in identifying relevant features or patterns that can be used in the development of a predictive model.
    - In this case, our client might base her first approximation of a house's sale price on the sale price of nearby houses that she observes with similar attributes.
    - We also note that she has a good understanding of property prices in her home country of Belgium. As a first approximation, then, she might expect that properties that would achieve high sale prices in Belgium would also achieve high sale prices in Ames, Iowa.
    - This type of analysis would allow the client to produce a rough estimate of the value of her properties.
    - However, she is interested in maximising the sale price for the properties, and as such would like a more detailed analysis, in order to provide a more accurate and reliable estimate of the likely sale price of the properties.
    - We therefore proceed with the development of a machine learning model.

* The training data are a public dataset with house prices for Ames, Iowa, that our client has found via an online search.
    - The dataset contains 1460 observations and 22 features.
    - We do not have information about the recency or reliability of these data, and we note that there are some missing values in the dataset, which have been handled in the [data cleaning notebook](https://github.com/frankiesanjana/housing-price-predictor/blob/main/jupyter_notebooks/02-data-cleaning.ipynb)
    - Ideally we would check whether the dataset is recent or not before proceeding, since house prices can fluctuate significantly over time, and would prefer a dataset whose reliability has been verified and which has no missing values. However, here we can simply note this as a possible limitation of our dataset, and hence our model and its predictions.

## Dashboard Design
* List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other items that your dashboard library supports.
* Eventually, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project you were confident you would use a given plot to display an insight but eventually you needed to use another plot type)
* Project Summary
    - Introduces project
    - Describes app functionality
    - Lists project terms and jargon
    - Describes dataset
    - Links to README
    - Lists business requirements
* House Price Correlation Study
    - Notes the business requirement answered by the correlation study
    - Allows inspection of dataset (via checkbox)
    - Notes the features with the highest correlation to sale price
    - Shows plots of correlation between each variable and `SalePrice`
        - violin plot for categorical
        - scatterplot for numerical
        - line graphs for time series
    - Shows Spearman and Pearson correlation heatmaps
    - Shows PPS score
    - Shows histogram of target variable `SalePrice`
    - Summarises findings
* Project Hypotheses and Validation
    - Lists hypotheses and summarises findings / validation
* House Price Predictor
    - Notes the business requirement answered by the house price predictor
    - Shows the four inherited houses' attributes and their predicted sale prices
    - Shows the summed predicted price for the four inherited houses
    - Contains interactive input widgets to allow the user to input data from further houses to predict the sale price
    - Displays a button to allow the user to predict the sale price of a house with the details they have added using the ML pipelines developed during the project
* ML: Housing Price Predictor
    - Summarises the aims, development process and findings of the ML process
    - Displays the ML pipeline to predict house sale price
    - Displays the features that the model was trained on and their importance in a bar chart
    - Displays the pipeline performance metrics: R2 score, MAE, MSE, RMSE, for each of the train and test sets
    - Displays regression evaluation plots showing the predicted and actual sale prices on train and test sets

## Unfixed Bugs
* You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a big variable to consider, paucity of time and difficulty understanding implementation is not valid reason to leave bugs unfixed.

## Deployment
### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

## Main Data Analysis and Machine Learning Libraries
* Here you should list the libraries you used in the project and provide example(s) of how you used these libraries.


## Credits 

* In this section, you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism. 
* You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign-Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The photos used on the home and sign-up page are from This Open Source site
- The images used for the gallery page were taken from this other open-source site



## Acknowledgements (optional)
* In case you would like to thank the people that provided support through this project.

