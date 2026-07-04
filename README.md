\# Student Stress Prediction using Machine Learning



\## Project Overview

## 🚀 Live Demo

Try the deployed application here:

https://student-stress-prediction-cm.streamlit.app



This project predicts whether a student is likely to experience \*\*High Stress\*\* or \*\*Low Stress\*\* using supervised machine learning techniques based on academic, behavioural, and lifestyle-related factors.



The project demonstrates a complete end-to-end machine learning workflow, including data preprocessing, exploratory data analysis, feature engineering, model building, model evaluation, and comparison of multiple classification algorithms.



\---



\## Objective



The objective of this project is to build and compare machine learning classification models capable of predicting student stress levels and identifying the most suitable model for the given dataset.



\---



\## Dataset



This project uses the \*\*Student Stress Dataset\*\* obtained from \*\*Kaggle\*\*.



The dataset contains approximately \*\*25,500 student records\*\* with information related to academic performance, lifestyle habits, and behavioural characteristics.



\### Features



\- Sleep Hours

\- Study Hours

\- Social Media Hours

\- Attendance

\- Exam Pressure

\- Family Support

\- Month

\- Student Type (School / College / Working Student)



\### Target Variable



\*\*Stress\_Level\*\*



\- 0 → Low Stress

\- 1 → High Stress



\---



\## Data Preprocessing



The following preprocessing steps were performed:



\- Handling missing values

\- Identifying and replacing invalid negative values

\- Removing duplicate records

\- One-Hot Encoding of categorical variables

\- Correlation analysis

\- Train-Test Split (80:20)

\- Feature Scaling using StandardScaler (where applicable)



\---



\## Machine Learning Models



The following classification algorithms were trained and evaluated:



\- Logistic Regression

\- Decision Tree Classifier

\- Random Forest Classifier

\- K-Nearest Neighbors (KNN)



\---



\## Model Performance



| Model | Accuracy |

|--------|---------:|

| Random Forest | \*\*80.8%\*\* |

| Logistic Regression | \*\*80.6%\*\* |

| K-Nearest Neighbors | \*\*77.8%\*\* |

| Decision Tree | \*\*74.0%\*\* |



\---



\## Best Performing Model



Random Forest achieved the highest accuracy (\*\*80.8%\*\*).



However, Logistic Regression produced nearly identical performance while offering greater interpretability, making it a strong baseline classification model.



\---



\## Technologies Used



\- Python

\- Pandas

\- NumPy

\- Matplotlib

\- Seaborn

\- Scikit-learn

\- Jupyter Notebook

\- Streamlit




\---



\## Repository Structure



```

Student-Stress-Prediction/

│

├── Student\_Stress\_Prediction.ipynb

├── student\_stress.csv

├── README.md

└── requirements.txt

```



\---



\## How to Run the Project



1\. Clone the repository



```bash

git clone <repository-url>

```



2\. Install the required libraries



```bash

pip install -r requirements.txt

```



3\. Open the notebook



```bash

jupyter notebook Student\_Stress\_Prediction.ipynb

```



\---



\## Future Improvements



\- Hyperparameter tuning

\- Cross-validation

\- Streamlit deployment

\- Model persistence using Joblib

\- XGBoost implementation



\---



\## Author



\*\*Chiranjeet Mishra\*\*



This project is part of my Data Science portfolio and demonstrates an end-to-end machine learning workflow, from data preprocessing to model evaluation and comparison.

## Dataset Acknowledgement

The dataset used in this project was obtained from Kaggle. Credit for the dataset belongs to the original creator. This repository focuses on data analysis, preprocessing, model development, and evaluation.

