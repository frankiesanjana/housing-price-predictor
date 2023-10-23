import streamlit as st

def page_project_hypotheses_body():

    st.write("### Project Hypotheses and Validation")

    # conclusions taken from "03 - Data Analysis" notebook
    st.success(
        f"**Hypothesis 1: The size of a house is positively correlated with its sale price**\n"
        f"* **Correct.** We see from the correlation study that the size of a house is \n"
        f"correlated with its sale price, with larger properties having a higher value.\n"
        f"This is reflected in the variables `1stFlrSF`,\n"
        f"`GarageArea`, `GrLivArea`, `MasVnrArea` and `TotalBsmtSF`.\n\n"

        f"**Hypothesis 2: The quality of a house is positively correlated with its sale price**\n"
        f"* **Correct.** We see from the correlation study that the quality of a house is \n"
        f"correlated with its sale price: higher quality is associated with a higher value. \n"
        f"This is seen in the variables `KitchenQual` and `OverallQual`.\n\n"
        

        f"**Hypothesis 3: The year of construction of a house is positively correlated with its \n"
        f"sale price (i.e., more recently constructed houses have higher sale prices)**\n"
        f"* **Correct.** We see from the correlation study that the age of a house is \n"
        f"correlated with its sale price, with more recently built or remodelled properties \n"
        f"having a higher value. This is apparent from the variables `GarageYrBlt`, \n"
        f"`YearBuilt` and `YearRemodAdd`.\n"
        )