from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Weather API key
weather_api_key = "e6c98122c38d2f39f93e5ce1c20a0178"

# OpenRouteService API key
ors_api_key = "5b3ce3597851110001cf62488985bce4d88347c5b6c81fc0e13eb089"

@app.route('/weather', methods=['GET'])
def get_weather():
    location = request.args.get('location')
    if location:
        weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={weather_api_key}&units=metric"
        weather_response = requests.get(weather_url)
        weather_data = weather_response.json()
        if weather_response.status_code == 200:
            temperature = weather_data['main']['temp']
            weather_condition = weather_data['weather'][0]['description']
            return jsonify({'temperature': temperature, 'weather_condition': weather_condition})
        else:
            return jsonify({'error': 'Failed to fetch weather data'}), 400
    else:
        return jsonify({'error': 'Location is required'}), 400

@app.route('/route', methods=['GET'])
def get_route():
    start_coords = request.args.get('start_coords')
    end_coords = request.args.get('end_coords')
    if start_coords and end_coords:
        start_coords = [float(x) for x in start_coords.split(',')]
        end_coords = [float(x) for x in end_coords.split(',')]
        ors_url = "https://api.openrouteservice.org/v2/directions/driving-car"
        params = {
            'api_key': ors_api_key,
            'start': f"{start_coords[0]},{start_coords[1]}",
            'end': f"{end_coords[0]},{end_coords[1]}"
        }
        route_response = requests.get(ors_url, params=params)
        route_data = route_response.json()
        if route_response.status_code == 200 and 'features' in route_data:
            try:
                distance = route_data['features'][0]['properties']['segments'][0]['summary']['distance'] / 1000
                duration = route_data['features'][0]['properties']['segments'][0]['summary']['duration'] / 60
                return jsonify({'distance': distance, 'duration': duration})
            except (IndexError, KeyError) as e:
                return jsonify({'error': 'Error parsing route data'}), 400
        else:
            return jsonify({'error': 'Failed to fetch route data'}), 400
    else:
        return jsonify({'error': 'Start and end coordinates are required'}), 400
    
# Base URL for the Grocery Store API
BASE_URL = "https://simple-grocery-store-api.glitch.me"

# Endpoint for checking the status of the API
@app.route('/api/status', methods=['GET'])
def get_status():
    response = requests.get(f"{BASE_URL}/status")
    return jsonify(response.json()), response.status_code

# Endpoint for getting all products
@app.route('/api/products', methods=['GET'])
def get_products():
    category = request.args.get('category')
    results = request.args.get('results')
    available = request.args.get('available')
    
    params = {}
    if category:
        params['category'] = category
    if results:
        params['results'] = results
    if available:
        params['available'] = available
    
    response = requests.get(f"{BASE_URL}/products", params=params)
    return jsonify(response.json()), response.status_code

# Endpoint for getting a single product by ID
@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    response = requests.get(f"{BASE_URL}/products/{product_id}")
    return jsonify(response.json()), response.status_code

# Endpoint for creating a new cart
@app.route('/api/carts', methods=['POST'])
def create_cart():
    response = requests.post(f"{BASE_URL}/carts")
    return jsonify(response.json()), response.status_code

# Endpoint for adding an item to the cart
@app.route('/api/carts/<string:cart_id>/items', methods=['POST'])
def add_to_cart(cart_id):
    data = request.json
    response = requests.post(f"{BASE_URL}/carts/{cart_id}/items", json=data)
    return jsonify(response.json()), response.status_code

# Endpoint for getting cart items
@app.route('/api/carts/<string:cart_id>/items', methods=['GET'])
def get_cart_items(cart_id):
    response = requests.get(f"{BASE_URL}/carts/{cart_id}/items")
    return jsonify(response.json()), response.status_code

# Endpoint for creating an order
@app.route('/api/orders', methods=['POST'])
def create_order():
    data = request.json
    headers = {'Authorization': f"Bearer {data.get('token')}"}
    response = requests.post(f"{BASE_URL}/orders", json=data, headers=headers)
    return jsonify(response.json()), response.status_code

if __name__ == '__main__':
    app.run(debug=True)