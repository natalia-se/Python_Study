import requests
username = 'natalia-se'
url = f'https://api.github.com/users/{username}/repos'
response = requests.get(url)
if response.status_code == 200:    
    repos = response.json()    
    for repo in repos:        
        print(f"Repo Name: {repo['name']}")
    else: print(f"Failed to retrieve repositories. Status code: {response.status_code}")