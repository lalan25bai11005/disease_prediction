# 🏥 Disease Prediction System

## 📌 Overview

The Disease Prediction System is a machine learning-based web application that predicts possible diseases based on user-input symptoms. It is designed to provide quick preliminary insights using simple inputs such as fever, cough, fatigue, and other symptoms.

The system uses a trained machine learning model to classify input data and predict one of the predefined diseases.

---

## 🎯 Problem Statement

In many situations, people experience symptoms but are unsure about the possible disease. Consulting a doctor immediately may not always be feasible. This project aims to provide a simple AI-based solution that predicts diseases based on symptoms entered by the user.

---

## 🎯 Objectives

* To build a machine learning model for disease prediction
* To provide a user-friendly interface for symptom input
* To demonstrate practical application of ML concepts
* To deliver quick and simple predictions

---

## 🚀 Features

* Predicts diseases based on symptoms
* Simple and easy-to-use web interface
* Fast prediction using trained model
* Uses real-world ML concepts (classification)
* Expandable dataset for improved accuracy

---

## 🛠️ Technologies Used

* **Programming Language:** Python
* **Framework:** Flask
* **Libraries:** pandas, scikit-learn, numpy
* **Frontend:** HTML

---

## 📁 Project Structure

```
disease_prediction/
│
├── app.py                # Flask backend
├── train.py              # Model training script
├── dataset.csv           # Dataset
├── model.pkl             # Trained model
├── requirements.txt      # Dependencies
├── README.md             # Documentation
│
├── templates/
│   └── index.html        # User interface
```

---

## ⚙️ Installation & Setup

### 1. Clone or download the project

```bash
git clone <https://github.com/lalan25bai11005/disease_prediction.git>
cd disease_prediction
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Train the model

```bash
python train.py
```

### 4. Run the application

```bash
python app.py
```

### 5. Open in browser

```
http://127.0.0.1:5000/
```

---

## 📊 How It Works

1. User enters symptoms through the web interface
2. Input data is sent to the Flask backend
3. The trained ML model processes the input
4. The model predicts the disease
5. Result is displayed on the webpage

---

## 🧪 Sample Input

* Fever: 1
* Cough: 1
* Headache: 1
* Fatigue: 1
* Body Pain: 1
* Age: 25

### ✅ Output:

**Flu**

---

## 📈 Machine Learning Model

* Algorithm Used: Random Forest Classifier
* Type: Supervised Learning (Classification)
* Input Features: Symptoms + Age
* Output: Predicted Disease

---

## ⚠️ Limitations

* Small dataset may reduce accuracy
* Works only for predefined diseases
* Not a replacement for medical diagnosis

---

## 🔮 Future Enhancements

* Add more diseases and symptoms
* Improve dataset size and accuracy
* Add graphical UI and styling
* Deploy on cloud for public access

---

## 📚 References

* Scikit-learn Documentation
* Flask Documentation
* Machine Learning concepts 

---

## 👨‍💻 Author
Lalan Kumar Gupta

---
