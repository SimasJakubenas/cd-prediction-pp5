import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_pkl_file
from src.machine_learning.evaluate_classification import classification_performance


def page5_ml_prediction_body():

    version = 'v1'
    # load needed files
    heart_disease_pipe_dc_fe = load_pkl_file(
        f'outputs/ml_pipeline/predict_heart_disease/{version}/clf_pipeline_data_cleaning_feat_eng.pkl')
    heart_disease_pipe_model = load_pkl_file(
        f"outputs/ml_pipeline/predict_heart_disease/{version}/clf_pipeline_model.pkl")
    heart_disease_feat_importance = plt.imread(
        f"outputs/ml_pipeline/predict_heart_disease/{version}/features_importance.png")
    X_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_heart_disease/{version}/X_train.csv")
    X_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_heart_disease/{version}/X_test.csv")
    y_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_heart_disease/{version}/y_train.csv").values
    y_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_heart_disease/{version}/y_test.csv").values

    st.write("### ML Pipeline: Predict Heart Disease presence")
    # display pipeline training summary conclusions
    st.info(
        f"* The pipeline was tuned aiming at least 0.98 Recall on 'HD Present' class, "
        f"since we are interested in this project in detecting a potential heart_diseaseer. \n"
        f"* The pipeline accuracy test set is 0.97, which surpasses the requirement by the client."
    )

    # show pipelines
    st.write("---")
    st.write("#### There are 2 ML Pipelines arranged in series.")

    st.write(" * The first is responsible for data cleaning and feature engineering.")
    st.write(heart_disease_pipe_dc_fe)

    st.write("* The second is for feature scaling and modelling.")
    st.write(heart_disease_pipe_model)

    # show feature importance plot
    st.write("---")
    st.write("* The features the model was trained and their importance.")
    st.write(X_train.columns.to_list())
    st.image(heart_disease_feat_importance)

    # We don't need to apply dc_fe pipeline, since X_train and X_test
    # were already transformed in the jupyter notebook (page5_ml_prediction.ipynb)

    # evaluate performance on train and test set
    st.write("---")
    st.write("### Pipeline Performance")
    classification_performance(X_train=X_train, y_train=y_train,
                    X_test=X_test, y_test=y_test,
                    pipeline=heart_disease_pipe_model,
                    label_map=["HD Absent", "HD Present"])


# The code above was copied from the Churnometer Project from Code Institute 
# and was made to fit this project