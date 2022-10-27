import streamlit as st
import pandas as pd
from sklearn.metrics import r2_score, mean_absolute_error 
import numpy as np

def regression_performance(X_train, y_train, X_test, y_test,pipeline):
	st.write("Model Evaluation \n")
	st.info("Train Set")
	regression_evaluation(X_train,y_train,pipeline)

	st.info("Test Set")
	regression_evaluation(X_test,y_test,pipeline)

def regression_evaluation(X,y,pipeline):
  prediction = pipeline.predict(X)
  st.write('R2 Score:', r2_score(y, prediction).round(3))  
  st.write('Mean Absolute Error:', mean_absolute_error(y, prediction).round(3))


# code copied from Code Institute's Churnornmeter Project with some adjustments