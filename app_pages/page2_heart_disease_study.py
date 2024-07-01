import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from feature_engine.discretisation import ArbitraryDiscretiser
from src.data_management import load_heart_disease_data

sns.set_theme(context='notebook', style='darkgrid', palette='flare')
COLOR = '#1d6edf'
BACKGROUND_COLOR = (0.063, 0.11, 0.173)
ACCENT_COLOR1 = '#09ab3b'
ACCENT_COLOR2 = 'red'


def page2_heart_disease_body():
    df = load_heart_disease_data()  
    target_var = 'target'
    vars_to_study = ['slope', 'chestpain', 'noofmajorvessels', 'restingBP',
                    'restingrelectro', 'fastingbloodsugar', 'serumcholestrol']

    st.write("### House Sale Price Study")
    st.info(
        f"#### Business Requirement 1\n"
        f"* The client is interested in discovering how listed variables are "
        f"correlated with presence of Heart Disease."
    )

    # inspect data
    if st.checkbox("Inspect Patient Data"):
        st.write(
            f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns."
            f"You can see the first 10 rows displayed below:")
        
        st.write(df.head(10))

    st.write("---")

    # Correlation Study Summary
    """Correlation Study Findings"""
    st.write(
        f"* Correlation studies were conducted to better understand how "
        f"the variables are correlated to  **`target`**. \n\n"
        f"* The most correlated variables to **`target`** are: **{vars_to_study}**"
    )

    # Text based on "02 - Heart Disease Study" Notebook - "Conclusions and Next steps" section
    st.info(
        f"* Almost all the patients who had the slope of the peak exercise at 'flat' "
        f"and 'downslope' values had Heart Disease \n"
        f"* Most of the patients who reported non-anginal or asymptomatic pain had "
        f"Heart Disease \n"
        f"* Most of the patients who had number of vessels affected set at values 2 "
        f"and 3 had Heart Disease \n"
        f"* Patients with Heart Disease typically had a higher resting blood preasure \n"
        f"* Most patients with probable or definite left ventricular hypertrophy value "
        f"in electrocardiogram results had Heart Disease \n"
        f"* Patients who had their fasting blood sugar levers above 120 mg/dl were more "
        f"likely to have a Heart Disease \n"
        f"* All patients with total cholesterol levels above 470 mg/dl had Heart Disease \n"
    )

    if st.checkbox("Show Classification Plots"):
        plot_heart_disease_correlation(df, target_var, vars_to_study)

    if st.checkbox("Show male with Heart Disease age distribution"):
        male_age_hd_bins(df)


def plot_heart_disease_correlation(df, target_var, vars_to_study):
    for col in vars_to_study:
        plot_numerical(df, col, target_var)
        print("\n\n")


# functions taken from 2nd Jupyter Notebook
def plot_numerical(df, col, target_var):
    plt.figure(figsize=(8, 5), facecolor=BACKGROUND_COLOR)
    # Set plot colors
    plot_coloring(plt)
    sns.histplot(data=df, x=col, hue=target_var, kde=True, element="step",
                palette=[ACCENT_COLOR1, ACCENT_COLOR2])
    plt.title(f"{col}", fontsize=20, y=1.05)
    st.pyplot(plt)  # Render the plot in Streamlit
    plt.show()


def plot_coloring(plt):
    plt.rcParams['text.color'] = COLOR
    plt.rcParams['axes.labelcolor'] = COLOR
    plt.rcParams['xtick.color'] = COLOR
    plt.rcParams['ytick.color'] = COLOR
    plt.rcParams['grid.color'] = COLOR

    ax = plt.axes()
    ax.set(facecolor=BACKGROUND_COLOR)
    plt.setp(ax.spines.values(), color=COLOR)


def male_age_hd_bins(df):
    # Create bins for age ranges
    plt.figure(figsize=(10, 5), facecolor=BACKGROUND_COLOR)
    age_map = [-np.Inf, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, np.Inf]
    disc = ArbitraryDiscretiser(binning_dict={'age': age_map})
    df_parallel = disc.fit_transform(df)
    n_classes = len(age_map) - 1
    classes_ranges = disc.binner_dict_['age'][1:-1]

    # Add labels to bins
    labels_map = {}
    for n in range(0, n_classes):
        if n == 0:
            labels_map[n] = f"20-{classes_ranges[0]}"
        elif n == n_classes-1:
            labels_map[n] = f"{classes_ranges[-1]}-80"
        else:
            labels_map[n] = f"{classes_ranges[n-1]}-{classes_ranges[n]}"
    df_parallel['age'] = df_parallel['age'].replace(labels_map)

    # Male with Heart Disease filtering and sorting
    df_age_hd = df_parallel[df_parallel['target'] == 1]
    df_male_age_hd = df_age_hd[df_age_hd['gender'] == 1]
    df_sorted_male_age = df_male_age_hd.sort_values(by=['age'], axis=0)
    
    # Set plot colors
    plot_coloring(plt)
    sns.histplot(df_sorted_male_age['age'], color=[ACCENT_COLOR2], edgecolor=COLOR)
    plt.title('Age distribution of males with HD')
    st.pyplot(plt)  # Render the plot in Streamlit
    plt.show()


def main():
    st.title('Numerical Data Visualization')
    page2_sale_price_study_body()  # Call the function that contains the study body and visualization logic

if __name__ == "__main__":
    main()
    
# The code above was copied from the Churnometer Project from Code Institute 
# and was made to fit this project