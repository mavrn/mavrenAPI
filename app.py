from flask import Flask, request, jsonify
import rembg

app = Flask(__name__)

@app.route('/remove-background', methods=['POST'])
def remove_background():
    try:
        image_data = request.get_data()
        processed_image_data = rembg.remove(image_data)

        return jsonify({'result': 'success', 'processed_image': processed_image_data.decode()})
    except Exception as e:
        print(e)
        return jsonify({'result': 'error', 'message': 'Internal Server Error'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)