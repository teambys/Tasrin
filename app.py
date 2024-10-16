from flask import Flask, render_template, request, redirect, url_for
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

def generate_random_device_id():
    return str(uuid.uuid4())

def send_requests():
    global task_running
    while task_running:
        user_agent = random.choice(user_agents)
        device_id = generate_random_device_id()
        
        headers = {
            "User-Agent": user_agent,
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
        }
        
        data = {
            "username": "tasin95775",
            "question": "Sample question",
            "deviceId": device_id,
            "gameSlug": "",
            "referrer": ""
        }
        
        try:
            response = requests.post("https://ngl.link/api/submit", headers=headers, data=data)
            log_message = f"Success: {response.status_code}" if response.status_code == 200 else f"Failed: {response.status_code}"
            print(log_message)
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")

        time.sleep(1)  # Pause between requests

@app.route('/', methods=['GET', 'POST'])
def index():
    global task_running
    if request.method == 'POST':
        if not task_running:
            task_running = True
            thread = threading.Thread(target=send_requests)
            thread.start()
            return redirect(url_for('index'))
    return render_template('index.html')

@app.route('/stop', methods=['POST'])
def stop():
    global task_running
    task_running = False
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
