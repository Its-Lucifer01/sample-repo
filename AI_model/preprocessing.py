from flask import Flask, jsonify, request
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# Load data
df11 = pd.read_csv(r'D:/ECOVisionaries/my-app/backend/data/GlobalFoodEmissions-1.csv')
df12 = pd.read_csv(r'D:/ECOVisionaries/my-app/backend/data/GlobalFoodEmissions-2.csv')
df13 = pd.read_csv(r'D:/ECOVisionaries/my-app/backend/data/GlobalFoodEmissions-3.csv')
df14 = pd.read_csv(r'D:/ECOVisionaries/my-app/backend/data/GlobalFoodEmissions-4.csv')
df21 = pd.read_csv(r'D:/ECOVisionaries/my-app/backend/data/Exploring Food Waste Data-2021.csv')
df22 = pd.read_csv(r'D:/ECOVisionaries/my-app/backend/data/Exploring Food Waste Data-2022.csv')
df23 = pd.read_csv(r'D:/ECOVisionaries/my-app/backend/data/Exploring Food Waste Data-2023.csv')
df24 = pd.read_csv(r'D:/ECOVisionaries/my-app/backend/data/Exploring Food Waste Data-timeseries.csv')
df25 = pd.read_csv(r'D:/ECOVisionaries/my-app/backend/data/Exploring Food Waste Data-Food Waste data and research - by country.csv')
df26 = pd.read_csv(r'D:/ECOVisionaries/my-app/backend/data/Exploring Food Waste Data-M49.csv')
df3 = pd.read_csv(r'D:/ECOVisionaries/my-app/backend/data/All Agriculture related Datasets for India.csv')
df41 = pd.read_csv(r'D:/ECOVisionaries/my-app/backend/data/Global Food Security Index 2019.csv', header=1)
df42 = pd.read_csv(r'D:/ECOVisionaries/my-app/backend/data/Global Food Security Index 2022.csv')

# Process data
df25.rename(columns={'Country': 'country'}, inplace=True)
data = df25.merge(df21, on='country', suffixes=('_df25', '_df21'))
data = data.merge(df22, on='country', suffixes=('_df21', '_df22'))
data = data.merge(df23, on='country', suffixes=('_df 22', '_df23'))
data = data.merge(df24, on='country', suffixes=('_df23', '_df24'))

iso_columns = [col for col in data.columns if 'iso_code' in col]
data_cleaned = data.drop(columns=iso_columns)

columns_to_drop = ['area_sq_km_df23', 'density_/sq_km_df23', 'growth_rate_df21', 'growth_rate_df22']
data_cleaned = data_cleaned.drop(columns=columns_to_drop)

columns_to_drop = ['world_%_df21', 'world_%_df22', 'rank_df22', 'rank_df21']
data_cleaned = data_cleaned.drop(columns=columns_to_drop)

columns_to_drop = ['Source']
data_cleaned = data_cleaned.drop(columns=columns_to_drop)

columns_to_drop = ['un_member']
data_cleaned = data_cleaned.drop(columns=columns_to_drop)

data_cleaned['2021_population'] = pd.to_numeric(data_cleaned['2021_population'].astype(str).str.replace(',', ''), errors='coerce')
data_cleaned['2022_population'] = pd.to_numeric(data_cleaned['2022_population'].astype(str).str.replace(',', ''), errors='coerce')
data_cleaned['2023_last_updated'] = pd.to_numeric(data_cleaned['2023_last_updated'].astype(str).str.replace(',', ''), errors='coerce')

X = data_cleaned[['2021_population', '2022_population', 'density_sq_km']]
y = data_cleaned['combined figures (kg/capita/year)']

X['density_sq_km'] = X['density_sq_km'].str.extract('(\d+)').astype(float)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=101)
model = RandomForestRegressor()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Absolute Error: {mae}')
print(f'R-squared: {r2}')

# Create a Flask app
app = Flask(__name__)

# Define routes
@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({
        'df11': df11.to_dict(orient='records'),
        'df12': df12.to_dict(orient='records'),
        'df13': df13.to_dict(orient='records'),
        'df14': df14.to_dict(orient='records'),
        'df21': df21.to_dict(orient='records'),
        'df22': df22.to_dict(orient='records'),
        'df23': df23.to_dict(orient='records'),
        'df24': df24.to_dict(orient='records'),
        'df25': df25.to_dict(orient='records'),
        'df26': df26.to_dict(orient='records'),
        'df3': df3.to_dict(orient='records'),
        'df41': df41.to_dict(orient='records'),
        'df42': df42.to_dict(orient='records'),
        'data': data.to_dict(orient='records'),
        'data_cleaned': data_cleaned.to_dict(orient='records')
    })

@app.route('/api/model', methods=['GET'])
def get_model():
    return jsonify({
        'mae': mae,
        'r2': r2
    })

@app.route('/api/figures', methods=['GET'])
def get_figures():
    fig = px.scatter(x=y_test, y=y_pred, trendline='ols')
    return jsonify(fig.to_dict())

if __name__ == '__main__':
    app.run(debug=True)