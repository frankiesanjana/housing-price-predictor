import streamlit as st


def page_summary_body():
    """
    Function to display the contents
    of the project summary page
    """
    st.write("### Project Summary")

    # text based on README file - "Dataset Content" section
    st.info(
        f"Housing Price Predictor is a project developed to predict the sale "
        f"price of houses in Ames, Iowa, USA, based on attributes of the "
        f"houses.\n"
        f"The project encompasses both data analysis and machine learning "
        f"components.\n"
        f"* Through data analysis, it provides insights into the factors "
        f"influencing housing prices, and quantifies their impact.\n"
        f"* The machine learning aspect allows users to input property "
        f"information via the dashboard and receive a prediction of the "
        f"expected sale price of that property.\n\n"
        f"**Project Terms & Jargon**\n"
        f"* **Sale price** of a property is the current market price, in "
        f"US dollars, of a property with various attributes.\n"
        f"* **Inherited property** is a property that the client has "
        f"inherited, and wishes to sell for the maximum price achievable.\n"
        f"* Although not strictly 'terms and jargon', we add a note here "
        f"to remind users that all price data within this project are in "
        f"US dollars and all areas are measured in square feet.\n\n"
        f"**Project Dataset**\n"
        f"* The dataset represents **housing records from Ames, Iowa**, "
        f"containing 1,460 observations on the profile of each house "
        f"(including metrics relating to size, quality, age and condition), "
        f"and the respective sale price of the house, "
        f"for houses built between 1872 and 2010.\n"
        f"* The project dataset is available on "
        f"[Kaggle](https://www.kaggle.com/codeinstitute/housing-prices-data) "
        f"via Code Institute.")

    # Link to README file to provide access to full project documentation
    st.write(
        f"* For additional information, please see the explanatory notes "
        f"in the [Project README file](https://github.com/frankiesanjana/"
        f"housing-price-predictor).")

    # copied from README file - "Business Requirements" section
    st.success(
        f"The project has 2 business requirements:\n"
        f"* **BR1** - The client is interested in discovering how the house "
        f"attributes correlate with the sale price. Therefore, the client "
        f"expects data visualisations of the correlated variables against "
        f"the sale price to show that.\n"
        f"* **BR2** - The client is interested in predicting the house sale "
        f"price from her four inherited houses, and any other house in "
        f"Ames, Iowa, USA.\n"
        f"* Data analysis is used to address the first of these requirements, "
        f"and has been successful in finding and visualising correlations "
        f"between the features and the sale price.\n"
        f"* **The ML model and pipeline address the second of these "
        f"requirements, and have been successful in meeting the criteria "
        f"required to fulfil this requirement.**"
        )
