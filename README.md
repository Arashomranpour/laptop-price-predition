<div align="center">

# 💻 Laptop Price Predictor

**Estimate a laptop's price from its specifications - an end-to-end regression project with a Streamlit app.**

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikitlearn&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-337AB7)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)

</div>

---

## ✨ Overview

**Notebook (`app.ipynb`)**

- 📊 EDA and feature engineering on `laptop_data.csv` (brand, type, RAM, weight, GPU, OS, ...).
- 🏷️ Preprocessing with `ColumnTransformer` + `Pipeline`; the target price is log-transformed.
- 🤖 Models compared: **Linear/Ridge, KNN, Decision Tree, Random Forest, Extra Trees, AdaBoost, Gradient Boosting, XGBoost**, plus **Voting** and **Stacking** ensembles.
- 💾 Final pipeline saved as `pipe.pkl` / `pipe1.pkl` (and the cleaned data as `df.pkl`).

**App (`app.py`)** - "Laptop price prediction": choose the specifications in the form and get the predicted price.

## 🚀 Getting Started

```bash
git clone https://github.com/Arashomranpour/laptop-price-predition.git
cd laptop-price-predition
pip install pandas numpy scikit-learn xgboost seaborn matplotlib streamlit jupyter
streamlit run app.py
```

## 📁 Project Structure

```
.
├── app.ipynb          # EDA, feature engineering, model comparison
├── test.ipynb         # Hyper-parameter search experiments
├── app.py             # Streamlit app
├── laptop_data.csv    # Dataset
└── pipe.pkl  pipe1.pkl  df.pkl   # Saved pipelines and data
```

## 🛠️ Tech Stack

`scikit-learn` · `XGBoost` · `pandas` · `Seaborn` · `Streamlit`
