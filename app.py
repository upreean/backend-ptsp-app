from flask import Flask, jsonify
import json

app = Flask(__name__)

def load_data_mahasiswa():
    try:
        with open('data_mahasiswa.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Error: File 'data_mahasiswa.json' tidak ditemukan.")
        return []

data_mahasiswa = load_data_mahasiswa()

@app.route('/mahasiswa/<string:nim>', methods=['GET'])
def get_mahasiswa_by_nim(nim):
    mahasiswa_ditemukan = [
        mahasiswa for mahasiswa in data_mahasiswa 
        if mahasiswa.get('nim') == nim
    ]
    if mahasiswa_ditemukan:
        return jsonify(mahasiswa_ditemukan)
    else:
        return jsonify({"error": "Data mahasiswa tidak ditemukan"}), 404

if __name__ == '__main__':
    app.run(port=5000, debug=True)