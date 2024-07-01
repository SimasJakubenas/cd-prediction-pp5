import streamlit as st

def page4_hypothesis_and_validation_body():

    st.write("### Project Hypothesis and Validation")
	
    st.success(
    f"**1.** High resting blood sugar level increases total cholesterol "
    f"level in the blood: **False**. \n "
    f"- The correlation study on **Heart Disease Study** showed "
    f"no correlation between the two variables. \n\n"

    f"**2.** Higher cholesterol level increases chance of Heart Disease "
    f": **False**.\n "
    f"- We can't claim that imperatively as correlation study showed weak "
    f"correlation. \n\n"

    f"**3.** Men aged 50-55 are most prone to Heart Disease: **False**.\n"
    f"- Correlation study showed that age had no correlation with presence of"
    f"Heart Disease. Regardless, plotted Heart Disease presence in males from"
    f"different age groups. Men aged 50-55 showed to be not the most "
    f"Heart Disease prone demografic based on this data. \n\n"
    )

# The code above was copied from the Churnometer Project from Code Institute 
# and was made to fit this project