import streamlit as st


def predict_sale_price(X_live, house_features, sale_price_pipeline):

    # from the live data, subset features related to this pipeline
    X_live_sale_price = X_live.filter(house_features)

    # apply the pipeline to the live data and predict the sale price
    sale_price_prediction = sale_price_pipeline.predict(X_live_sale_price)
    
    # format the predicted price to round and show dollar sign
    # we round to the nearest whole dollar
    sale_price_prediction = float(sale_price_prediction)
    predicted_sale_price = "${:,.0f}".format(sale_price_prediction)

    # create a statement to display the results
    statement = (
        f'The predicted sale price for the house based on the '
        f'provided attribute values is: **{predicted_sale_price}**.'
    )

    st.success(statement)