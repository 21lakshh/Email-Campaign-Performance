# 📧 Email Campaign Performance Optimization

Optimizing marketing campaigns is one of the most common and impactful tasks in data science. This project focuses on improving the performance of email-based campaigns using feature engineering, exploratory data analysis, and various machine learning models.

Emails are highly effective as they are *free*, **scalable**, and **personalizable**. The goal is to optimize emails based on **content**, **personalization**, **timing**, and **user behavior** to boost engagement rates.

---

## 📊 Project Summary

- **Total Emails Sent**: 100,000  
- **Emails Opened**: 10,345  
- **Emails Clicked**: 2,119  
- **Open Rate**: 10.35%  
- **Click Rate**: 2.12%  
- **Click-Through Rate (CTR)**: 20.48% (clicks per open)

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

## 🏆 Best Performing Model

- **Model**: `SVC (Support Vector Classifier)`  
- **Score**: **97.73**

---

## 📈 Performance Evaluation

- **Predicted Average CTR**: Slightly lower than historical CTR  
- **Potential CTR Improvement**: **-0.39%**

### 🔍 What It Tells You

- **Baseline CTR**: How often people click on average (real-world benchmark)  
- **Model Predicted CTR**: What your model thinks the CTR will be (on average)  
- **Improvement (%)**: How much better (or worse) the model is compared to just guessing the baseline CTR for everyone  

Despite high validation accuracy, the negative improvement suggests overfitting or a need for better calibration. This highlights the importance of **contextual performance metrics** (like CTR lift) over raw accuracy.

---
