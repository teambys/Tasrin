from flask import Flask, render_template, request, jsonify
import requests
import random
import uuid
import threading
import time

app = Flask(__name__)

user_agents = [
    "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15"
]

task_running = False
logs = []

def generate_random_device_id():
    return str(uuid.uuid4())

def send_requests():
    global task_running, logs
    while task_running:
        user_agent = random.choice(user_agents)
        device_id = generate_random_device_id()
        
        headers = {
            "User-Agent": user_agent,
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
        }
        
        data = {
            "username": "tasin95775",
            "question": "এই সব খেলা ইনবক্সে করলেই তো হয় হুদাই সিঙ্গেলদের জ্বালাতন করার কোনো মানে হয়? - পরের বার এইটার রিপ্লাই দিয়েন",
            "deviceId": device_id,
            "gameSlug": "",
            "referrer": ""
        }
        
        try:
            response = requests.post("https://ngl.link/api/submit", headers=headers, data=data)
            log_message = f"Success: {response.status_code}" if response.status_code == 200 else f"Failed: {response.status_code}"
        except requests.exceptions.RequestException as e:
            log_message = f"Request failed: {e}"
        
        logs.append(log_message)
        if len(logs) > 100:  # Keep only the latest 100 log entries
            logs.pop(0)
        
        time.sleep(1)  # Pause between requests

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start():
    global task_running
    if not task_running:
        task_running = True
        thread = threading.Thread(target=send_requests)
        thread.start()
    return '', 204

@app.route('/stop', methods=['POST'])
def stop():
    global task_running
    task_running = False
    return '', 204

@app.route('/status')
def status():
    message = "Task is running." if task_running else "Task is stopped. Ready to start."
    return jsonify({"task_running": task_running, "message": message})

@app.route('/logs')
def get_logs():
    return jsonify({"logs": logs})

def keep_alive():
    url = "https://tasrin.onrender.com"
    interval = 600  # Ping every 10 minutes

    while True:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"Successfully pinged {url} - Status Code: {response.status_code}")
            else:
                print(f"Failed to ping {url} - Status Code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error pinging {url}: {e}")

        time.sleep(interval)

if __name__ == '__main__':
    threading.Thread(target=keep_alive, daemon=True).start()
    app.run(host='0.0.0.0', port=5000, debug=True)
