# Heart Disease Prediction Using Machine Learning

**Project Overview**

Heart disease is a leading cause of morbidity and mortality worldwide. Understanding the risk factors and being able to predict potential cases through data can improve early interventions. Using machine learning, this project seeks to identify patterns in lifestyle, demographic, and health-related factors that contribute to heart disease and provide a personal Risk Indicator Application.

**Data Source**

This project focuses on predicting heart disease risk using machine learning techniques applied to the Behavioral Risk Factor Surveillance System (BRFSS) 2015 survey data. BRFSS is a health-related telephone survey that is collected annually by the CDC. Each year, the survey collects responses from over 400,000 Americans on health-related risk behaviors, chronic health conditions, and the use of preventative services.

**Data Set**

The dataset is a subset of features from the BRFSS survey 2015, obtained from Kaggle. It has been pre-processed and cleaned to focus on risk factors relevant to heart disease, diabetes, and other chronic conditions. The feature selection can be confirmed by various studies, e.g. „Risk Factors for Coronary Artery Disease“ by Jonathan C. Brown et al or „Number of Coronary Heart Disease Risk Factors and Mortality in Patients With First Myocardial Infarction“ by John G Canto, Catarina I Kiefe, William J Rogers et al. John Hopkins Medicien Center…, which all largely refer to  major risk factors such as drinking, smoking, diabetes, obesity, dyslipidemia and hypertension.

**Data Structure**

•	Total Records: 253,680 survey responses

•	Features: 21 features representing individual characteristics and behaviors

•	Target Variable: Binary indicator of heart disease status (1 for respondents who reported having coronary heart disease (CHD) or myocardial infarction (MI), 0 otherwise). 

**Feature Selection**

•	Ordinal Features (Label Encoded): Age, BMI, General Health, Mental Health, Physical Health, Household Income

•	Binary Features (One-Hot Encoded): Blood Pressure, Smoking, High Cholesterol, Cholesterol Check, Gender, Physical Activity, Fruit Consumption, Vegetable Consumption, Alcohol Consumption, Health Care Access, Stroke, Health Costs, Walk Difficulty.

**Data Imbalance**

The dataset is highly imbalanced, with a significantly smaller proportion of respondents reporting heart disease. 

**Preprocessing Steps**

•	Feature Encoding: 

- Ordinal variables are label-encoded to maintain inherent order.

- Binary variables are one-hot encoded to ensure they are represented as distinct categories.

•	Data Resampling:

- Given the high imbalance in the target variable, Random UnderSampling has proven to significantly improve recall performance metrics, by reducing the number of majority class samples.

**Model Selection and Hyperparameter Tuning**

Due to the large dataset and to identifying complex interactions in the features the Radnom Forest Model has been utilized.
Moreover, hyperparameter such as n_estimator, max_depth, min_split, min_samples and max_features have been tuned via random search.

**Model Evaluation Metrics**

The model was primarily evaluated on:

•	Recall: Measures the model’s ability to correctly identify all positive cases (sensitivity).

•	Confusion Matrix: A visual assessment of true positives, false positives, true negatives, and false negatives.

**Feature Contribution Function**

Random Forests improve perfomance metrics by aggregating multiple decision tress but lose interpretability compared to a signle tree. Feature importance mitigates this problem. It is aimed at calculating the contribution of each feature to the final model's decision for a specific instance. Feature importances are computed as the mean and standard deviation of accumulation of the impurity decrease within each tree. More on scikit-learn. 

**Risk Indicator Application**

The Streamlit app allows users to input various health-related variables to estimate a health-related outcome based on the model's predictions. 
Key Features:

1.	User Input for Health Variables: The app presents a form where users can enter health data that follow the features the a machine learning model was trained on.

3.	Predictive Model Integration: The app then compiles the input data into a dictionary (example_input) and passes it to a predefined predict function. The predict function uses the input data to generate an outcome estimate, which is then displayed to the user.

4.	Output: Once the user submits their information, the app calls the predict function, which uses a machine learning model to generate a prediction.

**Key Findings Summary**

1.	Data Imbalance Impact: Due to the high imbalance in heart disease cases, the model without resampling performed poorly in recall, failing to identify a large portion of positive cases. The high imbalance led to an initial high accuracy rate, which, however, is unsuitable for categorical (label) problems.

2.	Effectiveness of Resampling: Undersampling improved model performance by forcing the classifier to pay more attention to minority cases, though it led to some data loss. This has succesfully been addressed with resampling the data, increasing the recall rate for True Positives from 0.1 up to over 0.8.

3.	Random Forest Model: The Random Forest Model appeared to be suitable fort he data set.

4.	Hyperparameter Tuning: Tuning hyperparameters improved recall effectiveness by 3 basis points and thus made a fair performance increase contribution, though not as much as resampling.

5.	Risk Contribution Function: Appeared to provide a good overview of the impact of certain features regarding given samples, improving the understanding of indivual risk patterns.

6.	Risk Indicator Application: This app could be used in a healthcare setting to provide individuals with first insights into health risks based on their self-reported lifestyle and health data. It allows for quick screening without requiring detailed medical records.

**Result evaluation and conclusion**

The recall score for having no heart disease is at 0.72 and for having heart disease at 0.82. The precision for having no heart disease is at 0.97 and for having heart disease at 0.23. The model may be biased toward predicting heart diseases more often, leading to high recall (capturing most actual class heart disease cases) but low precision (many of those predictions are incorrect). This is common when the decision threshold is low, causing the model to classify more samples as having heart disease to ensure it catches most true positives.

As a result, the model is more sensitive to risk factors for heart diseases as they become more significant (e.g. very high blood pressure or high cholesterin) and/or accumulate with more risk factors (e.g. low general and mental health). This outcome is assumed to be suitable, given the aim of the application to sensitize the user to the risks of having a heart disease.
Future work could explore more fine tuning techniques, such as dropping atomic links as well asconsulting domain experts for better insight into feature relevance and data interpretation. In this regard, result interpretation and reccomendations could be further automated via a chat-bot based on LLMs.

**Local Deployment**

•	Download files into one folder

•	Install and import libraries as listed in requirements.txt file

•	Run app.py file from project folder via terminal command: "streamlit run app.py"

**References**

•	Behavioral Risk Factor Surveillance System (BRFSS)

•	Heart Disease Health Indicators Dataset on Kaggle

•	Feature Contribution Function on scikit-learn


