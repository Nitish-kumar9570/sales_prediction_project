# Sales Prediction & Marketing Analytics Dashboard

A professional Machine Learning and Streamlit-based dashboard that predicts future sales using advertising spend and provides business marketing insights through interactive visualizations and analytics.

---

# Project Overview

This project analyzes how different advertising channels affect product sales and helps businesses make data-driven marketing decisions.

The dashboard predicts future sales based on:

- TV Advertising Budget
- Radio Advertising Budget
- Newspaper Advertising Budget
- Target Audience Segment
- Advertising Platform

The application also provides:

- Sales forecasting
- Advertising impact analysis
- Correlation analysis
- Feature importance percentage
- Interactive visualizations
- Business strategy recommendations

---

# Objectives

- Predict future sales using Machine Learning
- Analyze advertising effectiveness
- Understand marketing platform impact
- Visualize sales trends
- Deliver actionable business insights

---

# Machine Learning Model

The project uses Linear Regression.

Regression Formula:

```math
Sales = w₁(TV) + w₂(Radio) + w₃(Newspaper) + w₄(Segment) + w₅(Platform) + b
```

The model learns how advertising investments influence future sales outcomes.

---

# Dataset

Dataset Used:
- `Advertising.csv`

Main Columns:

| Column | Description |
|---|---|
| TV | TV advertising budget |
| Radio | Radio advertising budget |
| Newspaper | Newspaper advertising budget |
| Sales | Product sales |

Additional engineered features:
- Target Segment
- Advertising Platform

---

# Features

## Data Cleaning
- Missing value handling
- Duplicate removal

## Feature Engineering
- Segment encoding
- Platform encoding

## Sales Forecasting
Predict future sales based on advertising budget.

## Correlation Analysis
Understand relationships between advertising channels and sales.

## Advertising Impact Analysis
Analyze which platform contributes most to sales.

## Interactive Dashboard
Professional Streamlit UI with interactive charts and insights.

## Business Recommendations
Provides marketing strategy suggestions based on prediction results.

---

# Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core Programming |
| Pandas | Data Analysis |
| NumPy | Numerical Operations |
| Scikit-learn | Machine Learning |
| Streamlit | Web Dashboard |
| Matplotlib | Data Visualization |
| Seaborn | Statistical Visualization |
| Plotly | Interactive Charts |
| Statsmodels | Regression Trendlines |

---

# Project Structure

```bash
sales_prediction_project/
│
├── app.py
├── Advertising.csv
└── Sales_Prediction.ipynb
├── requirements.txt
└── README.md

```

---

# Installation Guide

## 1. Clone Repository

```bash
git clone https://github.com/Nitish-kumar9570/sales_prediction_project.git
```

---

## 2. Open Project Folder

```bash
cd sales_prediction_project
```

---

## 3. Create Virtual Environment (Optional)

### Linux / macOS

```bash
python -m venv .venv
source .venv/bin/activate
```

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# requirements.txt

```txt
streamlit
pandas
numpy
matplotlib
seaborn
plotly
scikit-learn
statsmodels
```

---

# Run The Application

```bash
streamlit run app.py
```

After running the command, Streamlit will automatically open the dashboard in your browser.

---

# Dashboard Modules

## Sales Prediction
Predicts future sales using advertising budgets.

## Correlation Heatmap
Shows relationships between marketing variables.

## Feature Impact Analysis
Displays percentage dependency of sales on different features.

## Advertising vs Sales Graphs
Interactive analysis for:
- TV
- Radio
- Newspaper

## Strategy Overview
Provides marketing recommendations based on:
- Advertising platform
- Target segment
- Budget performance

---

# Model Evaluation

Evaluation Metrics Used:

| Metric | Purpose |
|---|---|
| R² Score | Measures prediction accuracy |
| MAE | Measures prediction error |

---

# Business Insights

This dashboard helps businesses:

- Identify the best advertising channel
- Optimize marketing budget allocation
- Forecast future sales growth
- Improve campaign strategies
- Analyze audience targeting effectiveness

---

# Sample Workflow

```text
Load Dataset
      ↓
Data Cleaning
      ↓
Feature Engineering
      ↓
Train Regression Model
      ↓
Predict Future Sales
      ↓
Visualize Results
      ↓
Generate Business Insights
      ↓
Deploy with Streamlit
```

---

# Future Improvements

Possible future upgrades:

- Random Forest Regression
- XGBoost
- Time Series Forecasting
- AI Recommendation Engine
- User Authentication
- Database Integration
- CSV Upload Feature
- Real-time Analytics

---

# Dashboard Features

- Modern Dark UI
- Interactive Charts
- Real-time Prediction
- Responsive Layout
- Marketing Insights
- Feature Importance Analysis

---

# Author / Developed by

Nitish Kumar

Developed using:
- Python
- Machine Learning
- Streamlit

---

# License

This project is developed for educational and portfolio purposes.
