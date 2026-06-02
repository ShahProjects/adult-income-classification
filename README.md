# adult-income-classification
# Adult Income Classification Project

## 📌 Project Overview
This project is a Machine Learning classification system that predicts whether an individual's income is `<=50K` or `>50K` based on demographic and work-related features.

The system includes:
- Multiple ML models comparison
- Best model selection
- REST API using FastAPI
- Web UI using Streamlit
- End-to-end deployment ready structure

## LIVE FRONTEND LINK ✔ 
External URL: http://54.145.250.53:8501


---

## 🧠 Machine Learning Models Used

The following classification models were trained and evaluated:

- Logistic Regression
- Decision Tree Classifier
- Support Vector Classifier (SVC)
- K-Nearest Neighbors (KNN)

---

## ⚙️ ML Pipeline

The project uses a complete preprocessing pipeline:

- Missing value handling (SimpleImputer)
- Categorical encoding (OneHotEncoder)
- Feature scaling (StandardScaler)
- Column transformation (ColumnTransformer)
- Pipeline integration for all models

---

## 📊 Model Accuracy Comparison

| Model                 | Accuracy |
|----------------------|----------|
| Logistic Regression  | 85%      |
| Decision Tree        | 82%      |
| SVC                  | 86%      |
| KNN                  | 83%      |

---

## 🏆 Best Model

**Logistic Regression** was selected as the best performing model and saved as:

model.pkl


---

## 🚀 Project Features

- End-to-end ML pipeline
- Model training & evaluation
- Best model selection
- REST API using FastAPI
- Interactive frontend using Streamlit
- Real-time prediction system

---

## 🖥️ FastAPI Endpoint

### Endpoint:

POST /predict


### Example Request:
```json
{
  "age": 35,
  "workclass": "Private",
  "fnlwgt": 200000,
  "education": "Bachelors",
  "educational_num": 13,
  "marital_status": "Married-civ-spouse",
  "occupation": "Tech-support",
  "relationship": "Husband",
  "race": "White",
  "gender": "Male",
  "capital_gain": 0,
  "capital_loss": 0,
  "hours_per_week": 40,
  "native_country": "United-States"
}
Response:
{
  "prediction": "<=50K"
}
