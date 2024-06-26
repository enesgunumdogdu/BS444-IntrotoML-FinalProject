import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import xgboost as xgb
import lightgbm as lgb
import tkinter as tk

ages = pd.read_csv('Ages.csv')
data = pd.read_csv('data.csv')

data.rename(columns={'Unnamed: 0': 'Sample Accession'}, inplace=True)
ages.head()
data.head()

data_cleaned = data.drop(data.columns[1], axis=1)
merged_data = pd.merge(ages, data_cleaned, on='Sample Accession')

X = merged_data.drop(columns=['Sample Accession', 'Age'])
y = merged_data['Age']

merged_data = pd.merge(ages, data, on='Sample Accession')
merged_data.head()
merged_data.tail()

X = X.apply(pd.to_numeric, errors='coerce')
X = X.fillna(0) 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

gb_model = GradientBoostingRegressor(n_estimators=100, random_state=42)
gb_model.fit(X_train, y_train)

xgb_model = xgb.XGBRegressor(n_estimators=100, random_state=42)
xgb_model.fit(X_train, y_train)

models = {'Random Forest': rf_model, 'Gradient Boosting': gb_model, 'XGBoost': xgb_model} results = {} for name, model in models.items(): y_pred = model.predict(X_test) mae = mean_absolute_error(y_test, y_pred) r2 = r2_score(y_test, y_pred) results[name] = (mae, r2)

root = tk.Tk()
root.title("BS444 Introduction To ML Report")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

ttk.Label(frame, text="Model").grid(column=1, row=1)
ttk.Label(frame, text="Mean Absolute Error").grid(column=2, row=1)
ttk.Label(frame, text="R^2 Score").grid(column=3, row=1)

for idx, (name, (mae, r2)) in enumerate(results.items(), start=2):
    ttk.Label(frame, text=name).grid(column=1, row=idx, sticky=tk.W)
    ttk.Label(frame, text=f"{mae:.2f}").grid(column=2, row=idx, sticky=tk.W)
    ttk.Label(frame, text=f"{r2:.2f}").grid(column=3, row=idx, sticky=tk.W)

root.mainloop()
