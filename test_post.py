import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# UPDATE THIS WITH YOUR URL
url = "https://oracleapex.com/ords/biruky/posts/"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

# Data to POST
payload = {
    "text": "Created from Python in Codespaces"
}

try:
    print("Creating new post via REST API...")
    response = requests.post(
        url,
        data=json.dumps(payload),
        headers=headers,
        timeout=30,
        verify=False
    )
    
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 201:
        print("✓ SUCCESS! Post created:")
        print(response.json())
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        
except Exception as e:
    print(f"Connection error: {e}")