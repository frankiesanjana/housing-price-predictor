import streamlit as st
from app_pages.multipage import MultiPage

# load page scripts

# create an instance of the app
app = MultiPage(app_name = "Housing Price Predictor")

# add app pages

# run the app
app.run()