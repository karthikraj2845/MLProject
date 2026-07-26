# 🎓 Student Performance Prediction

A Machine Learning web application that predicts a student's **Math Score** based on demographic and academic factors. The project includes a complete end-to-end ML pipeline, a Flask web application, and automated deployment to **AWS Elastic Beanstalk** using **GitHub Actions**.
> This repository contains my own implementation, development, and deployment of the project with AWS CI/CD integration.

---

## 🚀 Live Demo

**Application URL:**

```
http://studentperformance-env.eba-v2isv3bg.ap-south-2.elasticbeanstalk.com/predictdata
```

---

## 📌 Features

- Predicts a student's Math Score
- User-friendly Flask web interface
- Complete ML pipeline
- Data preprocessing
- Model training and evaluation
- Model serialization using Pickle
- Automatic deployment using GitHub Actions
- Hosted on AWS Elastic Beanstalk

---

# 🛠 Tech Stack

### Programming Language

- Python 3.12

### Machine Learning

- Scikit-learn
- CatBoost
- XGBoost
- Pandas
- NumPy

### Backend

- Flask
- Gunicorn

### Deployment

- AWS Elastic Beanstalk
- GitHub Actions
- GitHub Secrets
- IAM

---

# 📂 Project Structure

```
MLProject
│
├── artifacts/
│   ├── model.pkl
│   └── preprocessor.pkl
│
├── notebooks/
│
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   │
│   ├── pipeline/
│   │   ├── predict_pipeline.py
│   │   └── train_pipeline.py
│   │
│   ├── exception.py
│   ├── logger.py
│   └── utils.py
│
├── templates/
│   ├── home.html
│   └── index.html
│
├── application.py
├── app.py
├── environment.yml
├── requirements.txt
├── setup.py
└── README.md
```

---

# ⚙️ Machine Learning Pipeline

The project follows a complete machine learning workflow:

1. Data Ingestion
2. Data Validation
3. Data Transformation
4. Feature Engineering
5. Model Training
6. Hyperparameter Tuning
7. Model Evaluation
8. Model Saving
9. Prediction Pipeline

---

# 📊 Input Features

The model takes the following inputs:

- Gender
- Race/Ethnicity
- Parental Level of Education
- Lunch Type
- Test Preparation Course
- Reading Score
- Writing Score

### Output

- Predicted Math Score

---

# 🧠 Models Evaluated

The following regression algorithms were evaluated:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor
- AdaBoost Regressor
- XGBoost Regressor
- CatBoost Regressor

The best-performing model is automatically selected and saved.

---

# 💻 Installation

Clone the repository

```bash
git clone https://github.com/karthikraj2845/MLProject.git
```

Move into the project

```bash
cd MLProject
```

Create a virtual environment

```bash
conda create -n mlproject python=3.12
conda activate mlproject
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python application.py
```

Open your browser

```
http://localhost:5000
```

---

# ☁️ Deployment

This project is deployed on **AWS Elastic Beanstalk**.

Deployment is fully automated using **GitHub Actions**.

Whenever code is pushed to the `main` branch:

- GitHub Actions creates a deployment package
- Uploads it to AWS
- Creates a new Elastic Beanstalk application version
- Deploys the latest version automatically

---

# 🔄 CI/CD Workflow

```
Developer
      │
      ▼
GitHub Repository
      │
      ▼
GitHub Actions
      │
      ▼
AWS Elastic Beanstalk
      │
      ▼
Live Flask Application
```

---

# 📷 Application Screenshots

You can add screenshots here.

Example:

```
screenshots/
│
├── home.png
├── prediction.png
└── result.png
```

---

# 📦 Requirements

- Python 3.12
- Flask
- Gunicorn
- Pandas
- NumPy
- Scikit-learn
- CatBoost
- XGBoost

---



# ⭐ Acknowledgement
The implementation, deployment workflow, AWS configuration, and GitHub Actions integration in this repository were developed as part of my learning and hands-on practice.

---

