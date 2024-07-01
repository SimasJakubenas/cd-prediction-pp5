import streamlit as st

def predict_heart_disease(X_live, heart_disease_predictors, hear_disease_pipe_dc_fe, heart_disease_model):

	# from live data, subset features related to this pipeline
	X_live_heart_disease = X_live.filter(heart_disease_predictors)

	# predict
	heart_disease_prediction_proba = heart_disease_model.predict(X_live_heart_disease)

	# create a logic to display the results
	proba = heart_disease_prediction_proba
	if proba == [1]:
		proba = '**Present**'
	else:
		proba = '**Absent**'

	statement = (
		f'### With the values given, we estimate that the Heart Disease is {proba} '
	)

	st.write(statement)

# The code above was copied from the Churnometer Project from Code Institute 
# and was made to fit this project