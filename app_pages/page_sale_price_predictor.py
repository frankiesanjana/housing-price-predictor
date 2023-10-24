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
    sale_price_prediction = sale_price_pipeline.predict(df_inherited_filtered)
    df_inherited_filtered["Predicted Sale Price"] = sale_price_prediction

    st.write(df_inherited_filtered.head())

    summed_sale_price = round(df_inherited_filtered["Predicted Sale Price"].sum(), 2)

    st.success(
        f"* The total predicted sale price for the four inherited houses "
        f"is ${summed_sale_price}."
    )