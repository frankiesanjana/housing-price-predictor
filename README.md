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

Based on these business requirements and considering the potential needs of the user, a number of epics and user stories have been developed. These also map to the CRISP-DM (Cross Industry Standard Process for Data Mining) workflow shown below:

<img src="assets/images/crisp-dm.png" alt="CRISP-DM process">

Epic 1: Business Understanding

Epic 2: Information gathering and data collection

Epic 3: Data visualisation, cleaning, and preparation

Epic 4: Model training, optimisation and validation

Epic 5: Dashboard planning, designing, and development

Epic 6: Dashboard deployment and release

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

The following hypotheses were developed based on general knowledge of housing and of what features are likely to correlate with higher sale price of a property, in combination with the available features in the dataset (for example, we suspect that the location of a properly is likely to be highly relevant, but none of the features in the dataset provides information regarding location, so this is not referenced in our hypotheses).
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
* List your business requirements and a rationale to map them to the Data Visualisations and ML tasks.
[Map the business requirements in a User Story based format to each of the Data Visualization and ML Tasks along with the specific actions required for the enablement of each task.]
[Ensure at least 1 ML task is mentioned in the “Rationale to map the business requirements to the Data Visualizations and ML tasks” section in the README file.]


## ML Business Case
* In the previous bullet, you potentially visualised an ML task to answer a business requirement. You should frame the business case using the method we covered in the course.
[Articulate a Business Case for each Machine Learning task which must include the aim behind the predictive analytics task, the learning method, the ideal outcome for the process, success/failure metrics, model output and its relevance for the user, and any heuristics and training data used.]
[ensure proper ML terminology is used In the “ML Business Case” section at the README file, as described in the LMS section “Machine Learning Essentials” : “Machine Learning Terminology”]

We want an ML model to predict the sale price in US dollars of properties in Ames, Iowa, USA. The sale price is the target variable (also referred to as the label), i.e., the variable that we are interested in predicting.
Our ideal outcome is...
The model success metrics are...
The output is defined...
Heuristics...
The training data...

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

