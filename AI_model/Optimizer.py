from flask import Flask, jsonify
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from preprocessing import app, data_cleaned, model

app = Flask(__name__)

# Load data
df23 = pd.read_csv(r'D:/ECOVisionaries/my-app/backend/data/Exploring Food Waste Data-2023.csv')
df24 = pd.read_csv(r'D:/ECOVisionaries/my-app/backend/data/Exploring Food Waste Data-timeseries.csv')
df41 = pd.read_csv(r'D:/ECOVisionaries/my-app/backend/data/Global Food Security Index 2019.csv', header = 1)
df42 = pd.read_csv(r'D:/ECOVisionaries/my-app/backend/data/Global Food Security Index 2022.csv')

# Process data
data_3f = (df23
            .merge(df24, on='country')
            .merge(df41, left_on='country', right_on='Country')  
            .merge(df42, left_on='country', right_on='Country'))  

data_3f_cleaned = data_3f.drop(columns=['Unnamed: 0', 'iso_code_y', 'Country_y', '0', 'No [7]'])

data_3f_cleaned = data_3f_cleaned.rename(columns={
    'iso_code_x': 'iso_code',
    'Country_x': 'Country',
    'Overall Score': 'Overall_Score',
    'Affordability_x': 'Affordability',
    'Availability_x': 'Availability',
    'Quality & safety': 'Quality_and_Safety'})


@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({
        'data': data_3f_cleaned.to_dict(orient='records')
    })

@app.route('/api/correlation-matrix', methods=['GET'])
def get_correlation_matrix():
    numeric_data_f3 = data_3f_cleaned.select_dtypes(include=[np.number])
    correlation_matrix_f3 = numeric_data_f3.corr()
    return jsonify(correlation_matrix_f3.to_dict())

@app.route('/api/overall-score-distribution', methods=['GET'])
def get_overall_score_distribution():
    plt.figure(figsize=(10, 6))
    sns.histplot(data_3f_cleaned['Overall_Score'], bins=10, kde=True)
    plt.title('Distribution of Overall Scores')
    plt.xlabel('Overall Score')
    plt.ylabel('Frequency')
    plt.grid()
    plt.savefig('overall_score_distribution.png')
    return jsonify({'message': 'Plot saved to overall_score_distribution.png'})

@app.route('/api/affordability-by-country', methods=['GET'])
def get_affordability_by_country():
    plt.figure(figsize=(100, 100))
    sns.boxplot(x='country', y='Affordability', data=data_3f_cleaned)
    plt.title('Affordability by Country')
    plt.ylabel('Affordability')
    plt.xlabel('Country')
    plt.grid()
    plt.savefig('affordability_by_country.png')
    return jsonify({'message': 'Plot saved to affordability_by_country.png'})

@app.route('/api/average-scores-by-category', methods=['GET'])
def get_average_scores_by_category():
    average_scores = data_3f_cleaned[['country', 'Overall_Score', 'Affordability', 'Availability', 'Quality_and_Safety']].set_index('country').mean()
    average_scores.plot(kind='bar', figsize=(10, 6), color=['blue', 'orange', 'green', 'red'])
    plt.title('Average Scores by Category')
    plt.ylabel('Average Score')
    plt.xticks(rotation=45)
    plt.grid()
    plt.savefig('average_scores_by_category.png')
    return jsonify({'message': 'Plot saved to average_scores_by_category.png'})


if __name__ == '__main__':
    app.run(debug=True)