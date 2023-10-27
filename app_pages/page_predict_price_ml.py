import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_housing_data, load_pkl_file
from src.machine_learning.evaluate_regression import regression_performance, regression_evaluation_plots


def page_predict_price_ml_body():
    """
    Displays the ML pipeline and feature importance plot
    and the model's performance on train and test sets
    """
    # load the required files
    version = 'v1'
    sale_price_pipeline = load_pkl_file(
        f"outputs/ml_pipeline/predict_sale_price/{version}/regression_pipeline.pkl"
    )
    sale_price_feature_importance = plt.imread(
        f"outputs/ml_pipeline/predict_sale_price/{version}/feature_importance.png"
    )
    X_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_sale_price/{version}/X_train.csv")
    X_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_sale_price/{version}/X_test.csv")
    y_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_sale_price/{version}/y_train.csv").squeeze()
    y_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_sale_price/{version}/y_test.csv").squeeze()
    
    st.write("### ML Pipeline: Predict House Sale Price")    
    # display pipeline training summary conclusions
    st.info(
        f"* To fulfil BR2, we trained a regressor model to predict the sale price of "
        f"properties in Ames, Iowa based on a given set of attributes. "
        f"The pipeline was tuned aiming to ensure an R2 score of at least 0.75 "
        f"on both train and test sets.\n"
        f"* The pipeline performance for the best model on the train and test set is "
        f"an R2 score of 0.97 and R2 0.78 respectively, so it meets the performance "
        f"requirement indicated in the business case.\n"
        f"* The pipeline steps are displayed below. "
       )
    st.write("---")
    
    # show pipeline
    st.info(
        f"* A single pipeline has been created, combining data cleaning, "
        f"feature engineering, feature scaling and modelling: "
    )
    st.code(sale_price_pipeline)
    st.write("---")

    # show best features
    st.info("* The features the model was trained on and their importance:")
    st.write(X_train.columns.to_list())
    st.image(sale_price_feature_importance)
    st.write("---")
    
    # display pipeline performance metrics
    st.write("### Pipeline Performance")
    st.write("#### Performance goal of the predictions:\n")
    st.info(
        f"* We agreed with the client an R2 score of at least 0.75 \n"
        f"on both train and test sets.\n"
        f"* The pipeline performance shows that these performance "
        f"criteria have been met."
        )
    regression_performance(X_train=X_train, y_train=y_train,
                        X_test=X_test, y_test=y_test,
                        pipeline=sale_price_pipeline) 

    st.write("### Regression Performance Plots")
    st.info(
        f"* The regression performance plots below indicate that our model is "
        f"generally able to provide an acceptable indication of the sale price "
        f"of a house based on the input features, although we do note that the "
        f"model appears somewhat less effective for higher value houses."
        )
    regression_evaluation_plots(X_train=X_train, y_train=y_train, 
                                X_test=X_test, y_test=y_test, 
                                pipeline=sale_price_pipeline)  