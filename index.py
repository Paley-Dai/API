from flask import Flask, request, jsonify
from PIL import Image
import io

app = Flask(__name__)

@app.route('/receive_frame', methods=['POST'])
def receive_frame():
    # Assuming you're receiving JPEG frames
    
    frame_data = request.data
    
    img = Image.open(io.BytesIO(frame_data))
    img.save("receivedframe.jpg")
    
    print(frame_data)
    # Process the frame data as needed (e.g., save it to a file, display it, etc.)
    # For example, you can save it to a file named 'received_frame.jpg'
    with open('received_frame.jpg', 'wb') as f:
        f.write(frame_data)
    

    return '<img src="/static/received_frame.jpg" alt="Received Frame">', 200

@app.route('/check', methods=['GET'])
def simple():
    return jsonify({"name": "Sanjay"})

if __name__ == '__main__':
    app.run(host='192.168.43.88',port=3000)
