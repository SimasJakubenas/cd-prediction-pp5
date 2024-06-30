import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.page1_summary import page1_summary_body
from app_pages.page2_heart_disease_study import page2_heart_disease_body
from app_pages.page3_prediction import page3_prediction_body
from app_pages.page4_hypothesis_and_validation import page4_hypothesis_and_validation_body
from app_pages.page5_ml_prediction import page4_ml_prediction_body

app = MultiPage(app_name= "PP5 - Heart Disease Predictor") # Create an instance of the app 

# Add your app pages here using .add_page()
app.app_page("Project Summary", page1_summary_body)
app.app_page("Heart Disease Study", page2_heart_disease_body)
app.app_page("Predict Heart Disease", page3_prediction_body)
app.app_page("Project Hypothesis and Validation", page4_hypothesis_and_validation_body)
app.app_page("ML: Predict Heart disease", page4_ml_prediction_body)

app.run() # Run the  app

# code copied from Code Institute's Churnornmeter Project and made to fit project