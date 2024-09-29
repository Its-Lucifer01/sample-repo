from flask import Flask, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
import os
import pandas as pd

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains

# MongoDB configuration
app.config["MONGO_URI"] = "mongodb://localhost:27017/yourdbname"
mongo = PyMongo(app)

# Load data from CSV files
df11 = pd.read_csv(r'D:/ECOVisionaries/my-app/backend/data/GlobalFoodEmissions-1.csv')
df12 = pd.read_csv(r'D:/ECOVisionaries/my-app/backend/data/GlobalFoodEmissions-2.csv')

@app.route('/add_item', methods=['POST'])
def add_item():
    item = {"name": "Example Item", "quantity": 10}
    mongo.db.items.insert_one(item)
    return jsonify({"message": "Item added successfully!"})

@app.route('/get_items', methods=['GET'])
def get_items():
    items = mongo.db.items.find()
    return jsonify([item for item in items])

@app.route('/api/revenue', methods=['GET'])
def get_revenue():
    revenue_data = df11.groupby('Food System Stage')['GHG Emissions'].sum().reset_index()
    return jsonify(revenue_data.to_dict(orient='records'))

@app.route('/api/user-growth', methods=['GET'])
def get_user_growth():
    user_growth_data = df12[['Food product', 'Total_emissions']].copy()
    return jsonify(user_growth_data.to_dict(orient='records'))

@app.route('/api/ghg-emissions', methods=['GET'])
def get_ghg_emissions():
    ghg_emissions = df11.groupby('Food System Stage')['GHG Emissions'].sum().reset_index()
    return jsonify(ghg_emissions.to_dict(orient='records'))

@app.route('/api/total-emissions', methods=['GET'])
def get_total_emissions():
    total_emissions = df12[['Food product', 'Total_emissions']].copy()
    return jsonify(total_emissions.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)