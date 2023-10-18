import streamlit as st
from app_pages.multipage import MultiPage

# load page scripts
from app_pages.page_summary import page_summary_body

# create an instance of the app
app = MultiPage(app_name = "Housing Price Predictor")

# add app pages
app.add_page("Project Summary", page_summary_body)

# run the app
app.run()