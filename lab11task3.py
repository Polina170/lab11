import csv
with open("shop.csv", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    print("Нужно купить:")
    total = 0
    for row in reader:
        product = row["Продукт"]
        count = int(row["Количество"])
        price = int(row["Цена"])

        print(f"{product} - {count} шт. за {price} рублей")
        total = total + count * price

    print(f"Итоговая сумма: {total} рублей")