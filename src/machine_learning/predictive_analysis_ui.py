import streamlit as st


def predict_sale_price(X_live, house_features, sale_price_pipeline):

    # from the live data, subset features related to this pipeline
    X_live_sale_price = X_live.filter(house_features)

    # apply the pipeline to the live data and predict sale price
    # predict
    sale_price_prediction = sale_price_pipeline.predict(X_live_sale_price)

       # create a statement to display the results
    statement = (
        f'The predicted sale price for the house based on the '
        f'provided feature values is: **{sale_price_prediction}**.'
    )