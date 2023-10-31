import streamlit as st


def page_project_hypotheses_body():
    """
    Displays the project hypotheses
    """

    st.write("### Project Hypotheses and Validation")

    # conclusions taken from "03 - Data Analysis" notebook
    st.success(
        f"**Hypothesis 1: The size of a house is positively correlated "
        f"with its sale price**\n"
        f"* **Correct.** We see from the correlation study that the size "
        f"of a house is correlated with its sale price, with larger "
        f"properties having a higher value.\n"
        f"This is reflected in the variables `1stFlrSF`, "
        f"`GarageArea`, `GrLivArea`, `MasVnrArea` and `TotalBsmtSF`.\n\n"

        f"**Hypothesis 2: The quality of a house is positively correlated "
        f"with its sale price**\n"
        f"* **Correct.** We see from the correlation study that the quality "
        f"of a house is correlated with its sale price: higher quality "
        f"is associated with a higher value. \n"
        f"This is seen in the variables `KitchenQual` and `OverallQual`.\n\n"

        f"**Hypothesis 3: The year of construction of a house is positively "
        f"correlated with its sale price (i.e., more recently constructed "
        f"houses have higher sale prices)**\n"
        f"* **Correct.** We see from the correlation study that the age of "
        f"a house is correlated with its sale price, with more recently built "
        f"or remodelled properties having a higher value. This is apparent "
        f"from the variables `GarageYrBlt`, `YearBuilt` and `YearRemodAdd`.\n"
        )
