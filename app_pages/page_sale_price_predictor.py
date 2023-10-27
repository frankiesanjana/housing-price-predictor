import streamlit as st
import pandas as pd
import numpy as np
from src.data_management import load_housing_data, load_inherited_houses_data, load_pkl_file
from src.machine_learning.predictive_analysis_ui import predict_sale_price


def page_sale_price_predictor_body():

    # load the required files and create df for inherited properties
    version = 'v1'
    sale_price_pipeline = load_pkl_file(
        f"outputs/ml_pipeline/predict_sale_price/{version}/regression_pipeline.pkl"
    )
    house_features = (pd.read_csv(f"outputs/ml_pipeline/predict_sale_price/{version}/X_train.csv")
                      .columns
                      .to_list())
    df_inherited_houses = load_inherited_houses_data()
    
    # predict the sale price of inherited houses
    st.info("### Predicting sales price of inherited houses (BR2, part 1)")
    st.info(
       f"* **BR2** - The client is interested in predicting the house sale prices "
       f"from her 4 inherited houses, and any other house in Ames, Iowa."
	)
    # display the data for the inherited homes
    st.write(
        f"* The following table shows the features of the four properties "
        f"that have been inherited by our client:"
    )
    st.write(df_inherited_houses.head())
    st.write(
        f"* We then subset the most relevant features to be used for sale price "
        f"prediction, and display the predicted sale price for each house:"
    )
    df_inherited_filtered = df_inherited_houses.filter(house_features)
    sale_price_prediction = np.round(sale_price_pipeline.predict(df_inherited_filtered), 0)
    df_inherited_filtered["Predicted Sale Price"] = sale_price_prediction

    st.write(df_inherited_filtered.head())

    summed_sale_price = "${:,.0f}".format(df_inherited_filtered["Predicted Sale Price"].sum())

    st.success(
        f"* The total predicted sale price for the four inherited houses "
        f"is {summed_sale_price}."
    )
    st.write("---")
    # generate live data
    # predict the sale price of any other house in Ames, Iowa
    st.info("### Predicting sales price of any other house in Ames, Iowa (BR2, part 2)")
    st.info(
       f"* **BR2** - The client is interested in predicting the house sale prices "
       f"from her 4 inherited houses, and any other house in Ames, Iowa."
    )
    st.write(
        f"* To predict the sale price of another house, please enter values for the "
        f"following attributes of the house and click the 'Predict Sale Price' button:"
    )
    
    X_live = draw_input_widgets()

    # predict on live data
    if st.button("Predict Sale Price"):
        price_prediction = predict_sale_price(X_live, house_features, sale_price_pipeline)
    st.write("---")

def draw_input_widgets():
    """
    Defines the input widgets for the user to enter attributes to predict
    the sale price of any house in Ames, Iowa
    """
    # load dataset
    df = load_housing_data()
    # stipulate min and max percentage values for numerical vars
    percentage_min, percentage_max = 0.2, 3.0
    # create input widgets for the four most relevant features
    col1, col2 = st.beta_columns(2)
    col3, col4 = st.beta_columns(2)
    # these features are used to feed the ML pipeline
    # create an empty DataFrame, which will be the live data
    X_live = pd.DataFrame([], index=[0])
    # we now draw the widget based on the variable type
    # (numerical or categorical), and set initial values
    with col1:
        feature = "TotalBsmtSF"
        st_widget = st.number_input(
            label = feature,
            min_value = float(df[feature].min()*percentage_min),
            max_value = float(df[feature].max()*percentage_max),
            value = float(df[feature].median())
        )
    X_live[feature] = st_widget

    with col2:
        feature = "YearBuilt"
        # round the median to the nearest whole year
        median_value = round(df[feature].median())
        st_widget = st.number_input(
            label = feature,
            min_value = float(df[feature].min()),
            # set max to 2100, since by then our predictor will likely be obsolete
            max_value = 2100.0,
            value = float(median_value),
            # restrict input values to whole numbers only
            step = 1.0
        )
    X_live[feature] = st_widget

    with col3:
        feature = "2ndFlrSF"
        st_widget = st.number_input(
            label = feature,
            min_value = float(df[feature].min()*percentage_min),
            max_value = float(df[feature].max()*percentage_max),
            value = float(df[feature].median())
        )
    X_live[feature] = st_widget

    with col4:
        feature = "LotArea"
        st_widget = st.number_input(
            label = feature,
            min_value = float(df[feature].min()*percentage_min),
            max_value = float(df[feature].max()*percentage_max),
            value = float(df[feature].median())
        )
    X_live[feature] = st_widget

    return X_live