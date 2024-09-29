from flask import Flask, jsonify, request
import pandas as pd
import plotly.express as px
from preprocessing import app, data_cleaned, model
import Optimizer

app = Flask(__name__)

# Load data
df11 = pd.read_csv(r'D:/ECOVisionaries/my-app/backend/data/GlobalFoodEmissions-1.csv')
df12 = pd.read_csv(r'D:/ECOVisionaries/my-app/backend/data/GlobalFoodEmissions-1.csv')
df13 = pd.read_csv(r'D:/ECOVisionaries/my-app/backend/data/GlobalFoodEmissions-1.csv')
df14 = pd.read_csv(r'D:/ECOVisionaries/my-app/backend/data/GlobalFoodEmissions-1.csv')
df41 = pd.read_csv(r'D:/ECOVisionaries/my-app/backend/data/Global Food Security Index 2019.csv')
df42 = pd.read_csv(r'D:/ECOVisionaries/my-app/backend/data/Global Food Security Index 2022.csv')


# Process data
ghg_by_stage = df11.groupby('Food System Stage')['GHG Emissions'].sum().reset_index()
ghg_by_stage.sort_values(by='GHG Emissions', ascending=False, inplace=True)

total_emissions_by_product = df12[['Food product', 'Total_emissions']].copy()
total_emissions_by_product.sort_values(by='Total_emissions', ascending=False, inplace=True)

global_avg_emissions = df13[['Food product', 'Total Global Average GHG Emissions per kg']].copy()
global_avg_emissions.sort_values(by='Total Global Average GHG Emissions per kg', ascending=False, inplace=True)

emission_intensity = df14.groupby(['Region', 'Animal species'])['Emission Intensity (kg CO2e per kg protein)'].mean().reset_index()
emission_intensity.sort_values(by='Emission Intensity (kg CO2e per kg protein)', ascending=False, inplace=True)

food_security_index = df41[['Country', 'Overall Score', 'Affordability', 'Availability']].copy()
food_security_index.sort_values(by='Overall Score', ascending=False, inplace=True)

quality_safety_index = df42[['Country', 'Overall score', 'Quality and Safety']].copy()
quality_safety_index.sort_values(by='Overall score', ascending=False, inplace=True)

# Create figures
fig_emissions_stage = px.bar(ghg_by_stage, x='Food System Stage', y='GHG Emissions', title='Total GHG Emissions by Food System Stage')
fig_emissions_product = px.bar(total_emissions_by_product, x='Food product', y='Total_emissions', title='Total Emissions by Food Product')
fig_global_avg_emissions = px.bar(global_avg_emissions, x='Food product', y='Total Global Average GHG Emissions per kg', title='Global Average GHG Emissions per Food Product')
fig_emission_intensity = px.bar(emission_intensity, x='Animal species', y='Emission Intensity (kg CO2e per kg protein)', color='Region', title='Average Emission Intensity by Animal Species')
fig_food_security = px.bar(food_security_index, x='Country', y='Overall Score', title='Food Security Index by Country')
fig_quality_safety = px.bar(quality_safety_index, x='Country', y='Overall score', title='Quality and Safety Index by Country')

# Create Flask API
@app.route('/api/dashboard', methods=['GET'])
def get_dashboard_data():
    return jsonify({
        'ghg_emissions': ghg_by_stage.to_dict(orient='records'),
        'total_emissions': total_emissions_by_product.to_dict(orient='records'),
        'global_avg_emissions': global_avg_emissions.to_dict(orient='records'),
        'emission_intensity': emission_intensity.to_dict(orient='records'),
        'food_security': food_security_index.to_dict(orient='records'),
        'quality_safety': quality_safety_index.to_dict(orient='records')
    })

@app.route('/api/figures', methods=['GET'])
def get_figures():
    return jsonify({
        'fig_emissions_stage': fig_emissions_stage.to_dict(),
        'fig_emissions_product': fig_emissions_product.to_dict(),
        'fig_global_avg_emissions': fig_global_avg_emissions.to_dict(),
        'fig_emission_intensity': fig_emission_intensity.to_dict(),
        'fig_food_security': fig_food_security.to_dict(),
        'fig_quality_safety': fig_quality_safety.to_dict()
    })

if __name__ == '__main__':
    app.run(debug=True)