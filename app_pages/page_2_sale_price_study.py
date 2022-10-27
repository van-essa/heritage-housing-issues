import streamlit as st
from src.data_management import load_house_data

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")



def page_2_sale_price_study_body():

    
    # load data
    df = load_house_data()

    # hard copied from churned customer study notebook
    vars_to_study = ['OverallQual', 'GrLivArea', 'YearBuilt', '1stFlrSF', 'GarageArea']

    st.write("### House Value Estimator")
    st.info(
        f"* The client is interested in understanding the patterns from the house sales data set, "
        f"so that the client can learn the most relevant variables correlated to SalePrice."
    )

    # inspect data
    if st.checkbox("Inspect Customer Base"):
        st.write(
            f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns, "
            f"printed below are the first 10 rows.")
        
        st.write(df.head(10))

    st.write("---")


    # Correlation Study Summary
    st.write(
        f"* A correlation study was conducted in the notebook to better understand how "
        f"the variables are correlated to SalePrice. \n"
        f"* Additional correlation studies were conducted to grasp the relation between "
        f"the quality of a house and the year it was built or remodeled. \n"
        f"* Also, a correlation study was conducted to display houses of a similar size "
        f"across different levels of overall quality against sale price. \n"
        f"Some of the most correlated variables to Sale Price are: **{vars_to_study}**"
    )

    # Text based on "02 - Sale Price Study" Notebook - "Conclusions and Next steps" section
    st.info(
        f"The correlation indications and plots in the noptebook are below. "
        f"It is indicated that: \n"
        f"* The sale price of a house is higher for larger houses (Ground Living Area). \n"
        f"* The sale price of a house is generally higher for homes of higher overall quality  "
        f"* The sale price of a house is sometimes higher if it was built recently. "
        f"This occurs due to the newer the house construction (Year Built or Remodel), "
        f"the higher generally in quality houses(Overall Quality). \n"
    )

    # Individual plots per variable
    if st.checkbox("Sale Price correlation per Variable"):
        df_eda = df.filter(vars_to_study + ['SalePrice'])
        target_var = 'SalePrice'
        regr_level_per_variable(df_eda, target_var)

    if st.checkbox("Overall Quality correlation against Year Built and Remodel"):
        quality_to_study = ['YearBuilt', 'YearRemodAdd']
        df_eda = df.filter(quality_to_study + ['OverallQual'])
        target_var = 'OverallQual'
        regr_level_per_variable(df_eda, target_var)

    if st.checkbox("Houses of Similar Area across Quality against Sale Price"):
        fig, axes = plt.subplots(figsize=(8, 5))
        fig = sns.lmplot(data=df, x="GrLivArea", y="SalePrice", ci=None, hue='OverallQual')
        plt.title(f"Houses of Similar Area across Quality", fontsize=20,y=1.05)
        st.pyplot(fig) 


def regr_level_per_variable(df_eda, target_var):
    
    for col in df_eda.drop([target_var], axis=1).columns.to_list():
            plot_numerical(df_eda, col, target_var)


def plot_numerical(df, col, target_var):
    fig, axes = plt.subplots(figsize=(8, 5))
    fig = sns.lmplot(data=df, x=col, y=target_var, ci=None) 
    plt.title(f"{col}", fontsize=20,y=1.05)
    st.pyplot(fig)

# The code above was copied from the Churnometer Project from Code Institute with some adjustments