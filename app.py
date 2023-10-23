import streamlit as st
from app_pages.multipage import MultiPage

# load page scripts
from app_pages.page_summary import page_summary_body
from app_pages.page_sale_price_study import page_sale_price_study_body
# from app_pages.page_sale_price_predictor import page_sale_price_predictor_body
from app_pages.page_project_hypotheses import page_project_hypotheses_body
# from app_pages.page_predict_price_ml import page_predict_price_ml_body

# create an instance of the app
app = MultiPage(app_name = "Housing Price Predictor")

# add app pages
app.add_page("Project Summary", page_summary_body)
app.add_page("House Sale Price Study", page_sale_price_study_body)
# app.add_page("House Sale Price Predictor", page_sale_price_predictor_body)
app.add_page("Project Hypotheses and Validation", page_project_hypotheses_body)
# app.add_page("ML: House Price Prediction", page_predict_price_ml_body)

# run the app
app.run()