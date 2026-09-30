# Loan Approval Prediction

## 📌 Project Overview

This project uses **Machine Learning classification algorithms** to predict whether a loan application will be approved or not based on applicant and loan-related information.

The project covers the complete machine learning workflow, including:

* Data loading and exploration
* Data preprocessing
* Categorical feature encoding
* Train-test splitting
* Feature scaling
* Classification model training
* Model evaluation
* Confusion matrix visualization
* Model comparison
* Model explainability using SHAP

---

## 🎯 Objective

The main objective of this project is to build a machine learning model that can predict the **loan approval status** of an applicant using features such as income, credit score, loan amount, employment experience, loan intent, and previous loan history.

**Target variable:** `loan_status`

* `1` → Loan Approved
* `0` → Loan Not Approved

---

## 📊 Dataset

The dataset contains **45,000 records** and **14 columns**.

### Features

| Feature               | Description                           |
| --------------------- | ------------------------------------- |
| `gender`              | Gender of the applicant               |
| `age`                 | Age of the applicant                  |
| `person_income`       | Annual income of the applicant        |
| `education`           | Education level                       |
| `home_onwership`      | Home ownership status                 |
| `employee_experience` | Employment experience                 |
| `loan_intent`         | Purpose of the loan                   |
| `loan_amount`         | Requested loan amount                 |
| `loan_interest_rate`  | Loan interest rate                    |
| `loan_percent_income` | Loan amount as a percentage of income |
| `previous_loan`       | Previous loan information             |
| `credit_history`      | Credit history information            |
| `credit_score`        | Applicant's credit score              |
| `loan_status`         | Target variable                       |

---

## 🔧 Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* SHAP

---

## 🧠 Machine Learning Workflow

### 1. Data Exploration

The dataset was explored using:

* `head()`
* `tail()`
* `shape`
* `info()`
* `describe()`
* Missing-value analysis
* Duplicate-value analysis
* Class distribution analysis

### 2. Exploratory Data Analysis

Visualizations were created to understand the dataset, including:

* Target variable distribution
* Numerical feature histograms
* Categorical feature distributions
* Boxplots
* Correlation heatmap

### 3. Data Preprocessing

Categorical features were converted into numerical form using **One-Hot Encoding**.

`ColumnTransformer` was used to apply encoding to categorical columns while keeping numerical columns unchanged.

### 4. Train-Test Split

The dataset was divided into:

* **80% training data**
* **20% testing data**

`stratify=y` was used to maintain the class distribution between training and testing data.

### 5. Feature Scaling

`StandardScaler` was used for models such as Logistic Regression and SVM where feature scaling is beneficial.

### 6. Machine Learning Models

The project evaluates classification models such as:

* Logistic Regression
* Decision Tree
* Random Forest

### 7. Model Evaluation

Models are evaluated using:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix

### 8. Model Explainability

**SHAP (SHapley Additive exPlanations)** is used to understand how individual features contribute to model predictions.

This helps answer questions such as:

* Which features influence loan approval?
* Does a higher credit score contribute to approval?
* How does loan amount affect predictions?
* Which features have the greatest overall impact?

---

## 📈 Results

The trained models are evaluated using classification metrics and confusion matrices.

The final model performance can be added here after completing model comparison.

Example:

| Model               | Accuracy | Precision | Recall | F1-Score |
| ------------------- | -------: | --------: | -----: | -------: |
| Logistic Regression |        — |         — |      — |        — |
| Decision Tree       |        — |         — |      — |        — |
| Random Forest       |        — |         — |      — |        — |

---

## 📁 Project Structure

```text
Loan-Approval-Prediction/
│
├── Loan_Approval_Prediction.ipynb
├── loan_data_new.csv
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ▶️ How to Run the Project

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
```

### 2. Open the project folder

```bash
cd Loan-Approval-Prediction
```

### 3. Install the required libraries

```bash
pip install -r requirements.txt
```

### 4. Start Jupyter Notebook

```bash
jupyter notebook
```

### 5. Open

```text
Loan_Approval_Prediction.ipynb
```

Run the notebook cells sequentially.

---

## 💡 Key Learning Outcomes

Through this project, I practiced:

* Data preprocessing
* Exploratory Data Analysis
* One-Hot Encoding
* ColumnTransformer
* Train-test splitting
* Feature scaling
* Classification algorithms
* Model evaluation
* Confusion matrices
* Feature importance
* SHAP-based model explainability

---

## 🚀 Future Improvements

* Hyperparameter tuning using `GridSearchCV`
* Cross-validation
* Random Forest optimization
* Additional classification models
* SHAP-based individual prediction explanations
* Building a web interface for loan prediction
* Deploying the trained model as a web application

---

## 👩‍💻 Author

**Deepika Kajale**

Computer Engineering Student


