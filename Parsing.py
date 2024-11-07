import requests
import json
import pandas as pd

url = "https://api.foursquare.com/v3/places/search"
print("Введите название объекта поиска")
k = input()

params = {
    "query": k,
    "ll": "59.933572,30.328414",
    "open_now": "true",
    "sort": "DISTANCE",
    "lang": "ru"
}

headers = {
    "Accept": "application/json",
    "Authorization": "fsq3DmACLLOeiKZbw4TJefXGmFnshxHPkyVMKAbZbnOc5Iw="  # Убедитесь, что ваш токен действителен
}

# Выполняем запрос
response = requests.get(url, params=params, headers=headers)
j_data = response.json()

# Проверяем, содержит ли ответ данные
if 'results' in j_data:
    # Извлекаем данные из списка результатов
    filtered_data = [
        {"name": place.get("name"), "address": place.get("location", {}).get("formatted_address")}
        for place in j_data["results"]
    ]

    # Выводим отфильтрованные данные и сохраняем в JSON-файл
    df = pd.DataFrame(filtered_data)
    print(df)

    with open("output_filtered.json", "w", encoding="utf-8") as file:
        json.dump(filtered_data, file, indent=4, ensure_ascii=False)
else:
    print("Данные не найдены в ответе API.")

df = pd.DataFrame(filtered_data)
