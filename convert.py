import pandas as pd
import json

# читаем Excel
df = pd.read_excel("menu.xlsx")

# убираем пустые строки
df = df.dropna(how="all")

# нормализуем названия колонок
df.columns = [str(col).strip().lower() for col in df.columns]

# маппинг колонок (под твою таблицу)
mapping = {
    "название": "name",
    "цена": "price",
    "описание": "composition"
}

data = []
for i, row in df.iterrows():
    item = {
        "id": i + 1,
        "name": str(row.get("название", "")),
        "price": int(row.get("цена", 0)),
        "composition": str(row.get("описание", "")),
        "image": ""
    }
    data.append(item)

# сохраняем JSON
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("data.json обновлён")
