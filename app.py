from flask import Flask, jsonify
import socket

app = Flask(__name__)

@app.route('/')
def home():
    # HTML과 인라인 CSS를 사용하여 디자인을 입혔습니다.
    return f"""
    <div style="
        display: flex; 
        flex-direction: column; 
        justify-content: center; 
        align-items: center; 
        height: 100vh; 
        font-family: 'Arial', sans-serif;
        background-color: #e3f2fd;
        margin: 0;
    ">
        <h1 style="color: #1565c0; font-size: 4rem; margin-bottom: 10px;">🚀 MISSION COMPLETE!</h1>
        <h2 style="color: #0d47a1; font-size: 2rem;">Woo-hyeok's CI/CD Pipeline is Working!</h2>
        <div style="
            background: white; 
            padding: 20px; 
            border-radius: 15px; 
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            margin-top: 20px;
        ">
            <p style="font-size: 1.2rem; color: #555;">
                <b>📍 Current Host:</b> <span style="color: #d32f2f;">{socket.gethostname()}</span>
            </p>
        </div>
        <p style="margin-top: 30px; color: #999;">Last Updated: 2026-04-04</p>
    </div>
    """

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)