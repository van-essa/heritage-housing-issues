import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.page_1_summary import page_1_summary_body
from app_pages.page_2_sale_price_study import page_2_sale_price_study_body
from app_pages.page_3_predict import page_3_predict_body
from app_pages.page_4_hypothesis_and_validation import page_4_hypothesis_and_validation_body
from app_pages.page_5_ml_predict import page_5_ml_predict_body

app = MultiPage(app_name= "Heritage Housing") # Create an instance of the app 

# Add your app pages here using .add_page()
app.app_page("Project Summary", page_1_summary_body)
app.app_page("House Sale Price Study", page_2_sale_price_study_body)
app.app_page("Predict House Value", page_3_predict_body)
app.app_page("Project Hypothesis and Validation", page_4_hypothesis_and_validation_body)
app.app_page("ML: Predict House Value", page_5_ml_predict_body)

app.run() # Run the  app

# code copied from Code Institute's Churnornmeter Project with some adjustments