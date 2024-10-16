import requests
import random
import uuid

# List of possible User-Agent strings to randomly choose from
user_agents = [
    "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15"
]

# Function to generate a random device ID
def generate_random_device_id():
    return str(uuid.uuid4())

# Function to perform the POST request with random User-Agent and Device ID
def send_request():
    url = "https://ngl.link/api/submit"
    
    # Randomly select a User-Agent
    user_agent = random.choice(user_agents)
    
    # Generate a random Device ID
    device_id = generate_random_device_id()
    
    headers = {
        "Host": "ngl.link",
        "Connection": "keep-alive",
        "Content-Length": "138",
        "sec-ch-ua-platform": '"Android"',
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": user_agent,
        "Accept": "*/*",
        "sec-ch-ua": '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "sec-ch-ua-mobile": "?1",
        "Origin": "https://ngl.link",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://ngl.link/tasin95775/",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,bn;q=0.7",
        "Cookie": "_ga=GA1.1.315432874.1728956959; __stripe_mid=88b4202d-3b3d-4ec3-bd30-1379deb6b05c41bc77; __stripe_sid=2eaf2a8b-b386-446c-94e6-a680e7da73b1ad2e43; mp_e8e1a30fe6d7dacfa1353b45d6093a00_mixpanel=%7B%22distinct_id%22%3A%20%22%24device%3A1928ddd8452fb8-0bb02b182a374f-b457559-7d0a0-1928ddd8453fba%22%2C%22%24device_id%22%3A%20%221928ddd8452fb8-0bb02b182a374f-b457559-7d0a0-1928ddd8453fba%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%7D; _ga_5DV1ZR5ZHG=GS1.1.1729088692.3.1.1729089066.0.0.0"
    }
    
    data = {
        "username": "gajarbotol",
        "question": "এই সব খেলা ইনবক্সে করলেই তো হয় হুদাই সিঙ্গেলদের জ্বালাতন করার কোনো মানে হয়? - পরের বার এইটার রিপ্লাই দিয়েন",
        "deviceId": device_id,
        "gameSlug": "",
        "referrer": ""
    }
    
    response = requests.post(url, headers=headers, data=data)
    
    # Print the response details
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)
    print("Used User-Agent:", user_agent)
    print("Generated Device ID:", device_id)

# Execute the function
send_request()
