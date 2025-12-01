import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Disable SSL warnings
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# UPDATE THIS WITH YOUR REST URL FROM STEP 3
url = "https://oracleapex.com/ords/biruky/posts/"

# Add browser headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    'Accept': 'application/json'
}

try:
    # Call the REST endpoint
    print("Calling REST API...")
    response = requests.get(url, headers=headers, timeout=30, verify=False)
    
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        print("\n✓ SUCCESS! Got JSON data:")
        print(data)
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        
except Exception as e:
    print(f"Connection error: {e}")