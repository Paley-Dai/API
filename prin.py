from flask import Flask, jsonify
import json

app = Flask(__name__)

# Route to get data from the JSON file
@app.route('/get_data', methods=['GET'])
def get_data():
    try:
        # Read data from the JSON file
        with open('new.json', 'r') as f:
            data = json.load(f)
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
