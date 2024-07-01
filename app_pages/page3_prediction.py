import streamlit as st
import pandas as pd
from src.data_management import load_heart_disease_data, load_pkl_file
from src.machine_learning.predictive_analysis_ui import predict_heart_disease


# Adapted from van-essa and Code Institute's Churnometer walkthrough project

def page3_prediction_body():
    # load predict sale_price files
    version = 'v1'
    hear_disease_pipe_dc_fe = load_pkl_file(
        f'outputs/ml_pipeline/predict_heart_disease/{version}/clf_pipeline_data_cleaning_feat_eng.pkl')
    heart_disease_model = load_pkl_file(
        f"outputs/ml_pipeline/predict_heart_disease/{version}/clf_pipeline_model.pkl")
    heart_disease_predictors = (
        pd.read_csv(f"outputs/ml_pipeline/predict_heart_disease/{version}/X_train.csv")
        .columns
        .to_list())

    st.write("### Predict Heart Disease Presence")
    # display client's query and its data
    st.info(
        f"#### Business Requirement 2\n"
        f"* The client is interested in predicting whether or not a patient has Heart Disease ")

    st.write("The table below represents the relevant data supplied by the client to predict Heart Disease:")
	
    hd_df = load_heart_disease_data()
    filtered_df = hd_df[['slope', 'chestpain', 'noofmajorvessels', 'restingBP',
                    'restingrelectro', 'fastingbloodsugar']]	
		
    st.write(filtered_df)

    st.write("---")
    st.write("Enter the relevant values of the variables below to generate a Heart Disease Prediction. ")
	
    # Generate Live Data
    X_live = DrawInputsWidgets()

    # Predict live data
    if st.button("Run Predictive Analysis"): 
        predict_heart_disease(
            X_live, heart_disease_predictors, hear_disease_pipe_dc_fe, heart_disease_model)


def DrawInputsWidgets():

    # load dataset
    df = load_heart_disease_data()
    percentageMin, percentageMax = 0.4, 2.0

# we create input widgets only for 6 features
    col1, col2, col3, col4 = st.beta_columns(4)
    col5, col6, col7, col8 = st.beta_columns(4)

    # We are using these features to feed the ML pipeline - values copied from check_variables_for_UI() result

    # create an empty DataFrame, which will be the live data
    X_live = pd.DataFrame([], index=[0])

    # from here on we draw the widget based on the variable type (numerical or categorical)
    # and set initial values
    with col1:
        feature = "slope"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget

    with col2:
        feature = "chestpain"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget

    with col3:
        feature = "noofmajorvessels"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget

    with col4:
        feature = "restingBP"
        st_widget = st.number_input(
            label=feature,
            min_value=df[feature].min()*percentageMin,
            max_value=df[feature].max()*percentageMax,
            value=df[feature].median()
        )
    X_live[feature] = st_widget

    with col5:
        feature = "restingrelectro"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget

    with col6:
        feature = "fastingbloodsugar"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget

    # st.write(X_live)

    return X_live

# The code above was copied from the Churnometer Project from Code Institute 
# and was made to fit this project