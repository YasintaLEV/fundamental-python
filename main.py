import requests

print("Hello World!")
try:
    r = requests.get("https://google.com")
    if r.status_code == 200:
        print(r.text)
except Exception as e:
    print('404 eror', e)