import requests

URL = "https://services.swpc.noaa.gov/text/3-day-forecast.txt"

r = requests.get(URL, timeout=30)
print("HTTP:", r.status_code)
print("Length:", len(r.text))

with open("forecast.txt", "w", encoding="utf-8") as f:
    f.write(r.text)

URL = "https://services.swpc.noaa.gov/text/27-day-outlook.txt"

r = requests.get(URL, timeout=30)
print("HTTP:", r.status_code)
print("Length:", len(r.text))

with open("forecast1.txt", "w", encoding="utf-8") as f:
    f.write(r.text)
if r.status_code == 200:
    with open("forecast1.txt", "w", encoding="utf-8") as f:
        f.write(r.text)
else:
    print("Ошибка NOAA:", r.status_code)
