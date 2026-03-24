import pandas as pd
import json

# читаем Excel
df = pd.read_excel("menu.xlsx")

print("Колонки в Excel:", df.columns.tolist())

# удаляем пустые строки
df = df.dropna(how="all")

data = []

for i, row in df.iterrows():
    row_dict = row.to_dict()

    # DEBUG — покажет что реально читается
    print(row_dict)

    # пытаемся взять значения по любым возможным названиям
    name = row_dict.get("Название") or row_dict.get("название") or ""
    price = row_dict.get("Цена") or row_dict.get("цена") or 0
    composition = row_dict.get("Описание") or row_dict.get("описание") or ""

    # если название пустое — пропускаем
    if pd.isna(name) or str(name).strip() == "":
        continue

    # фикс цены
    if pd.isna(price):
        price = 0

    item = {
        "id": len(data) + 1,
        "name": str(name).strip(),
        "price": int(float(price)),
        "composition": str(composition).strip(),
        "image": ""
    }

    data.append(item)

# сохраняем JSON
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("ГОТОВО. Всего товаров:", len(data))