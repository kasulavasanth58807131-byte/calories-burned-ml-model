# 🔥 Calories Burned Predictor

A machine learning web app that predicts calories burned during exercise based on biometric and workout data. Built with **XGBoost** and deployed via **Streamlit**.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.35-red?logo=streamlit)
![XGBoost](https://img.shields.io/badge/XGBoost-2.0-orange)
![R²](https://img.shields.io/badge/R²%20Score-0.9995-brightgreen)

---

## 📌 Project Overview

| Item | Detail |
|------|--------|
| **Dataset** | 15,000 exercise records (merged from `exercise.csv` + `calories.csv`) |
| **Task** | Regression — predict calories burned |
| **Best Model** | XGBoost (R² = 0.9995, MAE ≈ 1.01 cal) |
| **Deployment** | Streamlit Cloud |

---

## 🗂️ Repository Structure

```
calories-burned-predictor/
│
├── app.py               ← Streamlit web application
├── model.pkl            ← Trained XGBoost model
├── df.pkl               ← Processed dataset (for EDA charts)
├── exercise.csv         ← Raw exercise data
├── calories.csv         ← Raw calorie labels
├── requirements.txt     ← Python dependencies
└── README.md            ← This file
```

---

## 🚀 Live Demo

👉 **[Open App on Streamlit Cloud](https://your-app-name.streamlit.app)** *(update after deploy)*

---

## 🛠️ Features

- 🎛️ **Interactive sliders** for Gender, Age, Height, Weight, Duration, Heart Rate, Body Temp
- 🔥 **Instant calorie prediction** using a trained XGBoost model
- 📊 **Dataset insights** — distributions, correlation heatmap, scatter plots
- 🥇 **Percentile context** — see how you compare to the dataset
- 🍕 **Food equivalents** — fun calorie comparison (apples, pizza, chocolate!)

---

## ⚙️ Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/calories-burned-predictor.git
cd calories-burned-predictor

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch the app
streamlit run app.py
```

---

## ☁️ Deploy on Streamlit Cloud

1. Push this repo to **GitHub** (all files including `model.pkl` and `df.pkl`)
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud) → **New App**
3. Connect your GitHub repo
4. Set **Main file** to `app.py`
5. Click **Deploy** — done! 🎉

---

## 📈 Model Performance

| Model | R² | MAE | RMSE |
|---|---|---|---|
| **XGBoost** ✅ | **0.9995** | **1.01** | **1.49** |
| Gradient Boosting | 0.9993 | 1.21 | 1.71 |
| Support Vector Regressor | 0.9996 | 0.55 | 1.24 |
| Random Forest | 0.9983 | 1.67 | 2.62 |
| Ridge Regression | 0.9845 | 5.81 | 7.91 |
| Linear Regression | 0.9845 | 5.83 | 7.90 |

---

## 🧰 Tech Stack

- **Python 3.10+**
- **Streamlit** — web app framework
- **XGBoost** — gradient boosted trees
- **Scikit-learn** — preprocessing & evaluation
- **Pandas / NumPy** — data manipulation
- **Matplotlib / Seaborn** — visualizations

---

## 👤 Author

**Vasanth** · Data Science Intern  
📧 [your-email@gmail.com] · 🔗 [LinkedIn] · 💼 [Portfolio]

---

## 📄 License

MIT License — feel free to use and modify.
