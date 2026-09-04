from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def webhook():
    if request.method == 'POST':
        datos = request.get_json()
        print("Webhook recibido:", datos)
        return jsonify({"status": "recibido"}), 200
    return "Servidor activo", 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
