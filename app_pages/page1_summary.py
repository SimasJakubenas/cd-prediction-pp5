import streamlit as st

def page1_summary_body():
    st.write("### Project Summary")

    # text based on README file - "Dataset Content" section
    st.info(
        f"**Project Terms & Jargon**\n"
        f"* The dataset is sourced from **[Kaggle]"
        f"(https://www.kaggle.com/datasets/jocelyndumlao/cardiovascular-disease-dataset)**. "
        f"\n\n"
        f"* The dataset consists of 1000 rows each and represents patients "
        f"from multispecialty hospitals in India. \n\n"
        f"* The dataset consists of columns of variables relating to patients characteristics "
        f"(age, gender) and measurements of their vitals (i.e. resting blood preasure).#n#n "
        f"* Age of the patients in this dataset are between 20 and 80 years old.\n\n"
        f"* **target** is our target variable and it shows presence or absence "
        f"of Heart Disease in a patient.\n\n"
    )

    st.info(
        f"**Dataset Content Abbreviations**\n\n"
        f"| Variable | Explain | Type of Data | Units |\n"
        f"| :---- | :---- | :---- | :---- |\n"
        f"| patientid | Patient identification number | Numeric | Number |\n"
        f"| age | Age | Numeric | In Years |\n"
        f"| gender | Gender | Binary | 0 (female) / 1 (male) |\n"
        f"| restingBP | Resting blood pressure | Numeric Z| 94-200 (in mm HG) |\n"
        f"| serumcholestrol | Serum cholesterol | Numeric | 126-564 (in mg/dl) |\n"
        f"| fastingbloodsugar | Fasting blood sugar | Binary | 0 (false) / 1 (true) "
        f"> 120 mg/dl |\n"
        f"| chestpain | Chest pain type | Nominal | 0 (typical angina), 1 (atypical "
        f"angina), 2 (non-anginal pain), 3 (asymptomatic) |\n"
        f"| restingelectro | Resting electrocardiogram results | Nominal | 0 (normal), "
        f"1 (ST-T wave abnormality), 2 (probable or definite left ventricular hypertrophy) |\n"
        f"| maxheartrate | Maximum heart rate achieved | Numeric | 71-202 |\n"
        f"| exerciseangina | Exercise induced angina | Binary | 0 (no) / 1 (yes) |\n"
        f"| oldpeak | Oldpeak = ST | Numeric | 0-6.2 |\n"
        f"| slope | Slope of the peak exercise ST segment | Nominal | 1 (upsloping), 2 (flat), "
        f"3 (downsloping) |\n"
        f"| noofmajorvessels | Number of major vessels | Numeric | 	0, 1, 2, 3 |\n"
        f"| target | Heart disease status | Binary | 0: Absent, 1: Present |\n"
        )
    
    # Link to README file, so the users can have access to full project documentation
    st.write(
        f"\n\n For additional information, please visit and **read** the "
        f"**[Project's README file](https://github.com/SimasJakubenas/cd-prediction-pp5)**. \n\n")
    
     # copied from README file - "Business Requirements" section
    st.success(
        f"#### The project has 2 business requirements: \n\n"
        f"**1.** The client is interested in discovering how Heart Disease is affected by listed "
        f"variables. Therefore, the client expects data visualisations of the correlated "
        f"variables against the target to show that.\n\n"
        f"**2.** The client is interested in predicting the house sale price from her four "
        f"inherited houses and any other house in Ames, Iowa. "
        )

# The code above was copied from the Churnometer Project from Code Institute 
# and was made to fit this project