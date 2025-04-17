# 📧 Email Campaign Performance Optimization

Optimizing marketing campaigns is one of the most common and impactful tasks in data science. This project focuses on improving the performance of email-based campaigns using feature engineering, exploratory data analysis, and various machine learning models.

Emails are highly effective as they are *free*, **scalable**, and **personalizable**. The goal is to optimize emails based on **content**, **personalization**, **timing**, and **user behavior** to boost engagement rates.

---

##  Project Summary

- **Total Emails Sent**: 100,000  
- **Emails Opened**: 10,345  
- **Emails Clicked**: 2,119  
- **Open Rate**: 10.35%  
- **Click Rate**: 2.12%  
- **Click-Through Rate (CTR)**: 20.48% (clicks per open)

---

## 📊 Key Insights from Exploratory Data Analysis

Below are interesting behavioral patterns discovered across different segments:

### 🔠 Email Content & Personalization
- **Short Emails perform better**: 
  - **Open Rate**: 11.59% vs 9.12% (short vs long)
  - **Click Rate**: 2.39% vs 1.85%
- **Personalized Emails outperform Generic**:
  - **Open Rate**: 12.78% vs 7.93%
  - **Click Rate**: 2.73% vs 1.51%

### 🕰️ Time of Day Matters
- Best performance observed during **9 AM – 12 PM**, aligning with typical workday engagement:
  - **Peak Open Rate**: 15.94% at 12 AM and 13.24% at 10 AM
  - **Peak Click Rate**: 4.14% at 11 PM and 2.90% at 12 AM
- Lowest engagement occurs during **late evening hours (8 PM – 11 PM)**.

### 📅 Day of the Week Insights
- **Midweek days (Tue–Thu)** yield highest engagement:
  - **Top Click Rates**: Wednesday (2.76%), Tuesday (2.49%), Thursday (2.44%)
- **Fridays and weekends** have lower engagement:
  - Friday Click Rate: 1.40%

### 🌍 Country-wise Trends
- **UK and US users** show significantly higher engagement:
  - UK: 12.02% open, 2.47% click
  - US: 11.90% open, 2.44% click
- **European countries (ES, FR)** show much lower response:
  - FR: 4.06% open, 0.80% click

### 🛒 User Past Purchases
- Strong positive correlation between **purchase history and engagement**:
  - Users with 0 past purchases: **0.05% click rate**
  - Users with 10+ past purchases: **4.66%+ click rate**
- Super-engaged users (14–22 past purchases) show **click rates above 9%**, with some as high as **100%**.

These patterns indicate that **targeting short, personalized emails during working hours on Tuesday–Thursday**—especially to users with a strong purchase history—can significantly boost campaign performance.

---

## 🧱 Datasets Used

### `email_table`
| Column              | Description                                          |
|---------------------|------------------------------------------------------|
| email_id            | Unique identifier for each email sent               |
| email_text          | Type of text: short (2 paragraphs) or long (4 paragraphs) |
| email_version       | Either “personalized” (e.g., “Hi John”) or “generic” (e.g., “Hi,”) |
| hour                | Local hour when the email was sent                   |
| weekday             | Day of the week the email was sent                   |
| user_country        | Country based on user's IP                           |
| user_past_purchases | Number of past purchases by the user                |

### `email_opened_table`
| Column   | Description                        |
|----------|------------------------------------|
| email_id | Emails that were opened at least once |

### `link_clicked_table`
| Column   | Description                        |
|----------|------------------------------------|
| email_id | Emails where the internal link was clicked |

---

## 🧠 Feature Engineering

New features created to enhance model learning:

- `email_version_encoded`, `email_text_encoded` — Encoded categorical features  
- `is_weekend` — Whether the email was sent on Saturday/Sunday  
- `is_work_hour` — Sent between 9 AM and 5 PM  
- `email_sent_bin_encoded` — Time of day categorized as night, morning, afternoon, or evening  
- `version_text_combo` — Interaction between text and version  
- `user_engagement` — Past purchases × opened flag  
- `country_ctr` — Average CTR by user country  
- `purchase_bin_encoded` — User’s purchase history bucketed into none, low, med, high

---

## 🤖 Models Trained

| Model                     | Type                  |
|--------------------------|-----------------------|
| `LogisticRegression()`    | Linear                |
| `DecisionTreeClassifier()`| Tree-based            |
| `RandomForestClassifier()`| Ensemble              |
| `GradientBoostingClassifier()` | Boosting        |
| `KNeighborsClassifier()`  | Distance-based        |
| `XGBClassifier()`         | Gradient Boosting (XGBoost) |
| `SVC(probability=True)`   | Support Vector Machine|

---

## 🏆 Best Performing Models & Evolution

| Stage                       | Best Model           | CTR Improvement |
|----------------------------|----------------------|------------------|
| Before Feature Engineering | Logistic Regression  | **-1.68%**       |
| After Feature Engineering  | SVC                  | **-0.39%**       |
| After Grid Search Tuning   | Tuned SVC            | **+2.89%**       |

> 🔍 Note:  
> The grid search was done on a **small parameter space** due to high computation time. With **further hyperparameter tuning**, it's likely that even **greater CTR improvements** can be achieved.

---

## 📈 Performance Evaluation

- **Baseline CTR**: Real-world average (historical benchmark)
- **Model Predicted CTR**: Average predicted CTR across the dataset
- **CTR Improvement**: Comparison to the baseline

- Negative improvement indicates overfitting or lack of generalization
- Positive improvement suggests the model is **effectively learning patterns** that generalize to new data

Despite high validation accuracy from models like SVC, **real success is measured by CTR uplift**, not raw accuracy—highlighting the importance of **business-aligned evaluation metrics**.

---
