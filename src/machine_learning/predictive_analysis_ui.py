import streamlit as st

def predict_sale_price(X_live, sale_price_features, sale_price_pipeline):

	# from live data, subset features related to this pipeline
	X_live_sale_price = X_live.filter(sale_price_features)

	# predict
	sale_price_prediction_proba = sale_price_pipeline.predict(X_live_sale_price)

	# create a logic to display the results
	proba = sale_price_prediction_proba
	value = float(proba.round(1))
	amount = '${:,.2f}'.format(value)
	statement = (
		f'### With the values given, we estimate this house to be worth {amount} '
	)

	st.write(statement)
		
	st.write(proba)

# code copied from Code Institute's Churnornmeter Project with some adjustments