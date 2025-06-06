import requests

artifactory_url = "https://your-artifactory-domain/artifactory"
access_token = "your_existing_admin_token"
username = "your_service_user"  

url = f"{artifactory_url}/api/security/token"

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/x-www-form-urlencoded"
}

payload = {
    "username": username,
    "expires_in": 0 
}

response = requests.post(url, headers=headers, data=payload)

if response.status_code == 200:
    token_data = response.json()
    print("New access token:")
    print(token_data["access_token"])
else:
    print(f"Failed to create token: {response.status_code}")
    print(response.text)
