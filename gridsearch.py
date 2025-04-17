import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
email_table = pd.read_csv("email_table.csv")
opened_emails = pd.read_csv("email_opened_table.csv")
link_clicked = pd.read_csv("link_clicked_table.csv")

email_table['opened'] = email_table['email_id'].isin(opened_emails['email_id']).astype(int)
email_table['clicked'] = email_table['email_id'].isin(link_clicked['email_id']).astype(int)

le = LabelEncoder()
email_table['email_version_encoded'] = le.fit_transform(email_table['email_version'])
email_table['email_text_encoded'] = le.fit_transform(email_table['email_text'])
email_table['weekday_encoded'] = le.fit_transform(email_table['weekday'])
email_table['user_country_encoded'] = le.fit_transform(email_table['user_country'])

email_table['is_weekend'] = email_table['weekday_encoded'].isin([5, 6]).astype(int)
email_table['is_work_hour'] = email_table['hour'].between(9, 17).astype(int)
email_table['email_sent_bin'] = pd.cut(email_table['hour'], bins=[0, 6, 12, 18, 24], labels=['night', 'morning', 'afternoon', 'evening'])
email_table['email_sent_bin_encoded'] = email_table['email_sent_bin'].astype('category').cat.codes
email_table['version_text_combo'] = email_table['email_version_encoded'] * email_table['email_text_encoded']
email_table['user_engagement'] = email_table['user_past_purchases'] * email_table['opened']
country_ctr = email_table.groupby('user_country_encoded')['clicked'].mean()
email_table['country_ctr'] = email_table['user_country_encoded'].map(country_ctr)
email_table['purchase_bin'] = pd.cut(email_table['user_past_purchases'], bins=[-1, 0, 5, 20, 100], labels=['none', 'low', 'med', 'high'])
email_table['purchase_bin_encoded'] = email_table['purchase_bin'].astype('category').cat.codes

features = [
    'email_version_encoded',
    'email_text_encoded',
    'hour',
    'weekday_encoded',
    'user_country_encoded',
    'user_past_purchases',
    'is_weekend',
    'is_work_hour',
    'email_sent_bin_encoded',
    'version_text_combo',
    'user_engagement',
    'country_ctr',
    'purchase_bin_encoded'
]
X = email_table[features]
y = email_table['clicked']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


from sklearn.model_selection import GridSearchCV

param_grid = {
    'C': [1, 10],
    'gamma': [0.01, 0.1],
    'kernel': ['rbf'],  # Just focus on RBF kernel
    'probability': [True]
}

grid_search = GridSearchCV(SVC(), param_grid, cv=3, scoring='roc_auc', n_jobs=-1, verbose=2)
grid_search.fit(X_train, y_train)
best_svc = grid_search.best_estimator_

# Evaluate the tuned model
baseline_ctr = email_table['clicked'].mean()
model_predicted_ctr = best_svc.predict_proba(X)[:, 1].mean() 
improvement = ((model_predicted_ctr - baseline_ctr) / baseline_ctr) * 100
print(f"Tuned Model Potential CTR Improvement: {improvement:.2f}%")