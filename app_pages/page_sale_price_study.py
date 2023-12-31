import streamlit as st
import plotly.express as px
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import ppscore as pps
import seaborn as sns
from src.data_management import load_housing_data
sns.set_style("whitegrid")


def page_sale_price_study_body():
    """
    Displays sale price, correlated features and a checkbox
    to show the house sale price by variable
    """
    # load data
    df = load_housing_data()

    # hard copied from data analysis notebook
    vars_to_study = ['1stFlrSF', 'GarageArea', 'GarageYrBlt',
                     'GrLivArea', 'KitchenQual', 'MasVnrArea',
                     'OverallQual', 'TotalBsmtSF', 'YearBuilt',
                     'YearRemodAdd']

    st.write("### House Price Correlation Study (BR1)")
    st.info(
        f"* **BR1** - The client is interested in discovering how house "
        f"attributes correlate with the sale price. Therefore, the client "
        f"expects data visualisations of the correlated variables against "
        f"the sale price to show that."
    )

    # inspect the data
    if st.checkbox("Inspect Housing Data"):
        st.write(
            f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns. "
            f"The first 10 rows are shown below.")

        st.write(df.head(10))

    st.write("---")

    # Correlation Study Summary
    st.write(
        f"* A correlation study was conducted in the notebook to better "
        f"understand how the variables are correlated to the sale price "
        f"of a property. \n"
        f"The most correlated variables are: **{vars_to_study}**."
    )

    # Text based on "03 - Data Analysis" notebook
    st.info(
        f"The heatmaps below were created to highlight variables with "
        f"significant correlation. Heatmaps are displayed for Spearman "
        f"and Pearson correlations, as well as Predictive Power Score. "
        f"These provide an intuitive visualisation of the variables that "
        f"are most strongly correlated, highlighting patterns in the data "
        f"and enabling us to see relatively quickly which variables are the "
        f"most strongly correlated."
    )

    if st.checkbox("Heatmaps: Spearman, Pearson and PPS Correlations"):
        df_corr_pearson, \
            df_corr_spearman, \
            pps_matrix = calculate_corr_and_pps(df)
        display_corr_and_pps(df_corr_pearson=df_corr_pearson,
                             df_corr_spearman=df_corr_spearman,
                             pps_matrix=pps_matrix,
                             CorrThreshold=0.4, PPS_Threshold=0.2,
                             figsize=(12, 10), font_annot=10)

    st.info(
        f"Once the variables that were most highly correlated with sale price "
        f"had been identified, we were then able to plot graphs to show the "
        f"relationship between each of these variables and a house's sale "
        f"price. Before displaying these plots, we show a histogram of the "
        f"sale price, in order to better understand its distribution. "
        f"We see that: \n"
        f"* The target variable is positively skewed: the majority of sale "
        f"prices are clustered around the left tail of the distribution, "
        f"while the right tail of the distribution is longer. A small number "
        f"of properties have much higher sale prices than the average.\n"
        f"* Higher values of each variable are generally associated with "
        f"higher sale price. We can see three broad themes in the data:\n"
        f"* The size of a house is correlated with its sale price, with "
        f"larger properties having a higher value. This is reflected in "
        f"the scatter plots showing each of `1stFlrSF`, `GarageArea`, "
        f"`GrLivArea`, `MasVnrArea` and `TotalBsmtSF` plotted against "
        f"the target variable.\n"
        f"* The quality of a house is correlated with its sale price: "
        f"higher quality is associated with a higher value. This is seen "
        f"in the violin plots illustrating `KitchenQual` and `OverallQual` "
        f"against `SalePrice`.\n"
        f"* The age of a house is correlated with its sale price, with more "
        f"recently built or remodelled properties having a higher value. "
        f"This is apparent from the line plots showing each of the variables "
        f"`GarageYrBlt`, `YearBuilt` and `YearRemodAdd` plotted against the "
        f"target variable.\n"
    )

    df_eda = df.filter(vars_to_study + ['SalePrice'])
    target_var = 'SalePrice'

    st.write("#### Data visualisations")

    # Distribution of target variable
    if st.checkbox("Distribution of Target Variable"):
        display_target_hist(df_eda, target_var)

    # Individual plots for each variable
    if st.checkbox("Sale Price by Variable"):
        sale_price_by_variable(df_eda)


# Below are the functions used to display the dashboard plots
# in the page_sale_price_study_body function (above).
# These are adapted from notebook "03 Data Analysis"
# for use with the Streamlit dashboard.


def heatmap_corr(df, threshold, figsize=(20, 12), font_annot=8):
    if len(df.columns) > 1:
        mask = np.zeros_like(df, dtype=bool)
        mask[np.triu_indices_from(mask)] = True
        mask[abs(df) < threshold] = True

        fig, axes = plt.subplots(figsize=figsize)
        sns.heatmap(df, annot=True, xticklabels=True, yticklabels=True,
                    mask=mask, cmap='viridis',
                    annot_kws={"size": font_annot}, ax=axes,
                    linewidth=0.5
                    )
        axes.set_yticklabels(df.columns, rotation=0)
        plt.ylim(len(df.columns), 0)
        st.pyplot(fig)


def heatmap_pps(df, threshold, figsize=(20, 12), font_annot=8):
    if len(df.columns) > 1:
        mask = np.zeros_like(df, dtype=bool)
        mask[abs(df) < threshold] = True
        fig, ax = plt.subplots(figsize=figsize)
        ax = sns.heatmap(df, annot=True, xticklabels=True, yticklabels=True,
                         mask=mask, cmap='rocket_r',
                         annot_kws={"size": font_annot},
                         linewidth=0.05, linecolor='grey')
        plt.ylim(len(df.columns), 0)
        st.pyplot(fig)


def calculate_corr_and_pps(df):
    df_corr_spearman = df.corr(method="spearman")
    df_corr_spearman.type = "spearman"
    df_corr_pearson = df.corr(method="pearson")
    df_corr_pearson.type = "pearson"

    pps_matrix_raw = pps.matrix(df)
    pps_matrix = pps_matrix_raw.filter(['x', 'y', 'ppscore']) \
        .pivot(columns='x', index='y', values='ppscore')

    pps_score_stats = pps_matrix_raw.query("ppscore < 1") \
        .filter(['ppscore']).describe().T
    print("PPS threshold - check PPS score IQR to decide ")
    print("threshold for heatmap \n")
    print(pps_score_stats.round(3))

    return df_corr_pearson, df_corr_spearman, pps_matrix


def display_corr_and_pps(df_corr_pearson, df_corr_spearman,
                         pps_matrix, CorrThreshold, PPS_Threshold,
                         figsize=(20, 12), font_annot=8):

    print("\n")
    print("* Analyse how the target variable for the ML ")
    print("model is correlated with other variables")
    print("* Analyse multi-colinearity, that is, how the ")
    print("features are correlated among themselves")

    print("\n")
    print("*** Heatmap: Spearman Correlation ***")
    print("This evaluates monotonic relationship \n")
    heatmap_corr(df=df_corr_spearman, threshold=CorrThreshold,
                 figsize=figsize, font_annot=font_annot)

    print("\n")
    print("*** Heatmap: Pearson Correlation ***")
    print("This evaluates the linear relationship between ")
    print("two continuous variables \n")
    heatmap_corr(df=df_corr_pearson, threshold=CorrThreshold,
                 figsize=figsize, font_annot=font_annot)

    print("\n")
    print("*** Heatmap: Power Predictive Score (PPS) ***")
    print("PPS detects linear or non-linear relationships ")
    print("between two columns.\n")
    print("The score ranges from 0 (no predictive power) ")
    print("to 1 (perfect predictive power) \n")
    heatmap_pps(df=pps_matrix, threshold=PPS_Threshold,
                figsize=figsize, font_annot=font_annot)


def display_target_hist(df, target_var):
    """
    Creates a histogram to show the target variable
    """
    fig, axes = plt.subplots(figsize=(8, 6))
    sns.histplot(data=df, x=target_var, kde=True)
    plt.title(f"Distribution of {target_var}")
    plt.xlabel(f"{target_var}, US Dollars")
    plt.ylabel("Frequency")
    st.pyplot(fig)


def sale_price_by_variable(df):
    """
    Creates plots showing each variable against the
    target variable. Plot type is adjusted according
    to the variable type.
    """
    target_var = 'SalePrice'
    numerical_vars = ['1stFlrSF', 'GarageArea', 'GrLivArea',
                      'MasVnrArea', 'TotalBsmtSF']
    categorical_vars = ['OverallQual', 'KitchenQual']
    time_series_vars = ['GarageYrBlt', 'YearBuilt', 'YearRemodAdd']
    for col in df.columns:
        if col == target_var:
            continue

        if col in numerical_vars:
            # plot scatter plots for numerical vars
            fig, axes = plt.subplots(figsize=(8, 6))
            sns.scatterplot(data=df, x=col, y=target_var)
            plt.title(f"Scatter plot of {col} (sqft) vs. {target_var} (USD)")
            st.pyplot(fig)

        elif col in categorical_vars:
            # plot violin plots for categorical vars
            fig, axes = plt.subplots(figsize=(8, 6))
            sns.violinplot(data=df, x=col, y=target_var)
            plt.title(f"Violin plot of {col} vs {target_var} (USD)")
            plt.xlabel(col)
            plt.ylabel(target_var)
            st.pyplot(fig)

        elif col in time_series_vars:
            # plot line graphs for time series vars
            data_for_graphs = df[df[col] != 0]
            fig, axes = plt.subplots(figsize=(8, 6))
            sns.lineplot(data=data_for_graphs, x=col, y=target_var)
            plt.title(f"Line plot of {col} vs {target_var} (USD)")
            plt.xlabel(col)
            plt.ylabel(target_var)
            st.pyplot(fig)
