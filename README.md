* [Dataset Content](#dataset-content) 🗃️

* [Business Requirements](#business-requirements) 📋

* [Hypothesis and How To Validate](#hypothesis-and-how-to-validate) 💡

* [Rationale](#rationale) ✍

* [ML Business Case](#ml-business-case) 📊

* [Dashboard Design](#dashboard-design) 📐

* [Unfixed Bugs](#unfixed-bugs) 🛠️

* [Deployment](#deployment) 🖥️

* [Data Analysis and ML Libraries](#data-analysis-and-ml-libraries) 📚

* [Credits and Acknowledgments](#credits-and-acknowledgments) 💐

## Dataset Content

This heart disease dataset is acquired from one of the multispecialty hospitals in India and is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/telecom-churn-dataset). This dataset consists of 1000 rows with 14 columns and represents patient characteristics (age, gender), their vital measurements (resting blood preasure, maximum heart rate) and heart desease classification. We are going to use the latter as a target variable throughout the project.

<details>
<summary>The dataset's variable names, meanings and units can be inspected below: </summary> 

| Variable | Explain | Type of Data | Units |
| :---- | :---- | :---- | :---- |
| patientid | Patient identification number | Numeric | Number |
| age | Age | Numeric | In Years |
| gender | Gender | Binary | 0 (female) / 1 (male) |
| restingBP | Resting blood pressure | Numeric Z| 94-200 (in mm HG) |
| serumcholestrol | Serum cholesterol | Numeric | 126-564 (in mg/dl) |
| fastingbloodsugar | Fasting blood sugar | Binary | 0 (false) / 1 (true) > 120 mg/dl |
| chestpain | Chest pain type | Nominal | 0 (typical angina), 1 (atypical angina), 2 (non-anginal pain), 3 (asymptomatic) |
| restingelectro | Resting electrocardiogram results | Nominal | 0 (normal), 1 (ST-T wave abnormality), 2 (probable or definite left ventricular hypertrophy) |
| maxheartrate | Maximum heart rate achieved | Numeric | 71-202 |
| exerciseangina | Exercise induced angina | Binary | 0 (no) / 1 (yes) |
| oldpeak | Oldpeak = ST | Numeric | 0-6.2 |
| slope | Slope of the peak exercise ST segment | Nominal | 1 (upsloping), 2 (flat), 3 (downsloping) |
| noofmajorvessels | Number of major vessels | Numeric | 	0, 1, 2, 3 |
| target | Heart disease status | Binary | 0: Absent, 1: Present |

</details>

## Business Requirements

Our fictitious client 'Silent Hearts' is a Healthcare provider based in India. They are requesting help to analize the data and provide data-driven solution in predicting Heart Disease to maximise the benefit of early discovery and increase the chance of recovery amongst patients.

1 - The client is interested in discovering how Heart Disease is affected by listed variables. Therefore, the client expects data visualisations of the correlated variables against the target to show that.

2 - The client is interested in predicting whether or not a patient has Heart Disease.

## Hypothesis and how to validate?

1. High resting blood sugar level increases total cholesterol level in the blood.
* Correlation Study

2. Higher cholesterol level increases chance of Heart Disease.
* Correlation Study

3. Men aged 50-55 are most prone to Heart Disease.
* Correlation Study

## The rationale to map the business requirements to the Data Visualizations and ML tasks

**Business Requirement 1:** Data Visualisation and Correlation Study
* We will inspect the data related to the patient base.
* We will conduct a correlation study (Pearson and Spearman) to understand better how the variables are correlated to Heart Disease.
* We will plot the main variables against Heart Disease Status to visualize insights.

**Business Requirement 2:** Classification and Data Analysis
* We want to predict if a patient has heart disease or not. We want to build a binary classifier.

## ML Business Case

1. What are the business requirements?
* The client is interested in discovering how clinical measurements and patient characteristics correlate with Heart Disease presence. Therefore, the client expects data visualizations of the correlated variables against the Heart Disease status.
* The client is interested in predicting whether on not a patiente has Heart Disease.

2. Is there any business requirement that can be answered with conventional data analysis?
Yes, we can use conventional data analysis to investigate how clinical measurements and patient characteristics correlate with Heart Disease presence.

3. Does the client need a dashboard or an API endpoint?
The client needs a dashboard.

4. What does the client consider as a successful project outcome?
* A study showing the most relevant variables correlated to Heart Disease Status.
* Also, a capability to predict heart disease in patients from given data.

5. Can you break down the project into Epics and User Stories?

* Information gathering and data collection.
* Data visualization, cleaning, and preparation.
* Model training, optimization and validation.
* Dashboard planning, designing, and development.
* Dashboard deployment and release.

6. Are there Ethical or Privacy concerns?
No. The client found a public dataset.

7. Does the data suggest a particular model?
The data suggests a classification where the target is the Heart Disease status.

8. What are the model's inputs and intended outputs?
The inputs are clinical measurements and patient characteristics and the output is binary classification of absence/presence of Heard Disease.

9. What are the criteria for the performance goal of the predictions?
We agreed with the client an accuracy score of 98% and recall of atleast 97% on the train set as well as on the test set.

10. How will the client benefit?
By predicting Heart Disease to maximise the benefit of early discovery and increase the chance of recovery amongst patients.

## Dashboard Design
* List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other item that your dashboard library supports.
* Later, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project you were confident you would use a given plot to display an insight but subsequently you used another plot type).


## Unfixed Bugs
* You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

## Deployment
### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.


## Data Analysis and ML Libraries
* Here you should list the libraries you used in the project and provide an example(s) of how you used these libraries.


## Credits and Acknowledgments 

* In this section, you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism. 
* You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign-Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The photos used on the home and sign-up page are from This Open-Source site
- The images used for the gallery page were taken from this other open-source site



### Acknowledgements
* Thank the people that provided support through this project.

