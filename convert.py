import pandas as pd
import json

# читаем Excel
df = pd.read_excel("menu.xlsx")

# удаляем полностью пустые строки
df = df.dropna(how="all")

# нормализуем названия колонок
df.columns = [str(col).strip().lower() for col in df.columns]

data = []

for i, row in df.iterrows():
    # --- цена ---
    price = row.get("цена", 0)
    if pd.isna(price):
        price = 0

    # --- название ---
    name = row.get("название", "")
    if pd.isna(name) or str(name).strip() == "":
        continue  # пропускаем пустые строки

    # --- описание ---
    composition = row.get("описание", "")
    if pd.isna(composition):
        composition = ""

    item = {
        "id": i + 1,
        "name": str(name).strip(),
        "price": int(price),
        "composition": str(composition).strip(),
        "image": ""
    }

    data.append(item)

# сохраняем JSON
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("data.json успешно обновлён")